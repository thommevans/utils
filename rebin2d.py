import numpy as np

def rebin2d( a, binning_factors ):
    """
    Resizes a 2D array by averaging. New dimensions must be
    integral factors of the original dimensions. This routine
    was inspired by the IDL rebin routine; however, currrently
    it only has the option to bin down the input array to a
    lower resolution - it does not interpolate to higher
    resolutions (although this wouldn't be hard to add).
 
    Inputs
    ------
    a : 2D array
    binning_factors : tuple of int giving resolution decreas
    for each axis.

 
    Output
    -------
    rebinned_array : 2D array with reduced resolution.
    """
    M, N = np.shape( a )
    m, n = binning_factors
    a = np.reshape( a, ( M/m, m, N/n, n ) )
    a = np.sum( np.sum( a, axis=3 ), axis=1 )/float( m*n )
    return a
