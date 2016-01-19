import numpy as np

def logp_mvnormal_white( y, sig ):
    """
    Returns the log likelihood of data y with associated
    uncertainties sig assuming random draw from multivariate
    Gaussian distribution with diagonal covariance matrix.
    """
    n = len( y )
    term1 = -0.5*n*np.log( 2*np.pi )
    term2 = -np.sum( np.log( sig ) )
    term3 = -0.5*np.sum( (y/sig)**2. )
    return term1+term2+term3
