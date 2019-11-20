# This file includes the auxiliary functions criteria.py

import numpy as np
from scipy.optimize import root_scalar

# Requring self-made constants.py
from .const import Const


# Finding the critical number for collapse, pack in a class
class CriticalNumber:
    """
    Finding the critical DM number for collaps, ref. Phys. Rev. D 89, 015010 (2014)
    """
    
    @staticmethod
    def dss(mx,nx,mphi,a):
        """
        Finding the critical number for collapse in DSS phase
        """
        
        def virial_dss(y):
            # Eq. (22) of ref
            return -(3*np.pi**2)**(2/3)*mphi**2/(mx*y**2) +   \
                    (4*np.pi/3)**(1/3)*Const.G*nx**(2/3)*mx*  \
                    y**2*Const.RhoNS/mphi**2 +                \
                    8*a*mphi*np.exp(-y)*(1/y+1)
        
        def virial_dss_diff(y):
            # Diff of Eq. (22) wrt y
            return 2*2**(2/3)*(np.pi/3)**(1/3)*Const.G*Const.RhoNS*    \
                    y*mx*nx**(2/3)/mphi**2 + 19.1416*mphi**2/(y**3*mx) \
                    - 8*a*np.exp(-y)*mphi/y**2 * 8*a*np.exp(-y)*       \
                    (1/y+1)*mphi
        
        def virial_dss_diff2(y):
            # 2nd-diff of Eq. (22) wrt y
            return 2*2**(2/3)*(np.pi/3)**(1/3)*Const.G*Const.RhoNS*  \
                    mx*nx**(2/3)/mphi**2 - 57.4247*mphi**2/(y**4*mx) \
                    + mphi*a*(16*np.exp(-y)*(1/y**3 + 1/y**2) + 8*   \
                    np.exp(-y)*(1/y)+1)
        
        # Use Newton-Raphson method to find does y exist?
        sol_y = root_scalar(virial_dss,fprime=virial_dss_diff,       \
                            fprime2=virial_dss_diff2,x0=100,         \
                            method='newton')
        return sol_y
    
    
    @staticmethod
    def nss(mx,mphi,a):
        """
        Finding the critical number for collapse in NSS phase
        """
        # Eq. (13) of ref, thermal radius
        R_th = lambda mx: 250*Const.cm2GeV/np.sqrt(mx)
        y = lambda nx: 1.6*mphi*R_th(mx)/(10**nx)**(1/3)
        
        def virial_nss(ncoll):
            # Eq. (23) of ref
            return (4*np.pi/3)**(1/3)*Const.G*(10**ncoll)**(2/3)*     \
                    Const.RhoNS*mx*y(ncoll)**2/mphi**2 +              \
                    (4*np.pi/3)**(1/3)*Const.G*(10**ncoll)**(2/3)*    \
                    mx**2*mphi/y(ncoll) + 8*a*mphi*np.exp(-y(ncoll))* \
                    (1/y(ncoll)+1)-3*Const.NSTemp*Const.K2GeV
        
        #def virial_nss_diff(ncoll):
        #    # Diff of Eq. (23) wrt Nx
        #    return 2*2**(2/3)*mphi*mx**2*Const.G*(np.pi/3)**(1/3)/    \
        #            (3*(10**ncoll)**(1/3)*y(ncoll)) + 2*2**(2/3)*mx*  \
        #            Const.G*(np.pi/3)**(1/3)*Const.RhoNS*y(ncoll)**2/ \
        #            (3*mphi**2*(10**ncoll)**(1/3))
        
        #def virial_nss_diff2(ncoll):
        #    # Diff of Eq. (23) wrt Nx
        #    return 2*2**(2/3)*mphi*mx**2*Const.G*(np.pi/3)**(1/3)/    \
        #            (9*(10**ncoll)**(4/3)*y(ncoll)) + 2*2**(2/3)*mx*  \
        #            Const.G*(np.pi/3)**(1/3)*Const.RhoNS*y(ncoll)**2  \
        #            /(9*mphi**2*(10**ncoll)**(4/3))
        
        # Use bisection method to find the exponent of the critical number, 10-base
        sol_ncrit = root_scalar(virial_nss,bracket=[20,36],x0=35,     \
                                method='bisect')
        return sol_ncrit


