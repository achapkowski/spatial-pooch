import sys
sys.path.insert(0, "C:\SVN\spatial-pooch")
import pytest
import unittest
import pandas as pd
from spatialpooch import _tabular, _vector

@unittest.skip
class TestTabularDataTests(unittest.TestCase):
    """tests the tabular data tests cases"""
    #----------------------------------------------------------------------
    def test_fetch_crime(self):
        """fetch the crime data"""
        assert isinstance(_tabular.fetch_crime_data(), 
                          pd.DataFrame)
    #----------------------------------------------------------------------
    def test_fetch_traffic(self):
        """fetch the traffic data"""
        assert isinstance(_tabular.fetch_traffic_data(), 
                          pd.DataFrame)
###########################################################################
class TestVectorData(unittest.TestCase):
    """tests the vector data tests cases"""
    #----------------------------------------------------------------------
    def test_fetch_crime_sedf(self):
        """fetch the crime data as sedf"""
        assert isinstance(_vector.fetch_beach_access_data(f='arcgis'), 
                          pd.DataFrame)
    #----------------------------------------------------------------------
    def test_fetch_crime_string(self):
        """fetch the crime data as string paths"""
        assert isinstance(_vector.fetch_beach_access_data(), list)
    

if __name__ == "__main__":
    unittest.main()