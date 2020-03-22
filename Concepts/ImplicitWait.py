import time

from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()

driver.get('http://newtours.demoaut.com/')
driver.implicitly_wait(4)  # maximum wait for any element on a page

try:
    assert "Welcome: Mercury Tours" in driver.title

except Exception as ex:
    print(ex)
    driver.quit()

driver.find_element_by_name('userName').send_keys('mercury')
driver.find_element_by_name('password').send_keys('mercury')
driver.find_element_by_name('login').click()

time.sleep(4)
driver.quit()
