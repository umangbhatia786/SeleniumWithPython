from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.maximize_window()
driver.delete_all_cookies()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

driver.get('http://newtours.demoaut.com/index.php')

# Method1
driver.save_screenshot(r"C:\Users\Umang Bhatia\Documents\HomePage.png")

# Method2
driver.get_screenshot_as_file(r"C:\Users\Umang Bhatia\Documents\HomePage2.png")

driver.quit()
