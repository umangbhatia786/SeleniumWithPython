import time

from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")

driver.maximize_window()
driver.delete_all_cookies()

driver.get('http://live.demoguru99.com/index.php/')

print(driver.title)  # returns title of the page
print(driver.current_url)  # current url of the page

driver.find_element_by_xpath('//*[@id="nav"]/ol/li[1]/a').click()
print(driver.title)

time.sleep(3)
driver.quit()
