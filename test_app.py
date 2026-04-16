import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    resposta = client.get('/')
    assert resposta.status_code == 200
    assert resposta.json['status'] == 'sucesso'