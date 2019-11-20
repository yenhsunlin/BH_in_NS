# Introduction
This repository contains qcpython package `nsbh` for determining an old nearby neutron star could be destroyed by the dark-matter-forming black hole inside it or not. See jupyter notebook `tutorial.ipynb` for quick usage. The method is based on J. Bramante *et al.*, Phys. Rev. D **89**, 015010 (2014) [arXiv:1310.3509 [hep-ph]]

# Quick guide
## Prerequistes
`nsbh` requires the following packages to be installed in advance:

- numpy
- scipy

## Import the package
The core files are contained in the folder named `nsbh`, please put your jupyter notebook or python script together with `nsbh` folder in the same path.

Using jupyter notebook for instance, typing the following in the work cell:<br>

    from nsbh import *

and the package should be loaded on-the-fly. If the package cannot be found, please add the following the preamble

    import sys
    sys.path.append('./')

and load the package again.


The reproduction of the exclusion plots of the upper and middle panels of Fig. 1 in C. Kouvaris, Phys. Rev. Lett. **108**, 191301 (2012) are given in the *results* folder. Including <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;\alpha=10^{-2}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\large&space;\alpha=10^{-2}" title="\large \alpha=10^{-2}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;10^{-5}" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\large&space;10^{-5}" title="\large 10^{-5}" /></a>. Beige color is excluded due to the star is consumed by the black hole.

Numerical data are given as well, arranged in <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\large&space;(m_\chi,m_\phi,{\rm&space;1/0})" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\inline&space;\large&space;(m_\chi,m_\phi,{\rm&space;1/0})" title="\large (m_\chi,m_\phi,{\rm 1/0})" /></a>. `1` means excluded (star consumed) and `0` allowed (not consumed).
