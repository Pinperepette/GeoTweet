#!/usr/bin/env python
#from distutils.core import setup
import re, uuid
from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
reqs = [str(req.req) for req in install_reqs]

setup(name="GeoTweet",
      version="0.1",
      description="Program to search tweets, tag, hashtag, user, with locations and maps",
      license="MIT",
      author="The pirate Group",
      author_email="NULL",
      url="https://github.com/Pinperepette/GeoTweet",
      install_requires=reqs,
      keywords="twitter geo",
      classifiers=[
          'Development Status :: 1 - Beta',
          'Topic :: Forensics :: Analysis :: Hacking :: Social Engineer',
          'License :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
      zip_safe=True)
