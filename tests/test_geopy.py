from geopy.geocoders import Nominatim

aracaju_coords = "-10.981982, -37.053425"
user_agent_str = "climatempopy-test"

def test_geopy():
    geolocator = Nominatim(user_agent=user_agent_str)
    location = geolocator.reverse(aracaju_coords)
    assert location.raw['address']['city']=='Aracaju'
    assert location.raw['address']['state']=='Sergipe'
    assert location.raw['address']['suburb'] =='Atalaia'


