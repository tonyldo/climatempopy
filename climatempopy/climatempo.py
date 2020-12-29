from .const import *
from types import SimpleNamespace
import json

class ClimaTempo:    

    def __init__(self, session, climatempo_token, locale_id=None):
        self.session = session
        self.climatempo_token = climatempo_token
        self.locale_id = locale_id
        self.current = None
        self.forecast_72_hours= None
        self.forecast_15_days_georeferenced= None

    async def get_current_weather(self):
        url = API_URL+CURRENT_WEATHER_URL.format(self.locale_id)
        return await self.get_object_data(url)

    async def get_72_hours_forecast(self):
        url = API_URL+FORECAST_72_HOURS_URL.format(self.locale_id)
        return await self.get_object_data(url)

    async def get_15_days_forecast(self):
        url = API_URL+FORECAST_15_DAYS_URL.format(self.locale_id)
        return await self.get_object_data(url)

    async def get_locales(self,city,state=None,country=None):
        url = API_URL+SEARCH_LOCALE_URL.format(self.locale_id)
        params = {}
        params["name"]=city
        if state:
            params["state"]=state
        if country:
            params["country"]=country
        return await self.get_object_data(url,params)

    async def get_object_data(self, url, params=None):
        current = await self.async_http_request(url,params)
        return self.json_to_object(current) 

    def json_to_object(self, data):
        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

    async def async_http_request(self, url, params=None):
        if not params:
            params = {}
        params[TOKEN_PARAMETER_STR]=self.climatempo_token
        async with self.session.get(url, params=params) as res:
            res.raise_for_status()
            current = await res.text()
        return current
    
    async def update_current_weather(self):
        self.current = await self.get_current_weather()

    async def update_72_hours_forecast (self):
        self.forecast_72_hours = await self.get_72_hours_forecast()
    
    async def update_15_days_forecast (self):
        self.forecast_15_days_georeferenced = await self.get_15_days_forecast_georeferenced()