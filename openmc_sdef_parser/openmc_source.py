import openmc_sdef_parser.parse as parse
import openmc

import numpy as np
import matplotlib.pyplot as plt

def make_openmc_source(
    sdef_file: str,
    normalize: bool = False,
    exclude_first: bool = False
) -> openmc.IndependentSource:
    
    """Creates an openmc.IndependentSource object from a MCNP SDEF file.

    Args:
        sdef_file (str): The path to the MCNP SDEF file.
        normalize (bool, optional): Whether to normalize the source per 1. Defaults to False.
        exclude_first (bool, optional): Whether to exclude the first z bin. Defaults to False, i.e. include the first z bin and exclude the last z bin. Defaults to False.
    Returns:
        openmc.IndependentSource: The openmc.IndependentSource object representing the fusion source.
    """
    
    parsed_file = parse.sdef_template(sdef_file)
    
    origin = parsed_file['origin']
    energy = parsed_file['energy']
    r_bins = parsed_file['r_bins']
    z_bins = parsed_file['z_bins']
    r_prob = parsed_file['r_prob']
    z_prob = parsed_file['z_prob']
    wgt = parsed_file['wgt']
    constraints = parsed_file['constraints']
    
    source_mesh = openmc.CylindricalMesh(
        origin=origin,
        r_grid=r_bins,
        z_grid=z_bins)
    
    count = 0
    probs = np.zeros(source_mesh.dimension)
    
    if exclude_first:
        extra = 1
    else:
        extra = 0   
    
    for i, j, k in source_mesh.indices:
        mesh_index = (i-1, j-1, k-1)
        # Multiplication of z and r probabilities to get probability for each mesh cell
        probs[mesh_index] = z_prob[mesh_index[0]+extra][mesh_index[2]] * r_prob[mesh_index[0]] 
        count += 1
    
    if normalize:
        probs = probs / np.sum(probs)
    
    if energy[0] != -4:
        print('Unknown energy distribution. It must be -4 for fusion source.')
    else:
        source = openmc.IndependentSource()
        source.angle = openmc.stats.Isotropic()
        source.energy = openmc.stats.Normal(energy[2] * 1e6, energy[1] / np.sqrt(2) * 1e6 ) # mean_energy[MeV] -> [eV], FWHM/(LN2)^0.5/2 -> sigma[MeV] -> [eV]
        source.space = openmc.stats.MeshSpatial(
            mesh=source_mesh,
            strengths=np.reshape(probs.T, (count, )) * wgt,  # 2D-array -> 1D-array of probabilities
            volume_normalized = False
            )
        if len(constraints) != 0:
            source.constraints['domain_type'] = 'cell'
            source.constraints['domain_ids']  = ' '.join(constraints)
            source.constraints['rejection_strategy']  = 'resample'
        
        return source

def plot_source(
    source: openmc.IndependentSource,
    intensity_norm: bool = True,
    cmap: str = 'jet',
    interpolation: str = None
) -> None:
    
    """Plots the fusion source.

    Args:
        source (openmc.IndependentSource): The openmc.IndependentSource object representing the fusion source translated to OpenMC.
        intensity_norm (bool, optional): Whether to normalize the intensity per 1. Defaults to True.
        cmap (str, optional): color map. Defaults to 'jet'.
        interpolation (str, optional): interpolation method. Defaults to None. You can find more here: https://matplotlib.org/stable/gallery/images_contours_and_fields/interpolation_methods.html
    """
    
    origin = source.space.mesh.origin
    r_bins = source.space.mesh.r_grid
    z_bins = source.space.mesh.z_grid
    
    probs = source.space.strengths
    
    if intensity_norm:
        norm_par = np.max(probs)
    else:
        norm_par = 1

    new_probs = np.where(probs == 0, np.nan, probs)
        
    plt.imshow(new_probs.reshape(len(z_bins)-1, len(r_bins)-1) / norm_par, 
               extent=[r_bins[0]+origin[0], r_bins[-1]+origin[0], z_bins[0]+origin[2], z_bins[-1]+origin[2]], 
               cmap=cmap, 
               interpolation=interpolation,
               vmin=0)
    plt.colorbar()