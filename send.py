# -*- coding: utf-8 -*-
import time
import random
import json
import requests
import os
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-R", "--recipient", dest="recipient", help="Recipient of message", required=True)
parser.add_argument("-M", "--message", dest="message", help="Message to be sent", required=True)

args = parser.parse_args()
recipient = args.recipient
message = args.message

path = os.path.abspath('.')
path_geckodriver = path + '/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=path_geckodriver)
driver.get("https://web.whatsapp.com/")

input('Press enter after read captcha Whatsapp web')

wait = WebDriverWait(driver, 600)

elem = driver.find_element_by_xpath(
    '//span[contains(text(),"' + recipient + '")]'
)
elem.click()

inp_xpath = '//div[@data-tab="1"][contains(@class,"copyable-text") and contains(@class,"selectable-text")]'
input_box = wait.until(
    EC.presence_of_element_located((By.XPATH, inp_xpath))
)

now = datetime.datetime.now()
input_box.send_keys(message + Keys.ENTER)

message = "Send message (%s) to (%s)" % (message, recipient)
print(message)

driver.quit()
