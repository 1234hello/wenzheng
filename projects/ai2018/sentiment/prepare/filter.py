#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# ==============================================================================
#          \file   filter.py
#        \author   chenghuige  
#          \date   2018-09-14 21:55:52.069104
#   \Description  
# ==============================================================================

  
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys 
import os

import gezi

def filter(x):
  return gezi.filter_quota(x).replace('\r', '\x01').replace('\n', '\x02').replace('<R>', '\x01').replace('<N>', '\x02').replace('\t', ' ')
