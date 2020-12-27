#!/usr/bin/env python

import sys
import json
from climatempopy import simple_climatempopy


'''
To call this script:
$ pip3 install climatempopy
$ get_current_weather YOUR_CLIMATEMPO_TOKEN LAT LON 
'''

your_climatempo_token = str(sys.argv[1])
lat = str(sys.argv[2])
lon = str(sys.argv[3])

