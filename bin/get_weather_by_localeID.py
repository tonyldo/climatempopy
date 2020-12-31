#!/usr/bin/env python

import sys
from climatempopy import ClimaTempo
from aiohttp import ClientSession
import asyncio

'''
To call this script:
$ pip3 install climatempopy
$ get_weather_by_localeID YOUR_CLIMATEMPO_TOKEN LOCALE_ID 
'''

your_climatempo_token = str(sys.argv[1])
locale_id = str(sys.argv[2])

async def main():
    async with ClientSession() as session:
        climatempo = ClimaTempo(session, your_climatempo_token, locale_id)
        climatempo.update_current_weather()
        climatempo.update_72_hours_forecast()
        climatempo.update_15_days_forecast()
    print(climatempo.current)
    print(climatempo.forecast_72_hours)
    print(climatempo.forecast_15_days)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())