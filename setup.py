from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        for req in file_obj.readlines():
            req = req.strip()
            if req and not req.startswith("-e"):  # Remove '-e .' or any '-e' lines
                requirements.append(req)
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Mitali',
author_email='mitalighadigaonkar27@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)