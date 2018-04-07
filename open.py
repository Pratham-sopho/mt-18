import time
from html.parser import HTMLParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MLStripper(HTMLParser):

    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def mainMessage():
    time.sleep(8)
    rightChatBoxes = driver.find_elements_by_css_selector(".CxUIE")

    print(rightChatBoxes)

    i = 1
    for rightChatBox in rightChatBoxes:
        chatHead = driver.find_elements_by_css_selector("._3zmhL")[0]
        no_messages = int(chatHead.text)

        print(no_messages)
        rightChatBox.click()

        if i == 1:
            time.sleep(8)
            i = i+1

        messages = driver.find_elements_by_css_selector(".ZhF0n")[-no_messages:]

        for message in messages:
            print(strip_tags(message.text))


driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

#elem = driver.find_element_by_xpath('//span[contains(text(),"MT")]')
#elem.click()
time.sleep(2)

time.sleep(2)
mainMessage()

time.sleep(10)
driver.quit()
