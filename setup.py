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

# if match:
#     version = match.group(1)
# else:
#     raise RuntimeError(
#         'Unable to find the version in {0}'.format(VERSION_FILE))