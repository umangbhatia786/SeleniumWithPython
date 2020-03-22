import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get('https://www.expedia.co.in/')

# driver.find_element_by_id('tab-flight-tab-hp').click()  #This is one way we have been working so far
# Another way is shown below

driver.find_element(By.ID, 'tab-flight-tab-hp').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="flight-origin-hp-flight"]').send_keys('SFO')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="flight-destination-hp-flight"]').send_keys('NYC')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="flight-departing-hp-flight"]').clear()
driver.find_element(By.XPATH, '//*[@id="flight-departing-hp-flight"]').send_keys('23/03/2020')
time.sleep(1)
returnDate = driver.find_element(By.XPATH, '//*[@id="flight-returning-hp-flight"]')
returnDate.send_keys(Keys.CONTROL + "a", Keys.DELETE)
time.sleep(1)
returnDate.send_keys('28/03/2020')

driver.find_element(By.XPATH, '//*[@id="gcw-flights-form-hp-flight"]/div[8]/label/button').click()

# Explicit Wait in Python
wait = WebDriverWait(driver, 10)
el = wait.until(EC.element_to_be_clickable((By.ID, 'stopFilter_stops-0')))

el.click()
time.sleep(3)

driver.quit()
