from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)  # Set a wait time between requests

    @task
    def register_user(self):
        # Define the data to be sent in the POST request
        data = {
            'txt': 'testuser',
            'email': 'testuser@example.com',
            'pswd': 'password123'
        }

        # Send a POST request to register a new user
        self.client.post('/', data=data)

    @task
    def view_homepage(self):
        # Send a GET request to view the homepage
        self.client.get('/')

    # Add more tasks for other endpoints or actions as needed
