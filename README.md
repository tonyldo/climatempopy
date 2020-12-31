# ClimaTempoPy
## A Clima Tempo API Python Wrapper
### Retrieving Brazilian current weather and forecast prevision from Clima Tempo site.

1. Example
```
import sys
from climatempopy import ClimaTempo
from aiohttp import ClientSession
import asyncio

YOUR_CLIMA_TEMPO_TOKEN =''
LOCALE_ID = ''

async def main():
    async with ClientSession() as session:
        climatempo = ClimaTempo(session, YOUR_CLIMA_TEMPO_TOKEN , LOCALE_ID)
        climatempo.update_current_weather()
        climatempo.update_72_hours_forecast()
        climatempo.update_15_days_forecast()
    print(climatempo.current)
    print(climatempo.forecast_72_hours)
    print(climatempo.forecast_15_days)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

2. Scripts of this lib
```
To call this script:
$ pip3 install climatempopy
$ get_localeID YOUR_CLIMATEMPO_TOKEN LAT LON 
```