# Subroutines, pack in a class
class PhaseCheck:
    """
    Check if Nx surpasses the criteria for star consuming at different phases.
    """
    
    @staticmethod
    def dps(mx, nx, mphi, a):
        """
        DPS phase check
        """
        # Critical number for collapse in DPS phase
        Ncolldps = 1.1*1e61*a**-6*mphi**12*mx**-9
        
        # Decision tree determines the fate of NS in DPS phase
        if nx > Ncolldps:
            # Is the collapse triggered when DM is in degenerate state
            if Ncolldps > 8*1e35:
                # Will the black hole evaporate
                if Ncolldps > (3.4/mx)*1e36:
                    # no evaporation
                    return True,'Scenario (f)'
                else:
                    # will evaporate
                    return False,'Scenario (g)'
            else:
                # the required ncolldps does not satisfy in the degenerate state
                return PhaseCheck.nss(mx,nx,mphi,a)
        else:
            # Total number of DM is not enough to trigger Jeans instability
            return False,'Scenario (c)'
        
        
    @staticmethod
    def dss(mx,nx,mphi,a):
        """
        DSS phase check
        """
        lookup = np.linspace(28,43,601) #np.linspace(30,45,301)
        Ncolldss = 0  # initial value for Ncoll
        flag = 'ncoll_not_found'         # initial value for index j
        for nexp in lookup:
            y_sol = CriticalNumber.dss(mx,10**nexp,mphi,a)
            if y_sol.root < 1 or y_sol.converged == False:
                # determining Ncoll
                Ncolldss = 10**nexp
                j = 'ncoll_found'
                break
            else:
                pass
        
        # Decision tree determines the fate of NS in NSS phase
        if j == 'ncoll_not_found' or nx < Ncolldss:
            return False,'Scenario (b)'
        else:
            # Checking if DM is in degenerate state
            if Ncolldss > 8*1e35:
                # Does BH evaporate?
                if Ncolldss > (3.4/mx)*1e36:
                    # No, star consumed
                    return True,'Scenario (d)'
                else:
                    # Yes, BH evaporated
                    return False,'Scenario (e)'
            else:
                # Not in degenerate state
                return PhaseCheck.nss(mx,nx,mphi,a)
                      
        
    @staticmethod
    def nss(mx,nx,mphi,a):
        """
        NSS phase check
        """
        # Find the critical number for collapse in NSS phase
        ncollexp = CriticalNumber.nss(mx,mphi,a)
        if ncollexp.converged == False:
            Ncollnss = 1e100
        else:
            Ncollnss = 10**(ncollexp.root)
        
        # Decision tree determines the fate of NS in NSS phase
        # Can collapse continue when DM becomes relativistic?
        if nx > Ncollnss and Ncollnss < 8*1e35:
            # Checking the screened phase of 2nd collapse
            if 2*1e4*mphi/np.sqrt(mx) < 1:
                # partly screened
                # Can the 2nd collapse continue?
                if a > 1.6*1e4*mphi**2/np.sqrt(mx**3):
                    # Will the BH evaporate?
                    if Ncollnss > (3.4/mx)*1e36:
                        # no evaporation
                        return True,'Scenario (m)'
                    else:
                        return False,'Scenario (n)'
                else:
                    return False,'Scenario (j)'
            else:
                # strongly screened
                # Can the 2nd collapse continue?
                if a > 2.4*1e-9*np.exp(2.1*1e4*mphi/np.sqrt(mx))/  \
                   (mphi/(1+4.7*1e-5*(1/mphi)*np.sqrt(mx))):
                    # Will the BH evaporate
                    if Ncollnss > (3.4/mx)*1e36:
                        # no evaporation
                        return True, 'Scenario (k)'
                    else:
                        return False, 'Scenario (l)'
                else:
                    return False,'Scenario (i)'
        else:
            # Collapse can't continue when DM becomes relativistic
            return False,'Scenario (h)'    