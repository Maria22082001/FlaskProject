import os
import sqlite3
import time
import pytest
from app import app, get_db_connection, create_table

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            create_table()  # Create the users table for testing
            yield client

def test_register_user(client):
    # Test user registration (POST request to '/')
    data = {
        'txt': 'testuser',
        'email': 'testuser@example.com',
        'pswd': 'password123'
    }

    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'User registered successfully!' in response.data

def test_get_db_connection():
    # Test database connection
    conn = get_db_connection()
    assert isinstance(conn, sqlite3.Connection)
    conn.close()

def test_index_route(client):
    # Test GET request to '/' (index route)
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Slide Navbar</title>' in response.data

def test_create_table():
    # Test database table creation
    create_table()  # Call the create_table function
    db_path = 'database.db'
    assert os.path.exists(db_path)  # Check if the database file exists
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    table_exists = cursor.fetchone()
    conn.close()
    assert table_exists is not None

def test_response_time(client):
    # Test response time for GET request to '/'
    start_time = time.time()
    response = client.get('/')
    end_time = time.time()

    assert response.status_code == 200
    assert end_time - start_time < 0.5  # Check if response time is within expected threshold
