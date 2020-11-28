# -*- coding: utf-8 -*-

# ==============================================================================
# ██╗  ██╗██╗   ██╗███╗   ██╗████████╗ █████╗ 
# ╚██╗██╔╝██║   ██║████╗  ██║╚══██╔══╝██╔══██╗
#  ╚███╔╝ ██║   ██║██╔██╗ ██║   ██║   ███████║
#  ██╔██╗ ██║   ██║██║╚██╗██║   ██║   ██╔══██║
# ██╔╝ ██╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║
# ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝

# author: Xu Shen <xu.shen@awarehq.com>
# ==============================================================================



import re
from setuptools import setup, find_packages

VERSION_FILE = 'xunta/_version.py'
version_string = open(VERSION_FILE, 'rt').read()
version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
match = re.search(version_regex, version_string, re.M)

if match:
    version = match.group(1)
else:
    raise RuntimeError(
        'Unable to find the version in {0}'.format(VERSION_FILE))

setup(name='xunta',
      version=version,
      description='Package for search interesting people',
      author='Xu Shen',
      author_email='xu.shen@cornell.edu',
      license='Private',
      packages=find_packages(),
      install_requires=[
          'ftfy>=4.4.3',
          'pytest>=3.3.1',
          'gunicorn==19.8.1',
          'numpy>=1.17.4'
      ],
      zip_safe=False,
      include_package_data=True)