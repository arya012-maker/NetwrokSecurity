from setuptools import setup, find_packages
from typing import List



def get_requirements() -> List[str]:
    """
    this function will always return a list of requirements
    """
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            lines =  file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")
    
    return requirement_lst

setup(
    name="My_Network_Security_Project",
    version="0.0.1",
    author="Aryamann",
    author_email="aryamann233@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)    