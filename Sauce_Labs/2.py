from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def fetch_credentials():
    # Initialize WebDriver
    driver = webdriver.Chrome()

    try:
        # Navigate to the website
        url = "https://www.saucedemo.com/"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        # Locate username and password elements
        username_element = driver.find_element(By.ID, "login_credentials")
        password_element = driver.find_element(By.CLASS_NAME, "login_password")

        # Extract and clean the text
        usernames = username_element.text.strip().split("\n")[1:]  # Skip the first line "Accepted usernames are:"
        password = password_element.text.strip().split("\n")[1]    # Fetch the second line for password

        # Return the first username and password
        return usernames[0], password  # You can update to select other users if needed

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    finally:
        driver.quit()

def login():
    # Initialize WebDriver
    driver = webdriver.Chrome()

    try:
        # Navigate to the website
        url = "https://www.saucedemo.com/"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)

        # Locate the username, password fields and login button
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        # Enter the credentials and click the login button
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # Return the data
        data = {
            "usernames": username,
            "password": password,
            "login_header": login_header,
            "product_titles": product_titles
        }
        print(data)
        return data

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

# Run the login function
login()
