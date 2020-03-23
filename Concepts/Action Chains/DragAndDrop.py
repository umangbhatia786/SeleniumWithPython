import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.delete_all_cookies()
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

rome = driver.find_element_by_id('box6')
italy = driver.find_element_by_id('box106')

actions = ActionChains(driver)

actions.drag_and_drop(rome, italy).perform()

time.sleep(3)

driver.quit()
