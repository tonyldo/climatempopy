from geopy.geocoders import Nominatim
import json

user_agent_str = "climatempopy-test"

def test_geopy():
    geolocator = Nominatim(user_agent=user_agent_str)
    with open('./tests/tests_properties.json') as json_file:
        properties = json.load(json_file)
    coords=properties['aracaju_coords']
    location = geolocator.reverse(coords)
    assert location.raw['address']['city']=='Aracaju'
    assert location.raw['address']['state']=='Sergipe'
    assert location.raw['address']['suburb'] =='Atalaia'


