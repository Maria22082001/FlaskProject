import pytest
from app import app, get_db_connection

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_index_route(client):
    # Test GET request to '/'
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Flask application!' in response.data

def test_register_user(client):
    # Test POST request to '/' to register a new user
    username = 'testuser'
    email = 'testuser@example.com'
    password = 'password123'

    response = client.post('/', data={
        'txt': username,
        'email': email,
        'pswd': password
    })
    assert response.status_code == 200
    assert b'User registered successfully!' in response.data

    # Verify user is added to the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    assert user is not None
    assert user['email'] == email
    assert user['password'] == password
