#!/usr/bin/env python

import os
import sys

from setuptools import setup

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, 'mysum')

# When executing the setup.py, we need to be able to import ourselves, this
# means that we need to add the src/ directory to the sys.path.
sys.path.insert(0, src_dir)

setup()

