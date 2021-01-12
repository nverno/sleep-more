#!/usr/bin/env python

import os
import sys
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

# interview-db: select attendance tab
attendance_tab = driver.find_element_by_xpath('//li[text() = "Attendance"]')
attendance_tab.click()

# need to wait for tab panel to load to access buttons
try:
    tab_id = attendance_tab.get_attribute('id')
    # print(f"tab_id: {tab_id}")
    panel = driver.find_element_by_xpath('//div[@role="tabpanel"]')

    # import pdb; pdb.set_trace()
    buttons = WebDriverWait(driver, 5).until(
        lambda d: panel.find_elements(By.XPATH, '//button'))
        # EC.presence_of_element_located(
        #     (By.XPATH, f"//*[@id='{tab_id}']/div/div/button[1]")
        # ))

    for btn in buttons:
        print("Clicking ", btn.text, file=sys.stderr)
        btn.click()

    print('clicked em')
    
except Exception:
    print('oops, you get a strike lol', file=sys.stderr)
    sys.exit(1)
    
finally:
    driver.close()
