import time

from selenium import webdriver

driver = webdriver.Chrome(
    executable_path=r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")  # setting up chrome driver

driver.maximize_window()  # maximizing browser window
driver.delete_all_cookies()  # deleting all cookies

driver.get('http://live.demoguru99.com/index.php/')

print(driver.title)
time.sleep(2)

driver.get('http://newtours.demoaut.com/')
print(driver.title)
time.sleep(2)

driver.back()
print(driver.title)
driver.forward()
print(driver.title)

driver.quit()
