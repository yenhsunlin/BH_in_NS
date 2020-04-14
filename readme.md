## 1 Introduction
This repository contains a python package `dm2nsbh` for determining whether an old nearby neutron star could be destroyed by the dark-matter-forming black hole inside it or not. See jupyter notebook `tutorial.ipynb` or `tutorial.py` for quick usage. The method is based on G.L. Lin and Y.H. Lin [arXiv:2004.05312 [hep-ph]] (2020) and J. Bramante *et al.*, *Phys. Rev. D* **89**, 015010 (2014) [arXiv:1310.3509 [hep-ph]]

## 2 Quick guide
### Prerequistes
`dm2nsbh` requires the following packages to be installed in advance:

- `numpy`
- `scipy`

Missing any of them will result in error. We recommend *Anaconda*.

### Tested enviroment

- python 3.7.6
- numpy 1.18.1
- scipy 1.4.1

### Import the package
The core files are contained in the folder named `dm2nsbh`, please put your jupyter notebook or python script together with `dm2nsbh` folder under the same path.

Using jupyter notebook for instance, typing the following in the work space:

    from dm2nsbh import *

and the package should be loaded on-the-fly. If the package cannot be found (not encountered usually), please add the following in the preamble

    import sys
    sys.path.append('./')

then load the package again.

### Build-in functions
The dark matter (DM) capture rate and how many DM are captured after a period can be calculated through `caprate` and `numx`.

To determine an old neutron star is destroyed by a DM-forming black hole is given by `star_consumed`. Detail usage please check `tutorial.ipynb`. The meaning of the return value by `star_consumed` is explained by `decision_tree.pdf` in the `doc` folder.


## 3 Known issues

### Input variable type
If incompatible `numpy.int` or `numpy.float` happens during the calculations, try convert these `numpy` type of variables into native python `float` or `int` using `float(*var*)` or `int(*var*)`.

### `root_scalar` error
Certain range of inputs will cause the function `star_consumed` crashing due to the values are not allowed by `root_scalar` in `scipy.optimize`. Please simply ignore such inputs. If you are using loop calcuation, a way out to avoid kernel breaking due to `ValueError` can be done by

    try:
        star_consumed(*inputs*)
    except ValueError:
        pass

## 4 IMPORTANT NOTES!
If you use any of the code, even snippets, in this repository for academic researches or publishing scientific articles, please do cite the following (BibTeX)

    @article{lin2020analysis,
        author = "Lin, Guey-Lin and Lin, Yen-Hsun",
        archivePrefix = "arXiv",
        eprint = "2004.05312",
        month = "4",
        primaryClass = "hep-ph",
        title = "Analysis on the black hole formations inside old neutron stars by
                    isospin-violating dark matter with self-interaction",
        year = "2020"
    }
 
as well as the address of this repository
 
    https://github.com/yenhsunlin/dm2nsbh/
    
 Thanks!

