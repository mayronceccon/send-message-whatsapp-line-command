# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from qrcode import Qrcode

print("Started process")

print("Load Firefox")
options = Options()
options.headless = True
path = os.path.abspath('.')
path_geckodriver = os.path.join(path, 'geckodriver/geckodriver-v0.24.0-linux64/geckodriver')
driver = webdriver.Firefox(executable_path=path_geckodriver, options=options)
driver.get("https://web.whatsapp.com/")

Qrcode(driver)

running = True
while running:
    recipient = input("To: ")
    message = input("Message: ")

    elem = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"' + recipient + '")]'))
    )
    elem.click()

    inp_xpath = '//div[@data-tab="1"][contains(@class,"copyable-text") and contains(@class,"selectable-text")]'
    input_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, inp_xpath))
    )
    input_box.send_keys(message + Keys.ENTER)
    message_log = "Send message (%s) to (%s)" % (message, recipient)
    print(message_log)

    exit_send = int(input("Enter 1 to exit or 0 to continue: "))
    if exit_send == 1:
        running = False

driver.quit()
