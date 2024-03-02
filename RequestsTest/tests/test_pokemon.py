import requests
import pytest

HOST = 'https://api.pokemonbattle.me/v2'

def test_status_code():
    response = requests.get(url=f'{HOST}/trainers', params={'trainer_id': 135})
    assert response.status_code == 200, 'Unexpected status code for /trainers'
    jd = response.json()
    assert jd['data'][0]["trainer_name"] == "Санек"