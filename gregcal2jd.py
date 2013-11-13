import numpy as np
import pdb

def gregcal2jd( year, month, day, hour, minute, second ):
    """
    Takes a Gregorian proleptic date in Universal Time
    and returns the Julian Date.
    """

    # Get the number of full years elapsed since
    # the start date of the Julian Date, which
    # corresponds to 12UT on 24 Nov 4714BC:
    nyears = year - 1 + 4713. + 37.5/365.

    # Number of leap years before 4700BC:
    nleapdays = int( ( 4713 - 4700 )/4. )
    
    # Number of full centuries before the current
    # year that havve elapsed since 4700BC:
    ncenturies = int( ( year - 1 + 4700. )/100. )

    # Determine the century dates since 4700BC:
    centuries = np.arange( -4700, year, 100 )

    # Work out which of those century dates were
    # exactly divisible by 400:
    ixs = ( centuries%400==0 )
    ncenturies_div400 = len( centuries[ixs] )

    # Determine the number of leap years prior to
    # the current year according to the convention
    # of the Gregorian calendar:
    nleapdays += int( ( year - 1 + 4700 )/4. ) - ncenturies + ncenturies_div400

    # Check if the current year is a leap year:
    condition1 = ( year%4.==0 )
    condition2 = ( year%400==0 )
    if condition1*condition2:
        leapyear = True
    else:
        leapyear = False

    # Define the number of days per month, giving
    # February an extra year if it's a leap year:
    if leapyear==True:
        month_days = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    else:
        month_days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    # Calculate the number of full days elapsed
    # so far this year:
    ndays_thisyear = 0
    for i in range( month-1 ):
        ndays_thisyear += month_days[i]
    ndays_thisyear += day - 1

    # Add on the fractional day:
    ndays_thisyear += hour/24.
    ndays_thisyear += minute/60./24.
    ndays_thisyear += second/60./60./24.

    # Determine the JD:
    jd = 365*nyears + nleapdays + ndays_thisyear

    return jd
