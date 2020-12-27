from .const import *

class ClimaTempo:    

    def __init__(self, session, climatempo_token, city_id):
        self.session = session
        self.climatempo_token = climatempo_token
        self.city_id = city_id
    
    async def get_json_current_weather(self):
        params = {}
        params[TOKEN_PARAMETER_STR]=self.climatempo_token
        url = API_URL+CURRENT_WEATHER_URL.format(self.city_id)
        async with self.session.get(url, params=params) as res:
            res.raise_for_status()
            current = await res.json()
        return current