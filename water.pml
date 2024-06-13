load water.xyz
show sticks, water

load water_den.cube, dens_map
load water_pot.cube, pot_map

isosurface 0.002_density, dens_map, 0.002, state=1
ramp_new pot_color_Hartrees, pot_map, [-0.05, 0, 0.05], [red, white, blue]

set surface_color, pot_color_Hartrees
set surface_ramp_above_mode

set transparency=0.2
