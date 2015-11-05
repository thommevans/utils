import numpy as np
import pdb, warnings

def bin_1d( x, y, nbins=10, shift_left=0.0, shift_right=0.0 ):
    """
    shift_left and shift_right are optional arguments that allow you to shift the
    bins either to the left or right by a specified fraction of a bin width.
    """

    x = x.flatten()
    y = y.flatten()
    if len( x )!=len( y ):
        raise ValueError( 'vector dimensions do not match' )
    
    binw = (x.max()-x.min())/float(nbins)
    if nbins>1:
        # Have half-bin overlap at start:
        wmin = x.min()-binw-binw*shift_left+binw*shift_right
    elif nbins==1:
        wmin = x.min()
    else:
        pdb.set_trace()
    wmax = x.max()
    wrange = wmax - wmin
    if nbins>1:
        xbin = list(np.r_[wmin+binw/2.:wmax-binw/2.:nbins*1j])
    elif nbins==1:
        xbin = [wmin+0.5*wrange]
    else:
        pdb.set_trace()
    ybin = list(np.zeros(nbins))
    ybinstdvs = np.zeros(nbins)
    nperbin = np.zeros(nbins)
    for j in range(nbins):
        l = (abs(x - xbin[j]) <= binw/2.)
        if l.any():
            nperbin[j] = len(y[l])
            ybin[j] = np.mean(y[l])
            ybinstdvs[j] = np.std(y[l])

    return np.array(xbin), np.array(ybin), np.array(ybinstdvs), np.array(nperbin)
