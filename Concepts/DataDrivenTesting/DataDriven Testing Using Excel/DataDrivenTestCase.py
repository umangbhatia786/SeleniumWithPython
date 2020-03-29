from XLUtils import *
from selenium import webdriver

test_data_path = r'C:\Users\Umang Bhatia\Documents\MercuryTestData.xlsx'

driver = webdriver.Chrome(executable_path=r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(60)
driver.implicitly_wait(20)

driver.get('http://newtours.demoaut.com/index.php')

rows = get_rows_count(test_data_path, 'Sheet1')
columns = get_columns_count(test_data_path, 'Sheet1')

for r in range(2, rows + 1):
    user_name = read_cell_data(test_data_path, 'Sheet1', r, 1)
    password = read_cell_data(test_data_path, 'Sheet1', r, 2)

    driver.find_element_by_name('userName').clear()
    driver.find_element_by_name('userName').send_keys(user_name)
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('login').click()

    if 'Find a Flight' in driver.title:
        print('Test Case ' + str(r - 1) + ' has passed')
        write_data_into_cell(test_data_path, 'Sheet1', r, 3, 'Passed')

    elif 'Sign-on' in driver.title:
        print('Test Case ' + str(r - 1) + ' has failed')
        write_data_into_cell(test_data_path, 'Sheet1', r, 3, 'Failed')

    driver.back()

driver.quit()
