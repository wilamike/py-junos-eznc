import os
import sys

sys.path.insert(0,'lib')
from setuptools import setup, find_packages
from jnpr.eznc import VERSION

setup(
    name = "junos-eznc",
    version = VERSION,
    author = "Jeremy Schulman",
    author_email = "jschulman@juniper.net",
    description = ( "Making Junos automation via NETCONF 'easy'" ),
    license = "BSD-2",
    keywords = "Junos NETCONF networking automation",
    url = "http://www.github.com/jeremyschulman/py-junos-eznc",
    package_dir={'':'lib'},    
    packages=find_packages('lib'),
    install_requires=[
        "Paramiko",
        "netaddr".
        "lxml",
        "jinja2"
    ]
    dependency_links=[
        "git+https://github.com/Juniper/ncclient.git"
    ]
)
