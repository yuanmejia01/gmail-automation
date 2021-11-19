from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#abrir Google Chrome
driver =  webdriver.Chrome()

#Maximizar ventana
driver.maximize_window()

#delete cookies
driver.delete_all_cookies()

#navigate to the url
driver.get("https://www.gmail.com")

driver.find_element_by_id("identifierId").send_keys("yuanmejia01@gmail.com")

time.sleep(2)

#identificar usuario
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()

time.sleep(3)

driver.find_element_by_name("password").send_keys("###############")
time.sleep(3)

driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
time.sleep(3)

driver.close()
print("Gmail login succesfully completed")