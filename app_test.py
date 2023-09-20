import io
import sys
import pytest
from flask import Flask

# Import the Flask application for testing
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_index_text(client):
    response = client.get('/')
    assert b'Python Operations with Flask Routing and Views' in response.data

def test_print_route(client):
    response = client.get('/print/hello')
    assert response.status_code == 200

def test_print_text(client):
    response = client.get('/print/hello')
    assert b'hello' in response.data

def test_print_text_in_console(client, capsys):
    client.get('/print/hello')
    captured_out, _ = capsys.readouterr()
    assert captured_out == "Printed String: hello\n"

def test_count_route(client):
    response = client.get('/count/5')
    assert response.status_code == 200

def test_count_range_10(client):
    response = client.get('/count/10')
    expected_text = '\n'.join(str(num) for num in range(1, 11))
    assert expected_text.encode('utf-8') in response.data


def test_math_route(client):
    response = client.get('/math/5/+/5')
    assert response.status_code == 200

def test_math_add(client):
    response = client.get('/math/5/+/5')
    assert b'10' in response.data

def test_math_subtract(client):
    response = client.get('/math/5/-/5')
    assert b'0' in response.data

def test_math_multiply(client):
    response = client.get('/math/5/*/5')
    assert b'25' in response.data

def test_math_divide(client):
    response = client.get('/math/5/div/5')
    assert b'1.0' in response.data

def test_math_modulo(client):
    response = client.get('/math/5/%/5')
    assert b'0' in response.data
