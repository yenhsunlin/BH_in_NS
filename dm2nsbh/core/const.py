# This file includes the frequently used constants

class Const:
    """
    A class stores useful scientific constants
    """
    erg2GeV = 1/(1.602*1e-3)  # erg to NU, GeV
    K2GeV = 1/(1.161*1e13)    # Kelvin to NU, GeV
    g2GeV = 1/(1.783*1e-24)   # gram to NU, GeV
    cm2GeV = 1/(1.973*1e-14)  # cm to NU, GeV**-1;
    Vol2GeV = cm2GeV**-3      # cm**-3 to NU, GeV**3
    sec2GeV = 1/(6.529*1e25)  # second to NU, GeV**-1
    c = 2.998*1e8             # m/s
    MPl = 1.221*1e19          # Planck mass, GeV
    G = MPl**-2               # Gravitational constant in NU, GeV**-2
    NSTemp = 1e5              # NS temperature, K
    RhoNS = 0.00432376        # NS core density, GeV**4
    LocalDM = 0.3             # local DM number density, GeV/cm**3
    LocalVecDisp = 220        # local DM velocity dispersion, km/s