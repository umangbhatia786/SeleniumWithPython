import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.delete_all_cookies()
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

driver.get('https://testautomationpractice.blogspot.com/')

driver.switch_to.frame(0)

choose_file_btn = driver.find_element_by_id('RESULT_FileUpload-10')

driver.execute_script("arguments[0].scrollIntoView();", choose_file_btn)

choose_file_btn.send_keys(
    r'C:\Users\Umang Bhatia\Documents\Web Development\Advanced DOM Manipulation\RGB Color Game\rgbStyle.css')

time.sleep(3)

driver.quit()
