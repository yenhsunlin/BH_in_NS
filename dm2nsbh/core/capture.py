# This file includes how to calculate DM number in NS

import os
import numpy as np
from scipy.interpolate import interp1d

# Requiring self-made constants.py
from .const import Const


# Loading capture data
dat_path = os.path.dirname(os.path.abspath(__file__))
cap_dat = np.loadtxt(dat_path+'/nscap.dat', delimiter=" ")
# Fitting capture rate data
# Data obtained via private communication with the authors of JCAP 05, 035 (2019)
# neutron cap
n_fit = interp1d(cap_dat[:33,0],cap_dat[:33,1])
# proton cap
p_fit = interp1d(cap_dat[33:,0],cap_dat[33:,1])

def caprate_no(mx, sigxn, rho=Const.LocalDM, vbar=Const.LocalVecDisp, fnfp=1):
    """
    NS capture rate of DM without full degeneracy correction, # per seconds
    
    Parameters
    ----------
    mx : scalar or array-like
        DM mass in GeV
    sigxn : scalar
        DM-nucleon cross section in cm**2
    rho : scalar
        Local DM density in GeV/cm**3
    vbar : scalar
        Local DM velocity dispersion in km/s
    fnfp : scalar
        Isospin violation parameter fn/fp. Setting 1 equals
        isospin symmetry.
        
    Returns
    -------
    caprate : scalar
        Number of DM being captured by NS per second
    """
    cap_rate = 0.8*(5.072*1e72)*(rho/(mx*vbar))*(np.minimum(35e-45,sigxn) + \
            0.022*np.minimum(35e-45,sigxn*fnfp**-2))*np.minimum(1,1.47548*mx/(1+mx))
    
    return cap_rate


def caprate(mx, sigxn, rho=Const.LocalDM, vbar=Const.LocalVecDisp, fnfp=1):
    """
    NS capture rate of DM with full degeneracy correction, # per seconds
    
    Parameters
    ----------
    mx : scalar
        DM mass in GeV, must larger than 1e-6 GeV
    sigxn : scalar
        DM-nucleon cross section in cm**2
    rho : scalar
        Local DM density in GeV/cm**3
    vbar : scalar
        Local DM velocity dispersion in km/s
    fnfp : scalar
        Isospin violation parameter fn/fp. Setting 1 equals
        isospin symmetry.
        
    Returns
    -------
    caprate : scalar
        Number of DM being captured by NS per second
    """
    if mx<10:
        cap = 10**n_fit(np.log10(mx))*rho*(np.minimum(sigxn,1e-45)/1e-45)*(220/vbar) \
            + 10**p_fit(np.log10(mx))*rho*(np.minimum(sigxn*fnfp**-2,35e-45)/35e-45)*(220/vbar)
        return cap
    else:
        cap = caprate_no(mx,sigxn,rho,vbar,fnfp)
        return cap


def numx(age, mx, sigxn, rho=Const.LocalDM, vbar=Const.LocalVecDisp, tau=None, fnfp=1):
    """
    Total number of DM being captured in the NS at certain age.
    
    Parameters
    ----------
    age : scalar
        The age of the NS
    mx : scalar
        DM mass in GeV, must larger than 1e-6 GeV
    sigxn : scalar
        DM-nucleon cross section in cm**2
    rho : scalar
        Local DM density in GeV/cm**3
    vbar : scalar
        Local DM velocity dispersion in km/s
    tau : scalar
        The lifetime of DM, default is None, no decay
    fnfp : scalar
        Isospin violation parameter fn/fp. Setting 1 equals
        isospin symmetry.
        
    Returns
    -------
    DMnumber : scalar
        Total number of DM captured by the NS at certain age
    """
    if tau is None:
        return caprate(mx,sigxn,rho,vbar,fnfp)*age
    else:
        return caprate(mx,sigxn,rho,vbar,fnfp)*tau*(1 - np.exp(-age/tau))