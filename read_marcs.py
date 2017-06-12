from __future__ import print_function
import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt
import os
import pdb
import sys
import glob


def read_marcs(teff=5000, logg=4.5, turbulence=2.0, metallicity=0.0):
    """
    Reads in MARCS spectrum of specified properties
    and returns two arrays, one containing the wavelengths
    and the other containing the relative fluxes at
    each wavelength.
    Fluxes are returned in units of erg/cm2/s/angstrom.
    Wavelengths are returned in units of microns.
    """
    print( '\nReading in MARCS spectrum:' )
    specdir = str('~/data/MARCS/').replace('~',os.path.expanduser('~'))
    # Read in the relative fluxes (units=):
    specfile = specdir+'p%04d_g%+4.1f_m0.0_t%02d_st_z%+5.2f' % (teff, logg, turbulence, metallicity)
    specfile = glob.glob(specfile.replace('//','/')+'*.flx')[0]
    flux = np.loadtxt(specfile)
    print( '  Relative fluxes from: %s' % specfile )
    # Read in the corresponding wavelengths (units=):
    wavfile = specdir+'wavelengths.vac'
    wav = np.loadtxt(wavfile)
    print( '  Wavelengths from: %s' % wavfile )
    # Convert the wavelengths from angstroms to microns:
    wav = wav/(1e4)
    # NOTE: The relative fluxes can be left in units of
    # 'per angstrom', because converting them to 'per micron'
    # or something similar is simply just multiplying
    # everything by a constant value.
    return wav, flux
