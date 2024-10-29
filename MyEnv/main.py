from selenium import webdriver

def browser():
    chrome_driver = webdriver.Chrome()
    # firefox_driver = webdriver.Firefox()
    # edge_browser = webdriver.edge()
    chrome_driver.get("https://www.selenium.dev/")
    print("chrome initialized")

if __name__ == "__main__":
    browser()
    
