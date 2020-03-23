import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.delete_all_cookies()
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

# Perform right click

btn_right_click = driver.find_element(By.XPATH, '/html/body/div/section/div/div/div/p/span')

actions = ActionChains(driver)
actions.context_click(btn_right_click).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(
    Keys.ENTER).perform()
time.sleep(2)
alert_box = driver.switch_to.alert

alert_box.accept()
time.sleep(2)
driver.quit()
