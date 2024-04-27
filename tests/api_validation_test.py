import pytest
from app import app, get_db_connection

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_valid_user_registration(client):
    # Test valid user registration with complete data
    data = {
        'txt': 'testuser',
        'email': 'testuser@example.com',
        'pswd': 'password123'
    }

    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'User registered successfully!' in response.data

def test_invalid_user_registration_missing_data(client):
    # Test invalid user registration with missing data (e.g., missing email)
    data = {
        'txt': 'testuser',
        'pswd': 'password123'
    }

    response = client.post('/', data=data)
    assert response.status_code == 400
    assert b'Bad Request' in response.data

def test_invalid_user_registration_invalid_email(client):
    # Test invalid user registration with invalid email format
    data = {
        'txt': 'testuser',
        'email': 'invalid_email',  # Invalid email format
        'pswd': 'password123'
    }

    response = client.post('/', data=data)
    assert response.status_code == 400
    assert b'Bad Request' in response.data

def test_invalid_user_registration_missing_username(client):
    # Test invalid user registration with missing username
    data = {
        'email': 'testuser@example.com',
        'pswd': 'password123'
    }

    response = client.post('/', data=data)
    assert response.status_code == 400
    assert b'Bad Request' in response.data
