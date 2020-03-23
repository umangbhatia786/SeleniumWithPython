from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.delete_all_cookies()
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

driver.get('https://testautomationpractice.blogspot.com/')

# Performing double Click Action
text = 'Copy Me!'
driver.find_element_by_id('field1').clear()
driver.find_element_by_id('field1').send_keys(text)

btn_copy = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')

# Performing Double Click on Copy Button
actions = ActionChains(driver)
actions.double_click(btn_copy).perform()

copied_text = driver.find_element_by_id('field2').get_attribute('value')

assert copied_text == text

driver.quit()
