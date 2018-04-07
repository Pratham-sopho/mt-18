'''
### configurations
number_of_times = 1
### This Contact Name should be in recent chats , Should match exactly as it appears on contacts
name = 'Nabagata Saha'
message = 'Hi! are you there?'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

## Selenium web drivers
driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## load web driver for selenium : Firefox
def web_driver_load():
	global driver
	driver = webdriver.Firefox()
## quit web driver for selenium
def web_driver_quit():
	driver.quit()
	quit()

## actual login in hockey app site
def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	while True:
		time.sleep(25)
		try:
			appLoad = driver.find_element_by_xpath("//div[@class='CxUIE']")
			if appLoad:
				gotoChathead(name)
		except NoSuchElementException:
			print("Maa ki chu")
		finally:
			print('Login Checked')

def sendMessage(msg='Hi!'):
	web_obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
	web_obj.send_keys(msg)
	web_obj.send_keys(Keys.RETURN)

def gotoChathead(name):
	recentList = driver.find_elements_by_xpath("//span[@class='emojitext ellipsify']")
	for head in recentList:
		if head.text == name:
			head.click()
			break


### Main Method
if __name__ == "__main__":
	web_driver_load()
	whatsapp_login()
	for i in range(number_of_times):
		sendMessage(message)
		wait()
	print("Process complete successfully")
	web_driver_quit()
'''
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Firefox()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = "Nabagata Saha"

# Replace the below string with your own message
string1 = "Message sent using Python!!!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(1):
    input_box.send_keys(string1 + Keys.ENTER)
    time.sleep(1)
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# Replace below path with the absolute path
# to chromedriver in your computer
#driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Firefox()


driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Nabagata Saha"'
# Replace the below string with your own message
string = "Hello sexy"

def web_driver_quit():
	driver.quit()
	quit()

def send_message(target, string):
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    message.send_keys(string)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/button')[0]
    sendbutton.click()

if __name__ == "__main__":
    send_message(target, string)
    alert1 = driver.SwitchTo().Alert()
    alert1.Accept()
    web_driver_quit()
