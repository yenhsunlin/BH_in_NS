"""
DM2NSBH - Neutron Star consumed by Black Hole

A python package calculating the fate of an old neutron star in the
presence of dark matter being captured inside it.

"""

from dm2nsbh.core.const import Const
from dm2nsbh.core.capture import (caprate_no,caprate,numx)
from dm2nsbh.core.criteria import star_consumed

__all__ = ['Const','caprate_no','caprate','numx','star_consumed']
