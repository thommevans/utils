import numpy as np
import matplotlib.pyplot as plt
import pdb, os, sys


def parang( ha, dec, lat ):
    """
    SUMMARY
      Given an astronomical source at a particular hour
      angle being observed from a particular latitude,
      this routine calculates the parallactic angle.

    INPUTS
      ha - hour angle of source in decimal degrees
      dec - declination of angle in decimal degrees
      lat - latitude of observer in decimal degrees
            between +90 (north) and -90 (south)

    OUTPUTS
      pa - parallactic angle in decimal degrees

    NOTES
      
    """

    ha_rad = np.deg2rad( ha )
    dec_rad = np.deg2rad( dec )
    lat_rad = np.deg2rad( lat )

    x = -np.sin( ha_rad )
    y = +np.cos( dec_rad )*np.tan( lat_rad ) \
        -np.sin( dec_rad )*np.cos( ha_rad )
    pa_rad = -np.arctan2( x, y )
    pa_deg = np.rad2deg( pa_rad )

    return pa_deg
