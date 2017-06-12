import numpy as np
import pdb
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker

def correlation_plot(vectors, labels=None, figno=1, nbins_hist=50, showcolorbar=True, label_fontsize=12 ):
    """
    Plots correlations between variables.
    INPUT:
      vectors - NxM array where N is the number of data
      points and M is the number of variables.
    OUTPUT:
      Produces the plot and returns a matrix containing
      the correlation coefficients.
    """
    fig = plt.figure(figno, figsize=(15,14))
    ndata = np.shape(vectors)[0]
    nsets = np.shape(vectors)[1]
    if ndata>1000:
        random_subset = np.random.randint(0,high=ndata,size=1000)
    else:
        random_subset = np.arange( ndata )
    corrcoefs = np.empty([nsets,nsets])
    side_buffer = 0.15
    boxwidth = (1.-1.1*side_buffer)/nsets
    corr_cmap = matplotlib.cm.Reds
    corrcolormap = plt.cm.ScalarMappable(cmap=corr_cmap)
    corrcolormap.set_clim(vmin=0, vmax=1)
    for i in range(nsets):
        data1 = vectors[:,i]
	# Do the histogram along the diagonal:
        x_lowercorner = side_buffer+i*boxwidth
        y_lowercorner = side_buffer+nsets*boxwidth-(i+1)*boxwidth
        ax_x0 = plt.axes([x_lowercorner, y_lowercorner, boxwidth, boxwidth])
        ax_x0.xaxis.set_major_formatter(matplotlib.ticker.OldScalarFormatter())
        ax_x0.yaxis.set_major_formatter(matplotlib.ticker.OldScalarFormatter())
        plt.setp(ax_x0.xaxis.get_ticklabels(), visible = False)
        plt.setp(ax_x0.yaxis.get_ticklabels(), visible = False)
        plt.hist(data1, bins=nbins_hist)
        ax_x0.tick_params(axis='x', tick2On=False)
        ax_x0.tick_params(axis='y', size=0)        
        if ((labels!=None)*(i==0)):
            plt.ylabel(labels[i], fontsize=label_fontsize)
        if ((labels!=None)*(i==nsets-1)):
            plt.xlabel(labels[i], fontsize=label_fontsize)
	# Do the off-diagonal correlation plots:
        for j in range(i+1,nsets):
            data2 = vectors[:,j]
            # Check to see that both of the variables vary,
            # otherwise, it doesn't make sense to talk about
            # a correlation between them:
            if ((data1.min()!=data1.max())*(data2.min()!=data2.max())):
    	        correlation = np.corrcoef(data1,data2)[0,1]
            else:
                correlation = 0
            corrcoefs[i,j] = correlation
            corrcoefs[j,i] = correlation
            # Define the plotting axes: 
            x_lowercorner = side_buffer+i*boxwidth
            y_lowercorner = side_buffer+nsets*boxwidth-(j+1)*boxwidth
	    # Get the color to indicate the magnitude of correlation:
            axisbg = corrcolormap.to_rgba(abs(correlation))
            ax = plt.axes([x_lowercorner, y_lowercorner, boxwidth, boxwidth], axisbg=axisbg, sharex=ax_x0)
            ax.xaxis.set_major_formatter(matplotlib.ticker.OldScalarFormatter())
            ax.yaxis.set_major_formatter(matplotlib.ticker.OldScalarFormatter())
            ax.tick_params( labelsize=20 )
            plt.setp(ax.xaxis.get_ticklabels(), visible = False)
            plt.setp(ax.yaxis.get_ticklabels(), visible = False)
            plt.plot(data1[random_subset],data2[random_subset],'.k')
            if ((labels!=None)*(i==0)):
                plt.ylabel(labels[j], fontsize=label_fontsize )
            if ((labels!=None)*(j==nsets-1)):
                plt.xlabel(labels[i], fontsize=label_fontsize)
    # Lastly, add a color bar:
    cb_width = 0.25*boxwidth
    cb_height = 0.30
    cb_axis = fig.add_axes([1-side_buffer, 0.5, cb_width, cb_height])
    cb_norm = matplotlib.colors.Normalize(vmin=0, vmax=1)
    cb = matplotlib.colorbar.ColorbarBase(cb_axis, cmap=corr_cmap, norm=cb_norm, orientation='vertical')
    cb.set_ticks([0.0,0.5,1.0])
    return corrcoefs

