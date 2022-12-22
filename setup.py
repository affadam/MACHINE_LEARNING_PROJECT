from setuptools import setup
from typing import List,Dict,OrderedDict


#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Hariramanarayanan"
DESCRIPTION = "This is the first Machine learning project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]: # Calling requirements.txt
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()
    

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())