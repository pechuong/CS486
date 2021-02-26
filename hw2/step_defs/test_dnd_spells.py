import pytest
import requests

from pytest_bdd import scenarios, given, when, then

SPELLS_API = 'https://www.dnd5eapi.co/api/spells/'

scenarios('../features/dnd_spells.feature', example_converters=dict(spell=str, cast_time=str))


@pytest.fixture
@when('the DnD API is queried with "<spell>"')
def spell_response(spell):
    params = {'format': 'json'}
    response = requests.get(SPELLS_API + spell, params=params)
    return response


@then('the response status code is 200')
def spell_response_code(spell_response):
    assert spell_response.status_code == 200


@then('the response shows cast time of "<cast_time>"')
def spell_cast_time(spell_response, cast_time):
    assert spell_response.json()['casting_time'] == cast_time
