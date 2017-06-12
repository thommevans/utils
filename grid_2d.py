from __future__ import print_function
import os, pdb, sys
import numpy as np


def grid_2d( data2d, requested_bin_spacing, npts_min ):
    """
    The same as the fit_1d_grid function, except for 2D data.
    
    Hence, the data is binned on a 2D grid, and the 2D coordinates
    of the bin centers are returned.

    Be aware that if you're dividing up a 2D plane spanned by
    two variables with different units, it's probably a good idea
    to standardise both sets of input variables before passing them
    in here. For example, if you're using this routine to find
    the centers of 2D Gaussian basis functions, I currently have
    the code set up to only work for orthogonal 2D Gaussians
    (i.e. diagonal covariance matrices), so the basis width will
    need to be suitable for both input variables. Standardising
    both input variables would hopefully help to ensure this.
    Note that the standardised input variables would also need to
    be used in constructing the 2D Gaussian basis functions in that
    case.
    """
    print( 'NEED TO DOUBLE CHECK THIS IS DOING THE CORRECT THING: \n \
            previously the way i had it set up with vbr_script it was \n \
            not setting the basis widths properly!!!!!' )
    # Get the range of data along the first axis:
    data_x = data2d[:,0]
    lower_x = data_x.min()
    upper_x = data_x.max()
    # Get the range of data along the second axis:
    data_y = data2d[:,1]
    lower_y = data_y.min()
    upper_y = data_y.max()
    # Work out the number of bins we need if they're going
    # be spaced as close as possible to the requested spacing:
    nbins_x = np.ceil( ( upper_x-lower_x ) / float( requested_bin_spacing ) )
    nbins_y = np.ceil( ( upper_y-lower_y ) / float( requested_bin_spacing ) )
    # Compute the histogram:
    histogram, bin_x_edges, bin_y_edges = np.histogram2d( data_x, data_y, bins=( nbins_x, nbins_y ) )
    # NOTE: The values in the histogram array will be such that the  x-axis is by default along
    # the 1st dimension (i.e. rows, increasing downwards), and the y-axis is by default along
    # the 2nd dimension (i.e. columns, increasing rightwards).
    # Strip the un-needed last entries of the bin_x_edges and bin_y_edges arrays:
    bin_x_edges = bin_x_edges[:-1]
    bin_y_edges = bin_y_edges[:-1]
    # Calculate the bin widths:
    bin_x_widths = bin_x_edges[1]-bin_x_edges[0]
    bin_y_widths = bin_y_edges[1]-bin_y_edges[0]    
    # Work out which bins contain the minimum number of points:
    ixs = ( histogram >= npts_min )
    histogram = histogram[ixs]
    # Convert the bin_edges arrays into bin_edges mesh grids:
    bin_x_mesh, bin_y_mesh = np.meshgrid( bin_x_edges, bin_y_edges )
    # Before extracting the relevant entries, we need to put the meshgrids into the same format
    # the histogram entries (see above):
    bin_x_edges = bin_x_mesh.T[ixs]
    bin_y_edges = bin_y_mesh.T[ixs]
    # Calculate the bin centers:
    nbins = len( histogram )
    bin_centers = np.empty( [ nbins, 2 ] )
    for i in range( nbins ):
        bin_centers[i,0] = bin_x_edges[i] + 0.5*bin_x_widths
        bin_centers[i,1] = bin_y_edges[i] + 0.5*bin_y_widths
    return bin_centers, bin_x_widths, bin_y_widths
