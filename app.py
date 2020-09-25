import secret
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("./chromedriver")  # Optional argument, if not specified will search path.
driver.get('https://nyuad.dserec.com/online/capacity/');

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

login = driver.find_element_by_xpath("//*[@id=\"page\"]/div/ul/li/a/span").click()

sso = driver.find_element_by_xpath("/html/body/div[2]/div[1]/a").click()

netid = driver.find_element_by_xpath("//*[@id=\"netid\"]")
netid.send_keys(secret.user)

pwd = driver.find_element_by_xpath("//*[@id=\"password\"]")
pwd.send_keys(secret.password)
confirm_sso = driver.find_element_by_xpath("//*[@id=\"login\"]/button").click()

WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,'iframe')))

push = driver.find_element_by_xpath("//*[@id=\"auth_methods\"]/fieldset/div[1]/button").click()

WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME,'iframe')))

driver.implicitly_wait(20)

fitness = driver.find_element_by_xpath("//*[@id=\"page\"]/div/section/div/div/div/div/div/div/div/div/div[1]/div[1]/ul/li[7]/a").click()

driver.find_element_by_xpath("//*[@id=\"page\"]/div/section/div/div/div/div/div/div/div/div/div[1]/div[2]/div[3]/a[2]").click()

driver.find_element_by_xpath("//*[@id=\"page\"]/div/section/div/div/div/div/div/div/div/div/div[1]/div[2]/div[3]/a[2]").click()

# selecting time 
# has to be different for some days 
driver.find_element_by_xpath("//*[@id=\"page\"]/div/section/div/div/div/div/div/div/div/div/div[1]/div[2]/div[4]/div/div/div/div/div[3]").click()

driver.implicitly_wait(3)

# clicking reserve
driver.find_element_by_xpath("//*[@id=\"page\"]/div/section/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[2]/button[2]").click()
