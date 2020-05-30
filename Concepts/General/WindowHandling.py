from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get('http://demo.automationtesting.in/Windows.html')
print(driver.title)
driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()

for handle in driver.window_handles:
    driver.switch_to.window(handle)

print(driver.title)
print(driver.current_url)

driver.quit()
