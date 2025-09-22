import openmc_sdef_parser.parse as parse
import openmc

import numpy as np
import matplotlib.pyplot as plt

def make_openmc_tokamak_source(
    sdef_file: str,
    normalize: bool = True,
    exclude_first: bool = False
) -> openmc.IndependentSource:
    
    """Creates an openmc.IndependentSource object from a MCNP SDEF file.

    Args:
        sdef_file (str): The path to the MCNP SDEF file.
        normalize (bool, optional): Whether to normalize the source per 1. Defaults to True.
        exclude_first (bool, optional): Whether to exclude the first z bin. Defaults to False, i.e. include the first z bin and exclude the last z bin. Defaults to False.
    Returns:
        openmc.IndependentSource: The openmc.IndependentSource object representing the fusion source.
    """
    
    parsed_file = parse.sdef_tokamak_template(sdef_file)
    
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
    
    if normalize:
        r_prob = r_prob / np.sum(r_prob)
        for i in range(len(z_prob)):
            z_prob[i] = z_prob[i] / np.sum(z_prob[i])
    
    for i, j, k in source_mesh.indices:
        mesh_index = (i-1, j-1, k-1)
        # Multiplication of z and r probabilities to get probability for each mesh cell
        probs[mesh_index] = z_prob[mesh_index[0]+extra][mesh_index[2]] * r_prob[mesh_index[0]]
        count += 1

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

def plot_tokamak_source(
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

def make_openmc_point_source(
    sdef_file: str,
) -> openmc.IndependentSource:

    """Creates an openmc.IndependentSource object from a MCNP SDEF file for a point source with anisotropic angular distribution.

    Args:
        sdef_file (str): The path to the MCNP SDEF file.
    Returns:
        openmc.IndependentSource: The openmc.IndependentSource object representing the point source.
    """
    
    parsed_file = parse.sdef_ps_template(sdef_file)
    
    origin = parsed_file['origin']
    dir = parsed_file['dir']
    reference_uvw = parsed_file['reference_uvw']
    angular_bins = parsed_file['angular_bins']
    angular_prob = parsed_file['angular_prob']
    spatial_bins = parsed_file['spatial_bins'] * 1e6 # [MeV] -> [eV]
    spatial_prob = parsed_file['spatial_prob']
    wgt = parsed_file['wgt'] # TODO: implement weight to OpenMC point source
    
    if dir is None:
        print('Unkown distribution...') # TODO: add more information
    
    source = openmc.IndependentSource()
    
    dir_dist = openmc.stats.Tabular(angular_bins, angular_prob, 'histogram')
    probs = spatial_prob.T
    all_bins = np.tile(spatial_bins, (angular_prob.shape[0], 1))

    tabular_dists = [openmc.stats.Tabular(all_bins[i], probs[:, i] / 1e6, 'histogram') for i in range(probs.shape[1])]

    energy_dist = openmc.stats.Mixture(angular_prob, tabular_dists)
    
    sources = []

    for i, probs in enumerate(angular_prob):
        source = openmc.IndependentSource()
        source.space = openmc.stats.Point(origin)
        #source.space = openmc.stats.CylindricalIndependent(origin=origin, r=openmc.stats.PowerLaw(a=0, b=r, n=1), z=openmc.stats.Uniform(a=-x, b=x), phi=openmc.stats.Uniform(0., 2*np.pi))
        source.energy = energy_dist.distribution[i]
        source.angle = openmc.stats.PolarAzimuthal(mu=openmc.stats.Uniform(angular_bins[i], angular_bins[i+1]), reference_uvw=reference_uvw)
        source.strength = probs
        sources.append(source)
    
    return sources