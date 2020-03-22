from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")
# driver = webdriver.Ie(r"C:\Users\Umang Bhatia\Documents\Drivers\IEDriverServer.exe")

driver.maximize_window()
driver.delete_all_cookies()

driver.get('http://newtours.demoaut.com/')

print(driver.title)
print(driver.current_url)

driver.close()
