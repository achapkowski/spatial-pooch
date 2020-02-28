import importlib

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
def fetch_crime_data():
    """
    Loads crime sample data as a Pandas' DataFrame
    """
    data = None
    if allowed_formats['pandas']:
        fname = _GOODBOY.fetch("tabular/Crime_Incidents_in_2014.csv")
        data = pd.read_csv(fname)
    return data    
#--------------------------------------------------------------------------
def fetch_traffic_data():
    """
    Loads traffic count sample data as a Pandas' DataFrame
    """
    data = None
    if allowed_formats['pandas']:
        fname = _GOODBOY.fetch("tabular/Traffic_Count_Data.csv")
        data = pd.read_csv(fname)
    return data