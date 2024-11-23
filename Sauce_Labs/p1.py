from selenium import webdriver
import time

def access_web():
    driver = webdriver.Chrome()
    try:
        url = "https://www.saucedemo.com/"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(5)

    except Exception as e:
        print(f"An exception occured {e}")

    finally:
        print("site loaded")

access_web()