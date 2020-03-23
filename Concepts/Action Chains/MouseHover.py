import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.delete_all_cookies()
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

driver.get('https://opensource-demo.orangehrmlive.com/')

# Login into CRM Application
driver.find_element_by_id('txtUsername').clear()
driver.find_element_by_id('txtUsername').send_keys('admin')
driver.find_element_by_id('txtPassword').clear()
driver.find_element_by_id('txtPassword').send_keys('admin123')
driver.find_element_by_id('btnLogin').click()

# Admin Tab

admin_tab = driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]')
user_manage_tab = driver.find_element(By.XPATH, '//*[@id="menu_admin_UserManagement"]')
users_tab = driver.find_element(By.XPATH, '//*[@id="menu_admin_viewSystemUsers"]')

actions = ActionChains(driver)

actions.move_to_element(admin_tab).move_to_element(user_manage_tab).move_to_element(users_tab).click().perform()

time.sleep(3)

driver.quit()
