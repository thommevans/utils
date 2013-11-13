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
    filter_dir = str(filter_dir).replace('~',os.path.expanduser('~'))
    filter_file = str(filter_dir+'/'+filter_file).replace('//','/')
    array = np.loadtxt(filter_file)
    wav = array[:,0]
    transmission = array[:,1]
    return wav, transmission
