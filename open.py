import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = "dffds"
pwd = "sdfds"
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

elem = driver.find_element_by_xpath('//span[contains(text(),"MT 18")]')
elem.click()
time.sleep(2)

time.sleep(10)
driver.quit()
