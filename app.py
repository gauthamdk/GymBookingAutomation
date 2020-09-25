import secret
from selenium import webdriver

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

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

push = driver.find_element_by_xpath("//*[@id=\"auth_methods\"]/fieldset/div[1]/button").click()
