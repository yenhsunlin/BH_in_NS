# This file includes the main function for determining
# is star consumed or not

# Requiring self-made auxfuncs.py
from .auxfuncs import PhaseCheck


# Main routine
def star_consumed(mx, nx, mphi, alpha):
    """
    Determining the whether NS is consumed by the DM-forming
    black hole or not.
    
    Parameters
    ----------
    mx : scalar
        DM mass in GeV
    nx : scalar
        Total number of DM being captured by the NS
    mphi : scalar
        Mediator mass in MeV
    alpha : scalar
        Dark fine structure constant
        
    Returns
    -------
    result : tuple
        First is a boolean value, True for consumed and False for not consumed
        Second is a string, that which scenario DM settled eventually
    """
    mphi2GeV = mphi/1000
    a = alpha
    
    # Checking the collapse can overcome the relativistical momentum eventually
    if a > 4.7*(mphi2GeV/mx)**2:
        # Checking the collapse start from which phase
        if a > mphi2GeV/mx:
            # degenerate strongly screened, dss
            return PhaseCheck.dss(mx,nx,mphi2GeV,a)
        else:
            # degenerate partly screened, dps
            return PhaseCheck.dps(mx,nx,mphi2GeV,a)
    else:
        return False,'Scenario (a)'