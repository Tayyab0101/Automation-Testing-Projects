from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def selenium_textbook():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--ignore-certificate-errors")
    
    # Initialize the Chrome WebDriver with options
    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the webpage
    driver.get("https://demoqa.com/text-box")
    print("Page opened successfully")
    
    # Wait for the element to be present before interacting
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "userName"))
    )
    
    # Interact with the first name input box
    first_name = driver.find_element(By.ID, "userName")
    first_name.send_keys("John")
    print("Text entered")
    
    time.sleep(5)  # Pause for demonstration
    
    # Clear the text after some time
    first_name.clear()
    time.sleep(5)
    
    # Quit the browser
    driver.quit()

if __name__ == "__main__":
    selenium_textbook()
