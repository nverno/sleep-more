#!/usr/bin/env python

import os
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = os.environ["GITHUB_USERNAME"]
password = os.environ["GITHUB_PASSWORD"]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
# options.add_argument('--test-type')

driver = webdriver.Chrome(options=options)
driver.get('https://www.interview-db.com/')

github_signin = '/students/auth/github'
driver\
    .find_element_by_xpath(f"//a[@href='{github_signin}']")\
    .click()

driver\
    .find_element_by_xpath("//input[@name='login']")\
    .send_keys(username)

driver\
    .find_element_by_xpath("//input[@name='password']")\
    .send_keys(password)

driver\
    .find_element_by_xpath("//input[@name='commit']")\
    .click()

# interview-db
driver\
    .find_element_by_id('react-tabs-4').click()

# need to wait for tab panel to load
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='react-tabs-5']/div/div/button[1]")
        ))
    # print(element)

    for btn in driver.find_elements_by_xpath('//*[@id="react-tabs-5"]//button'):
        print("Clicking ", btn.text)
        btn.click()
    print('clicked em')
    
except Exception:
    print('oops, you get a strike lol')

finally:
    driver.close()
