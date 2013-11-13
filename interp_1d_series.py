import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate


def interp_1d_series( x_coarse, y_coarse, x_fine ):
    """
    Takes a coarsely sampled xy series, and interpolates
    the y values to a finer sampling specified by a finer
    x series. Returns the finely interpolated y series.
    """
    interp_func = scipy.interpolate.interp1d(x_coarse, y_coarse)
    y_fine = interp_func(x_fine)
    return y_fine
