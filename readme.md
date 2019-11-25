## Introduction
This repository contains a python package `nsbh` for determining whether an old nearby neutron star could be destroyed by the dark-matter-forming black hole inside it or not. See jupyter notebook `tutorial.ipynb` for quick usage. The method is based on J. Bramante *et al.*, *Phys. Rev. D* **89**, 015010 (2014) [arXiv:1310.3509 [hep-ph]]

## Quick guide
### Prerequistes
`nsbh` requires the following packages to be installed in advance:

- `numpy`
- `scipy`

Missing any of them will result in error.

### Import the package
The core files are contained in the folder named `nsbh`, please put your jupyter notebook or python script together with `nsbh` folder under the same path.

Using jupyter notebook for instance, typing the following in the work space:

    from nsbh import *

and the package should be loaded on-the-fly. If the package cannot be found, please add the following in the preamble

    import sys
    sys.path.append('./')

then load the package again.

### Build-in functions
The dark matter (DM) capture rate and how many DM are captured after a period can be calculated through `caprate` and `numx`.

To determine an old neutron star is destroyed by a DM-forming black hole is given by `star_consumed`. Detail usage please check `tutorial.ipynb`. The meaning of the return value by `star_consumed` is explained by `decision_tree.pdf` in the `doc` folder.

### Mathematica-dub
`nsbh` also provides a Mathematica-dub, see `mathematica-dub` folder. However, it will not subject to update and will be deprecated soon.

## Known issues

Certain range of inputs will cause the function `star_consumed` crashing due to the values are not allowed by `root_scalar` in `scipy.optimize`. Please simply ignore such inputs. If you are using loop calcuation, a way out to avoid kernel breaking due to `ValueError` can be done by

    try:
        star_consumed(*inputs*)
    except ValueError:
        pass

## IMPORTANT NOTES!
If you use any of the code, even snippets, in this repository for academic researches or publishing scientific articles, please ***DO*** cite the following (BibTeX)

    @article{Chen:2018ohx,
        author         = "Chen, Chian-Shu and Lin, Yen-Hsun",
        title          = "{Reheating neutron stars with the annihilation of
                            self-interacting dark matter}",
        journal        = "JHEP",
        volume         = "08",
        year           = "2018",
        pages          = "069",
        doi            = "10.1007/JHEP08(2018)069",
        eprint         = "1804.03409",
        archivePrefix  = "arXiv",
        primaryClass   = "hep-ph",
        SLACcitation   = "%%CITATION = ARXIV:1804.03409;%%"
    }
 
as well as the address of this repository
 
    https://github.com/yenhsunlin/nsbh/
    
 Thanks!

