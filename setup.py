from xml.etree.ElementTree import VERSION
from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup functions
PROJECT_NAME="censusip"
VERSION="0.0.1"
AUTHOR="Arpit Dubey"
DESCRIPTION="This is internship Project for FSDS Nov batch Machine Learning Project."
# PACKAGES=["censusip"]
LICENCE = "Apache License"
# PLATFORM = "Github, Docker, Heroku"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file

    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    # packages=PACKAGES,
    packages=find_packages(),
    licence = LICENCE,
    # Platform=PLATFORM,
    install_requires=get_requirements_list()
)