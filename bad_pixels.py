import numpy as np
import scipy
import scipy.ndimage

def zap( ecounts2d, nsig_cull_transient=8, nsig_cull_static=10, niter=1 ):
    """
    Routine for identifying static and transient bad pixels in a spectroscopic data cube. 

    Inputs:
    ecounts2d - NxMxK data cube where N is cross-dispersion, M is dispersion, K is frame number.
    nsig_cull_transient - threshold for flagging transient bad pixels.
    nsig_cull_static - threshold for flagging static bad pixels.
    niter - number of iterations to be used

    Outputs:
    ecounts2d_zapped - NxMxK cube containing the data with bad pixels corrected.
    transient_bad_pixs - NxMxK cube containing 1's for transient bad pixels and 0's otherwise
    static_bad_pixs - NxMxK cube containing 1's for static bad pixels and 0's otherwise
    ecounts2d_medfilt - NxMxK cube containing nominal PSF for each frame made using median filter
    """
    print '\n\nCleaning cosmic rays:'
    # Initialise arrays to hold all the outputs:
    ndisp, ncross, nframes = np.shape( ecounts2d )
    ecounts2d_zapped = np.zeros( [ ndisp, ncross, nframes ] ) # array for corrected data frames
    ecounts2d_medfilt = np.zeros( [ ndisp, ncross, nframes ] ) # array for median-filter frames
    transient_bad_pixs = np.zeros( [ ndisp, ncross, nframes ] ) # array for transient bad pixels
    static_bad_pixs = np.zeros( [ ndisp, ncross, nframes ] ) # array for static bad pixels
    # First apply a Gaussian filter to the pixel values
    # along the time axis of the data cube:
    ecounts2d_smoothed = scipy.ndimage.filters.gaussian_filter1d( ecounts2d, sigma=5, axis=2 )
    ecounts2d_smoothsub = ecounts2d - ecounts2d_smoothed # pixel deviations from smoothed time series
    med2d = np.median( ecounts2d_smoothsub, axis=2 )  # median deviation for each pixel
    stdv2d = np.std( ecounts2d_smoothsub, axis=2 ) # standard deviation in the deviations for each pixel
    # Loop over the data frames:
    for i in range( nframes ):
        ecounts2d_zapped[:,:,i] = ecounts2d[:,:,i]
        # Identify and replace transient bad pixels, possibly iterating more than once:
        for k in range( niter ):
            # Find the deviations of each pixel in the current frame in terms of 
            # number-of-sigma relative to the corresponding smoothed time series for
            # each pixel:
            ecounts2d_smoothsub = ecounts2d_zapped[:,:,i] - ecounts2d_smoothed[:,:,i]
            dsig_transient = np.abs( ( ecounts2d_smoothsub-med2d )/stdv2d )
            # Flag the outliers:
            ixs_transient = ( dsig_transient>nsig_cull_transient )
            # Create a median-filter frame by taking the median of 5 pixels along the
            # cross-dispersion axis for each pixel, to be used as a nominal PSF:
            medfilt_ik = scipy.ndimage.filters.median_filter( ecounts2d_zapped[:,:,i], size=[5,1] )
            # Interpolate any flagged pixels:
            ecounts2d_zapped[:,:,i][ixs_transient] = medfilt_ik[ixs_transient]
            # Record the pixels that were flagged in the transient bad pixel map:
            transient_bad_pixs[:,:,i][ixs_transient] = 1
        ntransient = transient_bad_pixs[:,:,i].sum() # number of transient bad pixels for current frame
        # Identify and replace static bad pixels, possibly iterating more than once:
        for k in range( niter ):
            # Create a median-filter frame by taking the median of 5 pixels along the
            # cross-dispersion axis for each pixel, to be used as a nominal PSF:
            medfilt_ik = scipy.ndimage.filters.median_filter( ecounts2d_zapped[:,:,i], size=[5,1] )
            # Find the deviations of each pixel in the current frame in terms of 
            # number-of-sigma relative to the nominal PSF:
            dcounts_static = ecounts2d_zapped[:,:,i] - medfilt_ik
            stdv_static = np.std( dcounts_static )
            dsig_static = np.abs( dcounts_static/stdv_static )
            # Flag the outliers:
            ixs_static = ( dsig_static>nsig_cull_static )
            # Interpolate any flagged pixels:
            ecounts2d_zapped[:,:,i][ixs_static] = medfilt_ik[ixs_static]
            # Record the pixels that were flagged in the static bad pixel map:
            static_bad_pixs[:,:,i][ixs_static] = 1
        nstatic = static_bad_pixs[:,:,i].sum() # number of transient bad pixels for current frame
        ecounts2d_medfilt[:,:,i] = medfilt_ik # record the nominal PSF for the current frame
        print '... frame {0} of {1}: ntransient={2}, nstatic={3}'.format( i+1, nframes, ntransient, nstatic )
    return ecounts2d_zapped, transient_bad_pixs, static_bad_pixs, ecounts2d_medfilt

