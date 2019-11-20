# 1 Introduction
This repository contains qcpython package `nsbh` for determining an old nearby neutron star could be destroyed by the dark-matter-forming black hole inside it or not. See jupyter notebook `tutorial.ipynb` for quick usage. The method is based on J. Bramante *et al.*, Phys. Rev. D **89**, 015010 (2014) [arXiv:1310.3509 [hep-ph]]

# 2 Quick guide
## 2.1 Prerequistes
`nsbh` requires the following packages to be installed in advance:

- numpy
- scipy

Missing any of them will result in error.

## 2.2 Import the package
The core files are contained in the folder named `nsbh`, please put your jupyter notebook or python script together with `nsbh` folder in the same path.

Using jupyter notebook for instance, typing the following in the work cell:<br>

    from nsbh import *

and the package should be loaded on-the-fly. If the package cannot be found, please add the following the preamble

    import sys
    sys.path.append('./')

then load the package again.

## 2.3 Build-in functions
The dark matter (DM) capture rate and how many DM are captured after a peried can be calculated through `caprate` and `numx`.

To determine an old neutron star is destroyed by a DM-forming black hole is given by `star_consumed`. Detail usage please check `tutorial.ipynb`.
