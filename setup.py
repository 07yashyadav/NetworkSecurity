'''
the setup file is an essential part of packaging and distributing a Python project.
it is used by setuptools to define configuration of your
project ,such as its metadata,dependencies and more
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''this function will return the list of requirements
    '''
    requirements_lst:List[str] = []
    try:
        with open('requirements.txt','r') as files:
           # read files from file
           lines = files.readlines()
           #process each line
           for line in lines:
               requirements = line.strip()
               # ignore empty lines and -e
               if requirements and requirements!="-e .":
                   requirements_lst.append(requirements)
    except Exception as e:
        print(f"Error reading requirements.txt: {e}")
    return requirements_lst

print(get_requirements())       

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author="Yash",
    author_email="yashthibgoan@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() 
) 