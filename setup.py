import os
from setuptools import setup, find_packages  # , findall

with open("readme.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

NAME = 'project'
VERSION = '0.0.0'

setup(
    name=NAME,
    version=VERSION,
    description='simple management of configs and paths within a project',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=[f'{NAME}.{p}' for p in find_packages(where=NAME)] + [NAME],
    package_data={},
    install_requires=[
        'python-dotenv',
        'pyyaml',
    ],
    include_package_data=True,
    python_requires='>=3.5.2',
    author="Jordan Miller",
    author_email="paradoxlabs@protonmail.com",
    url="https://github.com/propername/project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    # scripts=[f for f in findall(dir='pm3/bin') if f.endswith('.py')],
)
