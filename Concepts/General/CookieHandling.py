from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe')

driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

driver.get('https://www.amazon.in/')

# Capture All the cookies
cookies = driver.get_cookies()
print('The browser has %d cookies' % (len(cookies)))

print(cookies)  # prints all the cookies in dictionary format

# Add a cookie
my_cookie = {'name': 'My_Cookie', 'value': 'First'}
driver.add_cookie(my_cookie)

print(driver.get_cookies())

# Deleting cookie
driver.delete_cookie('My_Cookie')
print(len(driver.get_cookies()))

driver.quit()
