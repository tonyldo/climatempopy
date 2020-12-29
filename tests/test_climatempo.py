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
        current_weather = await climatempo.get_current_weather()
    assert current_weather.id==city_id
    assert current_weather.data.humidity

@pytest.mark.asyncio
async def test_72_hours_forecast():
    with open('./tests/tests_properties.json') as json_file:
        properties = json.load(json_file)
    city_id=properties['city_id']
    async with ClientSession() as websession:
        climatempo = ClimaTempo(websession, properties['token'], city_id)
        forecas_72_hours = await climatempo.get_72_hours_forecast()
    assert forecas_72_hours.id==city_id
    assert forecas_72_hours.data[0].date

@pytest.mark.asyncio
async def test_15_days_forecast():
    with open('./tests/tests_properties.json') as json_file:
        properties = json.load(json_file)
    city_id=properties['city_id']
    async with ClientSession() as websession:
        climatempo = ClimaTempo(websession, properties['token'],locale_id=city_id)
        forecas_15_days = await climatempo.get_15_days_forecast()
    assert forecas_15_days.data[0].date

@pytest.mark.asyncio
async def test_get_locales():
    with open('./tests/tests_properties.json') as json_file:
        properties = json.load(json_file)
    city_name=properties['city_name']
    state=properties['state_abreviation']
    country=properties['country_abreviation']
    async with ClientSession() as websession:
        climatempo = ClimaTempo(websession, properties['token'])
        locale = await climatempo.get_locales(city_name,state,country)
    assert len(locale)>0