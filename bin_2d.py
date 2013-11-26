import numpy as np
import pdb

def bin_2d( xcoords, ycoords, zsignal, nx=30, ny=30 ):
    """
    Bin a 2D data series.
    """
    pt_densities, yedges, xedges = np.histogram2d( ycoords, xcoords, bins=( ny, nx ) )
    dx = np.median( np.diff( xedges ) )
    dy = np.median( np.diff( yedges ) )
    x = 0.5*dx + xedges[:-1]
    y = 0.5*dy + yedges[:-1]
    extent = [ xedges.min(), xedges.max(), yedges.min(), yedges.max() ]
    grid = np.mgrid[ x[0]:x[-1]:nx*1j, y[0]:y[-1]:ny*1j ]
    x_grid = grid[0]
    y_grid = grid[1]
    z_grid = np.zeros( [ ny, nx ] ) + np.nan
    for i in range( nx ):
        for j in range( ny ):
            l = ( ( xcoords>=xedges[i] )*( xcoords<xedges[i+1] )*\
                  ( ycoords>=yedges[j] )*( ycoords<yedges[j+1] ) )
            if np.sum( l )==0:
                continue
            z_grid[j,i] = np.mean( zsignal[l] )
    return x_grid, y_grid, z_grid, pt_densities, extent
