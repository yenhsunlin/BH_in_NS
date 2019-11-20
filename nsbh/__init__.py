"""
NSBH - Neutron Star consumed by Black Hole

A python package calculating the fate of an old neutron star in the
presence of dark matter being captured inside it.

"""

from nsbh.core.const import Const
from nsbh.core.capture import (caprate_no,caprate,numx)
from nsbh.core.criteria import star_consumed

__all__ = ['Const','caprate_no','caprate','numx','star_consumed']
