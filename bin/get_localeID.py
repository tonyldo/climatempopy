#!/usr/bin/env python

import sys
from climatempopy import ClimaTempo
from aiohttp import ClientSession
import asyncio

'''
To call this script:
$ pip3 install climatempopy
$ get_localeID YOUR_CLIMATEMPO_TOKEN LAT LON 
'''

your_climatempo_token = str(sys.argv[1])
lat = str(sys.argv[2])
lon = str(sys.argv[3])

async def main():
    async with ClientSession() as session:
        climatempo = ClimaTempo(session, your_climatempo_token)
        locale = climatempo.get_locale_from_coords(lat, lon)
    print(locale)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())