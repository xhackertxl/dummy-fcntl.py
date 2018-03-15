"""
setup.py
"""

from setuptools import setup, find_packages

setup(
    name='fcntl',
    version='1.0.0',
    description='Dummy fcntl module for Windows',
    author='unknown',
    license='Public domain',
    url='https://github.com/irtnog/dummy-fcntl.py',
    packages=find_packages('src/'),
    package_dir={'': 'src'},
)
