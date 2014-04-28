import numpy as np
import pdb, warnings

# TODO: This could be sped up by using the numpy histogramdd function
# to first identify the cells that actually contain data points, then
# only bin the f variable in that subset.

def bin_3d( xp, yp, zp, f ):
    """
    Bin a 3D data series.

    xp = [ x, dx ]
    yp = [ y, dy ]
    zp = [ z, dz ]

    where (x,y,z) are the inputs with data values f and
    (dx,dy,dz) are the bin widths to be used along each
    input axis.
    """

    x = xp[0]
    dx = xp[1]
    y = yp[0]
    dy = yp[1]
    z = zp[0]
    dz = zp[1]

    x = x.flatten()
    y = y.flatten()
    z = z.flatten()
    f = f.flatten()
    nf = len( f )
    if ( len( x )==nf )*( len( y )==nf )*( len( z )==nf )==False:
        raise ValueError( 'vector dimensions do not match' )
        
    
    xr = x.max() - x.min()
    yr = y.max() - y.min()
    zr = z.max() - z.min()

    nx = int( np.ceil( xr/dx )+1 )
    ny = int( np.ceil( yr/dy )+1 )
    nz = int( np.ceil( zr/dz )+1 )

    xedges = np.arange( x.min()-0.5*dx, x.max() + 1.5*dx, dx )
    yedges = np.arange( y.min()-0.5*dy, y.max() + 1.5*dy, dy )
    zedges = np.arange( z.min()-0.5*dz, z.max() + 1.5*dz, dz )

    f = f.flatten()
    nf = len( f )

    print '\nBinning {0} values on a {1} x {2} x {3} grid'.format( nf, nx, ny, nz )
    print 'The following pairs of numbers are the number of bins'
    print 'requested and the number being done for each axis:'
    print 'axis1 --> {0}, {1}'.format( nx, len(xedges)-1 )
    print 'axis2 --> {0}, {1}'.format( ny, len(yedges)-1 )
    print 'axis3 --> {0}, {1}'.format( nz, len(zedges)-1 )
    print 'Each pair should therefore be two equal numbers.\n'
    fb = np.zeros( [ nx, ny, nz ] )
    npb = np.zeros( [ nx, ny, nz ] )
    xcents = np.zeros( [ nx, ny, nz ] )
    ycents = np.zeros( [ nx, ny, nz ] )
    zcents = np.zeros( [ nx, ny, nz ] )
    for i in range( nx ):
        print i+1, nx
        ixs_x = ( x>xedges[i] )*( x<=xedges[i+1] )
        xcent_i = 0.5*( xedges[i]+xedges[i+1] )
        if ixs_x.max()==False:
            xcents[i,:,:] = xcent_i
            fb[i,:,:] = 0
            npb[i,:,:] = 0
            continue
        for j in range( ny ):
            ixs_y = ( y[ixs_x]>yedges[j] )*( y[ixs_x]<=yedges[j+1] )
            ycent_j = 0.5*( yedges[j]+yedges[j+1] )
            if ixs_y.max()==False:
                ycents[i,j,:] = ycent_j
                fb[i,j,:] = 0
                npb[i,j,:] = 0
                continue
            for k in range( nz ):
                ixs_z = ( z[ixs_x][ixs_y]>zedges[k] )*( z[ixs_x][ixs_y]<=zedges[k+1] )
                f_in_bin = f[ixs_x][ixs_y][ixs_z]
                npb[i,j,k] = len( f_in_bin )
                if npb[i,j,k]==0:
                    fb[i,j,k] = 0.0
                else:
                    fb[i,j,k] = np.mean( f_in_bin )
                xcents[i,j,k] = xcent_i
                ycents[i,j,k] = ycent_j
                zcents[i,j,k] = 0.5*( zedges[k]+zedges[k+1] )
    return xcents, ycents, zcents, fb, npb
                

    
    
##     pt_densities, yedges, xedges = np.histogram2d( ycoords, xcoords, bins=( ny, nx ) )
##     dx = np.median( np.diff( xedges ) )
##     dy = np.median( np.diff( yedges ) )
##     x = 0.5*dx + xedges[:-1]
##     y = 0.5*dy + yedges[:-1]
##     extent = [ xedges.min(), xedges.max(), yedges.min(), yedges.max() ]
##     grid = np.mgrid[ x[0]:x[-1]:nx*1j, y[0]:y[-1]:ny*1j ]
##     x_grid = grid[0]
##     y_grid = grid[1]
##     z_grid = np.zeros( [ ny, nx ] ) + np.nan
##     for i in range( nx ):
##         for j in range( ny ):
##             l = ( ( xcoords>=xedges[i] )*( xcoords<xedges[i+1] )*\
##                   ( ycoords>=yedges[j] )*( ycoords<yedges[j+1] ) )
##             if np.sum( l )==0:
##                 continue
##             z_grid[j,i] = np.mean( zsignal[l] )
##     return x_grid, y_grid, z_grid, pt_densities, extent

## def bin_2d( xcoords, ycoords, zsignal, nx=30, ny=30 ):
##     """
##     Bin a 2D data series.
##     """
##     pt_densities, yedges, xedges = np.histogram2d( ycoords, xcoords, bins=( ny, nx ) )
##     dx = np.median( np.diff( xedges ) )
##     dy = np.median( np.diff( yedges ) )
##     x = 0.5*dx + xedges[:-1]
##     y = 0.5*dy + yedges[:-1]
##     extent = [ xedges.min(), xedges.max(), yedges.min(), yedges.max() ]
##     grid = np.mgrid[ x[0]:x[-1]:nx*1j, y[0]:y[-1]:ny*1j ]
##     x_grid = grid[0]
##     y_grid = grid[1]
##     z_grid = np.zeros( [ ny, nx ] ) + np.nan
##     for i in range( nx ):
##         for j in range( ny ):
##             l = ( ( xcoords>=xedges[i] )*( xcoords<xedges[i+1] )*\
##                   ( ycoords>=yedges[j] )*( ycoords<yedges[j+1] ) )
##             if np.sum( l )==0:
##                 continue
##             z_grid[j,i] = np.mean( zsignal[l] )
##     return x_grid, y_grid, z_grid, pt_densities, extent
