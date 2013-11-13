import numpy as np
import pdb

def autocorrelation( x, maxlag=None ):
    n = len( x.flatten() )
    if maxlag==None:
        maxlag = min( [ n, 1000 ] )
    denom = np.sum( chain_i**2. )
    numer = np.correlate( chain_i, chain_i, mode='full' )[n-1:][:maxlag+1]
    return numer/denom
