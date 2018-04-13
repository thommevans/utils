import numpy as np

def rescale_trspec( Rp1spec, pars1, pars2 ):
    """

    'Rp1spec' is the input transmission spectrum expressed
    as planet radius in metres.

    pars1 and pars2 contain the following properties:
      'Rbase' Baseline planet radius in metres
      'g' planet surface gravity in m/s2
      'T' atmosphere temperature in K
      'mu' mean molecular weight in kg

    """
    
    kboltz = 1.3806488e-23 # boltzmann constant in J K^-1

    Rbase1, g1, T1, mu1 = pars1
    Rbase2, g2, T2, mu2 = pars2
    
    H1 = ( kboltz*T1 )/( mu1*g1 )
    H2 = ( kboltz*T2 )/( mu2*g2 )

    z1 = ( Rp1spec-Rbase1 )/H1    
    z2 = H2*( z1 - 0.5*np.log( ( Rbase1*mu2*g2*T2 )/( Rbase2*mu1*g1*T1 ) ) )
    
    Rp2spec = Rbase2 + z2

    return Rp2spec
