from selenium import webdriver
import time

def get_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximixed")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://practicetestautomation.com/practice-test-login/")

    return driver

def main():
    driver = get_driver()
    driver.find_element(by="id", value = 'username').send_keys("student")
    time.sleep(2)
    driver.find_element(by="id", value = 'password').send_keys("Password123") # + Keys.RETURN)

    driver.find_element(by="id", value = "submit").click()
    print(driver.current_url)


    
    element = driver.find_element(by="xpath",value = '//*[@id="loop-container"]/div/article/div[2]/p[1]/strong')
    return(element.text)


print(main())

                                  