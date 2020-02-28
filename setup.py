"""
Build and install the project.

Uses versioneer to manage version numbers using git tags.
"""
import os
from setuptools import setup, find_packages



NAME = "spatialpooch"
FULLNAME = "Spatial-Pooch"
AUTHOR = "Andrew Chapkowski"
AUTHOR_EMAIL = "achapko1 (at) jh.edu"
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
LICENSE = "Apache 2.0"
URL = "https://github.com/achapkowski/spatial-pooch"
DESCRIPTION = (
    "Spatial-Pooch manages your Spatial library's sample data files: "
    "it automatically downloads and stores them in a local directory, "
    "with support for versioning and corruption checks."
)
KEYWORDS = ""
with open("README.md") as f:
    LONG_DESCRIPTION = "".join(f.readlines())

VERSION = "1"
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Scientific/Engineering",
    "Topic :: Software Development :: Libraries",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3 :: Only",
    "License :: OSI Approved :: {}".format(LICENSE),
]
PLATFORMS = "Any"
PACKAGES = find_packages(exclude=["doc", "data"])
SCRIPTS = []
PACKAGE_DATA = {
    "spatialpooch": [
        "spatialpooch", "registery.txt"
    ]
}
INSTALL_REQUIRES = ["pandas", "arcgis>=1.7.1", "pooch>=1.0.0"]
PYTHON_REQUIRES = ">=3.5"

if __name__ == "__main__":
    setup(
        name=NAME,
        fullname=FULLNAME,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        version=VERSION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        license=LICENSE,
        url=URL,
        platforms=PLATFORMS,
        scripts=SCRIPTS,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        classifiers=CLASSIFIERS,
        keywords=KEYWORDS,
        install_requires=INSTALL_REQUIRES,
        python_requires=PYTHON_REQUIRES
    )