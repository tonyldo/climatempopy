from  climatempopy import common
import json

user_agent_str = "climatempopy-test"

def test_geopy():
    with open('./tests/tests_properties.json') as json_file:
        properties = json.load(json_file)
    location = common.get_address(user_agent_str,properties['aracaju_coords'])
    assert location.address.city=='Aracaju'
    assert location.address.state=='Sergipe'
    assert location.address.suburb =='Atalaia'

def test_get_state_abbreviation():
    assert common.get_state_abbreviation('Sergipe') == common.get_state_abbreviation('SERGIPE') 
    assert common.get_state_abbreviation('rondonia') == common.get_state_abbreviation('Rondônia')



