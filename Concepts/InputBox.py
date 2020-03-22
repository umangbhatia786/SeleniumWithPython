import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()
driver.implicitly_wait(10)

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

# finding all input boxes on a web page

list_input_box = driver.find_elements(By.CLASS_NAME, 'text_field')

print('The number of input boxes are ' + str(len(list_input_box)))

# Filling Initial Details
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Umang')
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys('Bhatia')
driver.find_element(By.ID, 'RESULT_TextField-3').send_keys('9535832912')
driver.find_element(By.ID, 'RESULT_TextField-4').send_keys('India')
driver.find_element(By.ID, 'RESULT_TextField-5').send_keys('Kanpur')
driver.find_element(By.ID, 'RESULT_TextField-6').send_keys('bhatiau245@gmail.com')

# Selecting Gender
wait = WebDriverWait(driver, 15)
gender = wait.until(EC.element_to_be_clickable((By.ID, 'RESULT_RadioButton-7_0')))
gender.click()

# Selecting available days

root_id = 'RESULT_CheckBox-8_'

for i in range(1, 6):
    new_id = root_id + str(i)
    driver.find_element(By.ID, new_id).click()
    time.sleep(1)

drp_contact_time = Select(driver.find_element(By.ID, 'RESULT_RadioButton-9'))

list_options = drp_contact_time.options
print(len(list_options))

for option in list_options:
    print(option.text)

drp_contact_time.select_by_index(1)

driver.quit()
