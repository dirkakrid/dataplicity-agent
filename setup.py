#!/usr/bin/env python

from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Programming Language :: Python',
]

# http://bit.ly/2alyerp
with open('dpagent/_version.py') as f:
    exec(f.read())

with open('README.md') as f:
    long_desc = f.read()

setup(
    name='dpagent',
    version=__version__,
    description="Platform for connected devices",
    long_description=long_desc,
    author='WildFoundry',
    author_email='support@dataplicity.com',
    url='https://www.dataplicity.com',
    platforms=['any'],
    packages=find_packages(),
    classifiers=classifiers,

    entry_points={
        "console_scripts": [
           'dpagent = dpagent.app:main'
        ]
    },

    install_requires=[
        'websocket-client',
        'fs>=0.5.0',
        'enum34',
        'six',
    ]
)
