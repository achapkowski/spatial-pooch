import importlib
import pooch
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
def _fetch(data, f):
    """gets the data in the proper format"""
    data = _GOODBOY.fetch(fname=data, processor=pooch.processors.Unzip)
    if f is None:
        f = 'string'
    if str(f) == 'string':
        return data
    elif str(f) == 'arcgis' and allowed_formats['arcgis']:
        return pd.DataFrame.spatial.from_featureclass(data)
    else:
        return data
#--------------------------------------------------------------------------
def fetch_beach_access_data(f=None):
    """gets the data in the proper format"""
    return _fetch(dadta="vector/Public_Access_Information.zip", f=f)
#--------------------------------------------------------------------------
def fetch_shipping_lanes_data(f=None):
    """gets the data in the proper format"""
    return _fetch(dadta="vector/Shipping_Lanes.zip", f=f)
#--------------------------------------------------------------------------
def fetch_crime_data(f=None):
    """gets the data in the proper format"""
    return _fetch(dadta="vector/Crime.zip", f=f)
#--------------------------------------------------------------------------
def fetch_family_resource_centers_data(f=None):
    """gets the data in the proper format"""
    return _fetch(dadta="vector/Family_Resource_Centers.zip", f=f)

    