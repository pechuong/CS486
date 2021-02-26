import pytest
import requests

from pytest_bdd import scenarios, given, when, then

MONSTERS_API = 'https://www.dnd5eapi.co/api/monsters/'

scenarios('../features/dnd_monsters.feature', example_converters=dict(monster=str, hp=int))

@pytest.fixture
@when('the DnD API is queried with "<monster>"')
def monster_response(monster):
    params = {'format': 'json'}
    response = requests.get(MONSTERS_API + monster, params=params)
    return response

@then('the response status code is 200')
def monster_response_code(monster_response):
    assert monster_response.status_code == 200

@then('the response shows hit_points of "<hp>"')
def monster_response_hit_points(monster_response, hp):
    assert monster_response.json()['hit_points'] == hp