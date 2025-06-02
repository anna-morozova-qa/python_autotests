import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '79955b79fa7ed5873b882789a985b236'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 34205 

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers/34205', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['trainer_name'] == 'Анна Морозова'

