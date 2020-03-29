import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html')

driver.switch_to.frame('packageListFrame')
driver.find_element(By.LINK_TEXT, 'org.openqa.selenium').click()
driver.switch_to.default_content()
time.sleep(1)

driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT, 'Rotatable').click()
driver.switch_to.default_content()
time.sleep(1)
driver.switch_to.frame('classFrame')

description = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/ul/li/div')

print(description.text)

driver.quit()
