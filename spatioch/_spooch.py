"""
Module mypackage/datasets.py
"""
import pkg_resources
import pandas
import pooch

# Get the version string from your project. You have one of these, right?
from . import version


# Create a new friend to manage your sample data storage
SPATIALPOOCH = pooch.create(
    # Folder where the data will be stored. For a sensible default, use the
    # default cache folder for your OS.
    path=pooch.os_cache("spatial-pooch"),
    # Base URL of the remote data store. Will call .format on this string
    # to insert the version (see below).
    base_url="https://github.com/achapkowski/spatial-pooch/raw/{version}/data/",
    version=version.version,
    version_dev="master",
    # An environment variable that overwrites the path.
    env="SPATIODATA"
)
# You can also load the registry from a file. Each line contains a file
# name and it's sha256 hash separated by a space. This makes it easier to
# manage large numbers of data files. The registry file should be packaged
# and distributed with your software.
SPATIALPOOCH.load_registry(
    pkg_resources.resource_stream("spatioch", "registry.txt")
)


# Define functions that your users can call to get back the data in memory
def fetch_crime_data():
    """
    Loads crime sample data as a Pandas' DataFrame
    """
    # Fetch the path to a file in the local storage. If it's not there,
    # we'll download it.
    fname = SPATIALPOOCH.fetch("tabular/Crime_Incidents_in_2014.csv")
    # Load it with numpy/pandas/etc
    data = pandas.read_csv(fname)
    return data

def fetch_traffic_data():
    """
    Loads traffic count sample data as a Pandas' DataFrame
    """
    # Fetch the path to a file in the local storage. If it's not there,
    # we'll download it.
    fname = SPATIALPOOCH.fetch("tabular/Traffic_Count_Data.csv")
    # Load it with numpy/pandas/etc
    data = pandas.read_csv(fname)
    return data

