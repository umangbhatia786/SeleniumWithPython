from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get('http://newtours.demoaut.com/index.php')

links_list = driver.find_elements(By.TAG_NAME, 'a')

print('There are ' + str(len(links_list)) + ' present on this page')
for link in links_list:
    print(link.text)

driver.quit()
