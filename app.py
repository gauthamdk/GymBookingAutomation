#!./env/bin/python3

import secret
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = webdriver.ChromeOptions()
# option.add_argument("headless")

driver = webdriver.Chrome("./chromedriver") # , options=option)  # Optional argument, if not specified will search path.
driver.get('https://nyuad.dserec.com/online/capacity/');

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

login = driver.find_element_by_xpath("//*[@id=\"page\"]/div/ul/li/a/span").click()

sso = driver.find_element_by_xpath("/html/body/div[2]/div[1]/a").click()

netid = driver.find_element_by_xpath("//*[@id=\"username\"]")
netid.send_keys(secret.user)

pwd = driver.find_element_by_xpath("//*[@id=\"password\"]")
pwd.send_keys(secret.password)
confirm_sso = driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div[1]/div[1]/div[4]/div/button").click()

WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,'iframe')))

push = driver.find_element_by_xpath("//*[@id=\"auth_methods\"]/fieldset[1]/div[2]/button").click()

WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,'iframe')))

time.sleep(5)

fitness = driver.find_element_by_xpath("//*[@id=\"page\"]/div/section/div/div/div/div/div/div/div/div/div[1]/div[1]/ul/li[8]/a").click()

#skipping 2 days
driver.find_element_by_xpath("//*[@id=\"page\"]/div/section/div/div/div/div/div/div/div/div/div[1]/div[2]/div[3]/a[2]").click()

driver.find_element_by_xpath("//*[@id=\"page\"]/div/section/div/div/div/div/div/div/div/div/div[1]/div[2]/div[3]/a[2]").click()

# selecting time 
time.sleep(5)

try:
    driver.find_elements_by_xpath("//*[contains(text(), '4:')]")[1].click()
except:
    driver.find_elements_by_xpath("//*[contains(text(), '5:')]")[1].click()

# clicking reserve
time.sleep(5)
driver.find_elements_by_xpath("//*[contains(text(), 'Confirm')]")[1].click()

driver.implicitly_wait(10)

print("Successfully booked")
