#!/usr/bin/env python
from distutils.core import setup

setup(name='treecorr_tools',
      version='0.1',
      scripts=['bin/pz_stack', 'bin/tomography'],
      install_requires=['numpy','fitsio']
      )
