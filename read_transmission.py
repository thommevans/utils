import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
import os
import pdb
import sys
import glob


def read_transmission(transmission_dir, transmission_file):
    """
    Reads in file for the transmission function of a passband.
    The file should have two columns, with the first giving the
    wavelengths (in microns) and the second giving the fractional
    transmission. Returns these two columns.
    """
    transmission_dir = str(transmission_dir).replace('~',os.path.expanduser('~'))
    transmission_file = str(transmission_dir+'/'+transmission_file).replace('//','/')
    array = np.loadtxt(transmission_file)
    wav = array[:,0]
    transmission = array[:,1]
    return wav, transmission
