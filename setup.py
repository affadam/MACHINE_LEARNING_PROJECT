from setuptools import setup,find_packages # find_package - Return all the module wherever __init__.py resides (wherver __init__.py is there it is called as package)
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
        return requirement_file.readlines() #purpose of removing as doing the same job as find_package since we dont need it in setup.py
    

setup(
    name = PROJECT_NAME,
    version = VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    #packages=PACKAGES,
    packages=find_packages(), #alternate - ["housing"] # find_package - Return all the module wherever __init__.py resides (wherver __init__.py is there it is called as package)
    install_requires = get_requirements_list()
)

if __name__ == "__main__":
    print(get_requirements_list())