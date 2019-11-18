# This file includes how to calculate DM number in NS

import sys
sys.path.append('./')
import numpy as np
from scipy.interpolate import interp1d

# Requiring self-made constants.py
from constants import *


# Loading capture data
cap_dat = np.loadtxt("nscap.dat", delimiter=" ")
# Fitting capture rate data
# Taken from Fig. 1 of JCAP 05, 035 (2019)
cap_fit = interp1d(cap_dat[:,0],cap_dat[:,1])

def CaptureRateNoCorrection(mx, sigxn, rho=Const.LocalDM, vbar=Const.LocalVecDisp):
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
        
    Returns
    -------
    caprate : scalar
        Number of DM being captured by NS per second
    """
    cap_rate = 0.8*(5.072*1e72)*(rho/(mx*vbar))*np.minimum(1e-45,sigxn)*np.minimum(1,1.47548*mx/(1+mx))
    
    return cap_rate


def CaptureRate(mx, sigxn, rho=Const.LocalDM, vbar=Const.LocalVecDisp):
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
        
    Returns
    -------
    caprate : scalar
        Number of DM being captured by NS per second
    """
    if mx < 1e-6:
        raise ValueError('Input DM mass must larger than 1e-6 GeV')
    elif 1e-6 <= mx <= 10:
        return 10**cap_fit(np.log10(mx))*rho*(np.minimum(sigxn,1e-45)/1e-45)*(220/vbar)
    else:
        return CaptureRateNoCorrection(mx,sigxn,rho,vbar)


def Nx(age, mx, sigxn, rho=Const.LocalDM, vbar=Const.LocalVecDisp, tau=None):
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
        
    Returns
    -------
    DMnumber : scalar
        Total number of DM captured by the NS at certain age
    """
    if tau is None:
        return CaptureRate(mx,sigxn,rho,vbar)*age
    else:
        return CaptureRate(mx,sigxn,rho,vbar)*tau*(1 - np.exp(-age/tau))