import numpy as np
import pdb

"""
A module that contains some simple routines for
converting between the different units/formats
used for expressing right ascension and declination
coordinates.
"""

def add_colons( arr ):

    string = ''
    for i in arr:
        string += '{0}:'.format( i )
    string = string[:-1]

    return string

def strip_colons( string ):

    arr = []
    counter = 0
    n = len( string )
    while counter<n:
        ix = string.find( ':' )
        if ix>=0:
            arr += [ string[:ix] ]
            string = string[ix+1:]
            counter += len( arr[-1] ) + 1
        else:
            arr += [ string ]
            counter = n

    arr[0] = int( arr[0] )
    arr[1] = int( arr[1] )
    arr[2] = float( arr[2] )

    return arr

def hhmmss2decideg( hrs, mins, secs ):
    """
    Takes a right ascension value in units of
    hours and converts to degrees in decimal
    format. Output is a float with units of
    decimal degrees.
    """

    degs_deci = hrs*15. + mins*15./60. + secs*15./60./60.

    return degs_deci

def hhmmss2ddmmss( hrs, mins, secs ):
    """
    Takes a right ascension value in units of
    hours and converts to degrees in sexagesimal
    format. Output is a tuple of the form:
        [ degrees, minutes, seconds ]
    """

    degs_deci = hhmmss2decideg( hrs, mins, secs )
    degs_sexa = decideg2sexag( degs_deci )

    return degs_sexa

def sexag2decideg( degs, mins, secs ):

    degs_deci = degs + mins/60. + secs/60./60.

    return degs_deci

def sexag2hhmmss( degs, mins, secs ):
    """
    Given a sexagesimal value, converts to the
    RA units of hhmmss.
    """

    degs_deci = sexag2decideg( degs, mins, secs )

    hrs_deci = degs_deci/15.
    hrs = int( np.floor( hrs_deci ) )

    mins_deci = 60*( hrs_deci - hrs )
    mins = int( np.floor( mins_deci ) )

    secs = 60*( mins_deci - mins )
    
    return [ hrs, mins, secs ]

def decideg2sexag( deci ):
    """
    Provided a float in decimal format as input,
    this function converts the value to sexagesimal
    format and returns a tuple of the form:
        [ degrees, minutes, seconds ]
    """
    
    degs_deci = deci%360.
    degs = int( np.floor( degs_deci ) )

    if degs>0:
        mins_deci = 60*( degs_deci%degs )
    else:
        mins_deci = 60*degs_deci
    mins = int( np.floor( mins_deci ) )

    if mins>0:
        secs_deci = 60*( mins_deci%mins )
    else:
        secs_deci = 60*mins_deci
    secs = secs_deci

    return [ degs, mins, secs ]
    

def decideg2hhmmss( decideg ):

    degs, mins, secs = decideg2sexag( decideg )
    hrs, mins, secs = sexag2hhmmss( degs, mins, secs )

    return [ hrs, mins, secs ]

