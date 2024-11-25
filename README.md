# MCNP to OpenMC SDEF conversion tool

With this tool, you can convert a fusion neutron source from MCNP to OpenMC.

## Currently only cylindrical SDEF with radial and vertical dependent distributions is supported

- At the moment, work has been tested only with fusion neutron sources based on cylindrical geometry with radial and vertical dependent distributions.
- An example of such a source for MCNP can be found in the `/notebooks/data` folder.

### There isn't any methodical V&V on this tool. Use at your own risk.

## Installation

`pip install openmc_sdef_parser*.whl`

## Usage

- Import package:

    `import openmc_sdef_parser as parse`

- Link variable with the path to SDEF file:

    `sdef = parse.make_openmc_source('path/to/sdef')`

- Create settings object:

    `settings = openmc.Settings()`

- Add source to settings attribute:

    `settings.source = sdef`

## Attributes

- `sdef = parse.make_openmc_source('path/to/sdef')`

    - `sdef` is an openmc.IndependentSource object

- `sdef_file` is the path to the SDEF file
- `normalize` is whether to normalize the source per 1. Default is True
- `exclude_first` is whether to exclude the first z bin (vertical distribution). It may be useful in some cases. Default is False, i.e. include the first z bin and exclude the last z bin.

## Plotting

- If you want to plot your SDEF:

    `sdef = parse.make_openmc_source('path/to/sdef')`\
    `parse.plot_source(sdef)`

- Options:
     - By default, the source is normalized to 1.\
       If you want to plot the intensity from min to max, set `intensity_norm = False`
     - You can change the color map with `cmap` and the interpolation method with `interpolation`

     `parse.plot_source(sdef, intensity_norm = False, cmap = 'viridis', interpolation = 'bicubic')`

