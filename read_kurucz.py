import numpy as np
import matplotlib.pyplot as plt
import os, sys, pdb

def stellar_spectrum( model_filepath='', teff=None, logg=None, new_grid=False ):

     # Row dimensions of the input file:
    if new_grid==False:
        nskip = 22 # number of lines to skip at start of file
        nhead = 1 # number of header lines for each grid point
        nwav = 1221 # number of wavelengths for each grid point
        ncol_per_row = 8 # number of columns per row for Hnu and Hnucont
        nchar_per_entry = 10 # number of characters per column for Hnu and Hnucont
    else:
        nskip = 0 # TODO
        nhead = 0 # TODO
        nwav = 0  # TODO
        pdb.set_trace() # TODO

    print '\nReading in the model grid...'
    ifile = open( model_filepath, 'rU' )
    ifile.seek( 0 )
    rows = ifile.readlines()
    ifile.close()
    rows = rows[nskip:]
    nrows = len( rows )
    print 'Done.'

    # Read in the wavelengths:
    wav_nm = np.zeros( nwav )
    nrow_wav = 0
    counter = 0
    while counter<nwav:
        z = rows[nrow_wav].split()
        n = len( z )
        wav_nm[counter:counter+n] = np.array( z, dtype=float )
        counter = counter+n
        nrow_wav += 1

    # Read in the teff, logg and vturb values
    # for each of the grid points:
    row_ixs = np.arange( nrows-nrow_wav )
    nrows_per_block = int( np.ceil( nwav/float( ncol_per_row ) ) )
    nlines = 2*nrows_per_block + nhead # one block for Hnu, one block for Hnucont
    header_ixs = row_ixs[ row_ixs%nlines==0 ]
    header_ixs += nrow_wav
    if new_grid==True:
        #header_ixs += 1
        #header_ixs = header_ixs[:-1]
        pdb.set_trace() # todo
    ngrid = len( header_ixs )
    teff_grid = np.zeros( ngrid )
    logg_grid = np.zeros( ngrid )
    for i in range( ngrid ):
        header = rows[header_ixs[i]].split()
        teff_grid[i] = float( header[1] )
        logg_grid[i] = header[3]

    # Identify the grid point of interest:
    logg_ixs = ( logg_grid==logg )
    teff_ixs = ( teff_grid==teff )

    # Extract the intensities at each of the wavelengths
    # as a function of wavelength:
    grid_ix = ( logg_ixs*teff_ixs )

    x = np.arange( ngrid )
    grid_n = int( x[grid_ix] )

    nstart = header_ixs[grid_n] + nhead
    Hnu = np.zeros( nwav )
    Hnucont = np.zeros( nwav )
    counter = 1
    for i in range( nrows_per_block ):
        Hnu_row = rows[nstart+i]
        Hnucont_row = rows[nstart+i+nrows_per_block]
        for j in range( ncol_per_row ):
            if counter>nwav:
                break
            else:
                ix0 = nchar_per_entry*j
                ix1 = nchar_per_entry*( j+1 )
                Hnu[i*ncol_per_row+j] = float( Hnu_row[ix0:ix1] )
                Hnucont[i*ncol_per_row+j] = float( Hnucont_row[ix0:ix1] )
                counter += 1

    clight = 2.99792458e10
    wav_cm = wav_nm*(1e-9)*(1e2)
    flux = 4.*Hnu*clight/wav_cm**2.

    return wav_nm, flux
