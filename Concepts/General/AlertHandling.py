import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.get('https://testautomationpractice.blogspot.com/')

driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()

time.sleep(3)

# For switiching to alert popup
alert_popup = driver.switch_to_alert()

# accepting the alert
alert_popup.accept()

time.sleep(2)

driver.quit()
