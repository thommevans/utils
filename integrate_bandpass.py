import numpy as np
import matplotlib.pyplot as plt
import pdb

def integrate_bandpass(wav, flux, transmission):
    """
    Takes flux as a function of wavelength and integrates
    with a transmission function (i.e. for a bandpass).
    Note that there must be a one-to-one correspondence
    for the wav, flux and transmission series. If this
    is not already the case, it will be necessary to first
    interpolate using the interp_series() function.

    Integration is done using the built-in composite trapezoidal
    integration routine of numpy.
    """
    if ((len(wav)!=len(flux))*(len(wav)!=len(transmission))):
        pdb.set_trace()
    else:
        integ_flux = np.trapz(flux*transmission, x=wav)
    return integ_flux
