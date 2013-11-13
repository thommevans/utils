import numpy as np
import pdb

def bin_2d(xcoords, ycoords, zsignal, nx = 30, ny = 30):
    """
    Bin a 2D data series.
    """
    xedges = np.r_[ xcoords.min():xcoords.max():1j*( nx+1 ) ]
    yedges = np.r_[ ycoords.min():ycoords.max():1j*( ny+1 ) ]
    extent = [ xedges.min(), xedges.max(), yedges.min(), yedges.max() ]
    grid = np.mgrid[ xedges[0]:xedges[-1]:1j*nx, yedges[0]:yedges[-1]:1j*ny ]
    x_grid = grid[0]
    y_grid = grid[1]
    z_grid = np.zeros(x_grid.shape) + np.nan
    pt_densities = np.zeros( [ ny, nx ] )
    for i in range(nx):
        for j in range(ny):
            l = ( ( xcoords >= xedges[i] ) * ( xcoords < xedges[i+1] ) * \
                  ( ycoords >= yedges[j] ) * ( ycoords < yedges[j+1] ) )
            if np.sum( l ) == 0:
                continue
            else:
                z_grid[j,i] = np.mean( zsignal[l] )
                pt_densities[j,i] = np.sum( l )
    pt_densities /= pt_densities.sum()
    return x_grid, y_grid, z_grid, pt_densities, extent

def bin_2d_OLD(xcoords, ycoords, zsignal, nx = 30, ny = 30):
    """
    Bin a 2D data series.
    """
    pt_densities, xedges, yedges = np.histogram2d(xcoords, ycoords, bins=(nx,ny))
    extent = [xedges.min(), xedges.max(), yedges.min(), yedges.max()]
    grid = np.mgrid[xedges[0]:xedges[-1]:len(xedges)*1j, yedges[0]:yedges[-1]:len(yedges)*1j]
    x_grid = grid[0]
    y_grid = grid[1]
    z_grid = np.zeros(x_grid.shape) + np.nan
    pdb.set_trace()
    for i in range(nx):
        print xedges[i], xedges[i+1]
        for j in range(ny):
            l = ((xcoords >= xedges[i]) * (xcoords < xedges[i+1]) * \
                     (ycoords >= yedges[j]) * (ycoords < yedges[j+1]))
            if np.sum(l) == 0: continue
            z_grid[i,j] = np.mean(zsignal[l])
    return x_grid, y_grid, z_grid, pt_densities, extent
