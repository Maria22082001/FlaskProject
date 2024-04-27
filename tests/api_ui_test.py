import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    # Initialize Selenium WebDriver (replace with appropriate driver path)
    driver = webdriver.Chrome('/path/to/chromedriver')
    yield driver
    # Clean up after tests
    driver.quit()

def test_register_user(browser):
    # Open the application in the browser
    browser.get('http://localhost:5000')  # Adjust URL as needed

    # Fill out registration form
    username_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, 'txt'))
    )
    username_input.send_keys('testuser')

    email_input = browser.find_element_by_name('email')
    email_input.send_keys('testuser@example.com')

    password_input = browser.find_element_by_name('pswd')
    password_input.send_keys('password123')

    # Submit the form
    submit_button = browser.find_element_by_tag_name('button')
    submit_button.click()

    # Verify registration success message
    success_message = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'User registered successfully!')]"))
    )
    assert success_message.is_displayed()

    # Verify user registration in the database (optional)
    # You can use the get_db_connection() function to query the database

    # Additional assertions can be added as needed
