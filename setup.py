import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "superlibrary",
    version = "0.0.4",
    author = "Noel Macatangay",
    author_email = "nmacatangay@gmail.com",
    description = ("Super Library for crunching data"),
    license = "TM License",
    keywords = "superlibrary trams",
    url = "http://ec2-52-1-68-63.compute-1.amazonaws.com/datascientists/superlibrary.git",
    install_requires=required,
    packages=['superlibrary', 'superlibrary/log', 'superlibrary/config', 'superlibrary/couchdb', 'superlibrary/dynamodb', 'superlibrary/parsing', 'superlibrary/postgresql', 'superlibrary/rabbit' , 'superlibrary/s3', 'superlibrary/sqs', 'superlibrary/time', 'superlibrary/csv', 'superlibrary/mysql', 'superlibrary/sql'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
