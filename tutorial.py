import numpy as np
import matplotlib.pyplot as plt
from nsbh import *

# Basic properties of DM
age = 3e17     # NS age
mx = 0.5       # DM mass
sigxn = 1e-45  # DM-neutron cross section

# Calculating Nx vs mx
tau = 3.1e17  # DM lifetime, set to the age of the Universe
mx_ls = np.linspace(-3,2,50)
nx_ls = []
for mx in mx_ls:
    nx_ls.append(numx(age,10**mx,sigxn))

# Drawing Nx vs mx plot
plt.plot(10**mx_ls,nx_ls,label='Neutron')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('$m_\chi$ [GeV]')
plt.ylabel('$N_\chi$')
plt.show()

# Calculating Cc vs mx
mx_ls = np.linspace(-6,2,101)
cap_ls = []
# w/ full Pauli blocking
for m in mx_ls:
    cap_rate = caprate(10**m,sigxn)
    cap_ls.append(cap_rate)
# no full Pauli blocking correction
cap_no_pauli_ls = []
for m in mx_ls:
    cap_no_rate = caprate_no(10**m,sigxn)
    cap_no_pauli_ls.append(cap_no_rate)

# Drawing Cc vs mx plot
plt.plot(10**mx_ls,cap_no_pauli_ls,label='no full Pauli blocking')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('$m_\chi$ [GeV]')
plt.ylabel('$C_c$ [s$^{-1}$]')

plt.plot(10**mx_ls,cap_ls,label='full Pauli blocking')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('$m_\chi$ [GeV]')
plt.ylabel('$C_c$ [s$^{-1}$]')

plt.legend(loc='lower left')
plt.show()

# Test the function: star_consumed
# Basic DM properties
Mx = 10    # DM mass in GeV
Mphi = 10  # mediator mass in MeV
a = 1e-2   # dark fine-structure constant

consumed,_ = star_consumed(Mx,numx(age,Mx,sigxn),Mphi,a)
if consumed:
    print('Given DM mass is %.2f GeV, mediator mass %.2f MeV and a_x %.4f, the star is consumed by the DM-forming BH'%(Mx,Mphi,a))
else:
    print('Given DM mass is %.2f GeV, mediator mass %.2f MeV and a_x %.4f, the star is perfectly safe'%(Mx,Mphi,a))