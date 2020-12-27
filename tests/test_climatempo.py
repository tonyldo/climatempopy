from aiohttp import ClientSession
from climatempopy import ClimaTempo
import pytest
import json

@pytest.mark.asyncio
async def test_current_weather():
    with open('./tests/tests_properties.json') as json_file:
        properties = json.load(json_file)
    city_id=properties['city_id']
    async with ClientSession() as websession:
        climatempo = ClimaTempo(websession, properties['token'], city_id)
        current = await climatempo.get_json_current_weather()

    assert current['id']==city_id
    assert current['data']