#!/usr/bin/env python3
from setuptools import setup

setup(
    name='land_ownership',
    version='1.0.0',
    description=(
        'A tool for retrieving land ownership relationships'
    ),
    author='D Bondars',
    author_email='dmitriy.bondars@gmail.com',
    packages=['database', 'land_commands'],
    entry_points={
        'console_scripts': [
            'data_feed = database.database:main',
            'landtree = land_commands.command:main'
        ]
    }
)