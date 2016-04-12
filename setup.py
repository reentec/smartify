#!/usr/bin/env python
from setuptools import setup

setup(
    name='smartify',
    packages=[
        'smartify',
    ],
    scripts=[
        'bin/smartify',
    ],
    version='0.1.0',
    description='smarthome',
    author='reentec',
    author_email='roger.tanner@me.com',
    url='https://github.com/reentec/smartify',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: SmartHome Enthusiasts',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: SmartHome',
    ],
)
