import os
import importlib

import pooch
from pooch import Unzip

from ._spooch import SPATIALPOOCH as _GOODBOY

###########################################################################
allowed_formats = {
    "pandas" : False,
    "numpy" : False,
    "string" : True,
    "sedf" : False
}
###########################################################################
if importlib.util.find_spec('numpy') is not None:
    import numpy as np
    allowed_formats['numpy'] = True
if importlib.util.find_spec('pandas') is not None:
    import pandas as pd
    allowed_formats['pandas'] = True
if importlib.util.find_spec('arcgis') is not None:
    from arcgis.features import GeoAccessor, GeoSeriesAccessor
    allowed_formats['arcgis'] = True
###########################################################################
#--------------------------------------------------------------------------
def _fetch(data, f, **kwargs):
    """gets the data in the proper format"""
    data = _GOODBOY.fetch(fname=data, processor=Unzip())
    if f is None:
        f = 'string'
    if str(f) == 'string':
        return data
    elif str(f) == 'arcgis' and allowed_formats['arcgis']:
        for f in data:
            if str(f).lower().endswith(".shp"):
                return pd.DataFrame.spatial.from_featureclass(f)
            elif str(f).lower().endswith('.gdb') and 'dataset' in kwargs:
                fc = os.path.join(f, kwargs['dataset'])
                return pd.DataFrame.spatial.from_featureclass(f)
    return data
#--------------------------------------------------------------------------
def fetch_beach_access_data(f=None):
    """gets the data in the proper format"""
    data = _fetch(data="vector/Public_Access_Information.zip", f=f)
    return data
#--------------------------------------------------------------------------
def fetch_shipping_lanes_data(f=None):
    """gets the data in the proper format"""
    return _fetch(data="vector/Shipping_Lanes.zip", f=f)
#--------------------------------------------------------------------------
def fetch_crime_shp_data(f=None):
    """gets the data in the proper format"""
    return _fetch(data="vector/Crime.zip", f=f)
#--------------------------------------------------------------------------
def fetch_family_resource_centers_data(f=None):
    """gets the data in the proper format"""
    return _fetch(data="vector/Family_Resource_Centers.zip", f=f)

    