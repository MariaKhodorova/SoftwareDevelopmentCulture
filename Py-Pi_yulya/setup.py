from setuptools import setup

import json
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def read_dependencies(fname):
    filepath = path.join(here, "mtracker", fname)
    with open(filepath) as piplock:
        content = json.load(piplock)
        return [dependency for dependency in content.get('default')]

setup(
   name='mtracker_yulya',
   version='1.1',
   description='Provides a decorator for memory usage tracking. The part of FOSS course.',
   long_description=long_description,
   long_description_content_type='text/markdown',
   license='MIT',
   author='Yulia Kravtsova',
   author_email='yuvwwa@gmail.com',
   url='https://github.com/MariaKhodorova/SoftwareDevelopmentCulture/tree/pypi_yulya/Py-Pi_yulya',
   packages=['mtracker'],
   install_requires=read_dependencies("Pipfile.lock"), # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)