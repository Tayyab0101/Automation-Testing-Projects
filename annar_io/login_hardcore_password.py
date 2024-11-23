import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def load_config():
    with open("config.json", "r") as file:
        config = json.load(file)
    return config["email"], config["password"]

def logging_web():
    driver = webdriver.Chrome()

    try:
        username, password = load_config()
        #logging in
        url = "https://rmsdemo.anaar.io/admin/login"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(5)

        #locate elements/tabs
        email_field = driver.find_element(By.ID, "email").send_keys(username)
        password_field = driver.find_element(By.ID, "password").send_keys(password)
        login_button = driver.find_element(By.NAME, "submit")

        #select radio buttons
        admin_button = driver.find_element(By.XPATH, '//input[@type="radio" and @value="1"]')
        admin_button.click()
        login_button.click()

    except Exception as e:
        print(f"An exception occured: {e}")

    finally:
        print("Done as per commands")
        driver.quit()

logging_web()