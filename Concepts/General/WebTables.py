from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(15)

driver.get('https://testautomationpractice.blogspot.com/')
wait = WebDriverWait(driver, 10)

el = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="HTML9"]/div[1]/button')))
el.send_keys(Keys.PAGE_DOWN, Keys.PAGE_DOWN, Keys.PAGE_DOWN)

num_rows = len(driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr'))
num_cols = len(driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td'))

for r in range(2, num_rows + 1):
    for c in range(1, num_cols + 1):
        val = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[' + str(r) + ']/td[' + str(c) + ']')
        print(val.text, end=' | ')
    print('\n')

driver.quit()
