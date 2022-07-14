from xml.etree.ElementTree import VERSION
from setuptools import setup
from typing import List

# Declaring variables for setup functions
PROJECT_NAME="adult-census-ip"
VERSION="0.0.1"
AUTHOR="Arpit Dubey"
DESCRIPTION="This is internship Project for FSDS Nov batch Machine Learning Project."
PACKAGES=["censusip"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)