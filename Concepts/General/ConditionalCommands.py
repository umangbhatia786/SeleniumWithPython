import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()

driver.get('http://newtours.demoaut.com/')

user_name = driver.find_element_by_name('userName')
password = driver.find_element_by_name('password')
btn_signIn = driver.find_element_by_name('login')

if user_name.is_displayed():
    print('UserName Text Box is daisplayed')
    if user_name.is_enabled():
        print('User Name Text Box is Enabled')
        user_name.send_keys('mercury')

if password.is_displayed():
    print('Password Text Box is displayed')
    if password.is_enabled():
        print('Password Text Box is enabled')
        password.send_keys('mercury')

btn_signIn.click()
time.sleep(5)

driver.quit()
