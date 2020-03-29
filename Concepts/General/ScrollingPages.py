import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.delete_all_cookies()
driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)

driver.get('https://www.countries-ofthe-world.com/all-countries.html')

driver.find_element(By.LINK_TEXT, 'World Flags').click()

# 1.Scroll Down by pixel

# driver.execute_script('window.scrollBy(0,1000)','')

# 2.Scroll down till desired element is visible
# finland_flag = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[66]/td[1]/img')
# driver.execute_script("arguments[0].scrollIntoView();", finland_flag)

# 3.Scroll Down to the end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

time.sleep(3)

driver.quit()
