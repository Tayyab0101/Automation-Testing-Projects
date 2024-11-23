from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def access_web():
    driver = webdriver.Chrome()
    try:
        #access the web
        url = "https://www.saucedemo.com/"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        
        # Locate the username, password fields and login button
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        # Enter the credentials and click the login button
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        time.sleep(5)


    except Exception as e:
        print(f"An exception occured {e}")

    finally:
        print("site loaded")

access_web()