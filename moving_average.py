import numpy as np
import os, sys, pdb
import matplotlib.pyplot as plt

def mav( x, y, delx ):
    x = x[ np.argsort(x) ]
    yavg = np.zeros( len(x) )
    for i in range( len(x) ):
        ixs = ( ( x>x[i]-0.5*delx ) * ( x<x[i]+0.5*delx ) )
        yavg[i] = np.mean( y[ixs] )
    return yavg
