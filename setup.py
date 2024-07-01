from setuptools import find_packages,setup
from typing import List

HYPYON_E_DOT = "-e ."


def get_requirements(filepath:str) -> List[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ i.replace("\n","") for i in requirements]

        if HYPYON_E_DOT in requirements:
            requirements.remove(HYPYON_E_DOT)



setup(name='ML_Pipeline_Project',
      version='0.0.1',
      description='Machine Learning Pipeline Project',
      author='Shahbaz Faqir',
      author_email='shahbaz.h000pm@gmail.com',
      install_requires= get_requirements("requirements.txt")
     )