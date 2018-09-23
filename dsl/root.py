'''
Created on Dec 20, 2015

@author: xx
'''

import os

SRC_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_PATH = os.path.join(SRC_DIR, "output")
EXAMPLES_PATH = os.path.abspath(os.path.join(SRC_DIR, os.pardir))