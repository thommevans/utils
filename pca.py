import numpy as np
import matplotlib.pyplot as plt


# probably better to set scikit-learn up for doing all this

def eig( A ):
    if type(M)!=np.ndarray:
        M = np.array( M )
    M = ( A - np.mean( A, axis=1 ) ).T
    [ latent, coeff ] = np.linalg.eig( np.cov( M ) )
    score = np.dot( coeff.T, M )
    return coeff, score, latent

def svd( A ):
    print 'To do!'

    return None
