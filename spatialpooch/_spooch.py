"""
Driver Module 
"""
import os
import pkg_resources
import pooch
import importlib

from . import version

__all__ = ["SPATIALPOOCH"]

SPATIALPOOCH = pooch.create(
    path=pooch.os_cache("spatial-pooch"),
    base_url="https://github.com/achapkowski/spatial-pooch/raw/master/data/",#{version} - use if I am going to version the data
    #version="",#version.version, - use if data versioning is needed 
    version_dev="master",
    env="SPATIODATA")
SPATIALPOOCH.load_registry(
    os.path.join(os.path.dirname(__file__), 'registery.txt')
)

