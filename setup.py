#!/usr/bin/env python
from setuptools import setup, find_packages

version = __import__('s3_link').__version__

setup(
    name="s3_link",
    version=version,
    author="Hannes Ljungberg",
    author_email="hannes@5monkeys.se",
    zip_safe=False,
    license="WTFPL",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "boto==2.17.0",
    ],
    entry_points="""
    [console_scripts]
    s3-link=s3_link.generate:main
    """
)
