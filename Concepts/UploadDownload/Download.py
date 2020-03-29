import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_experimental_option('prefs', {"download.default_directory": "C://Users/I823285/Downloads"})
driver = webdriver.Chrome(executable_path=r'C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe',
                          options=chrome_options)

driver.delete_all_cookies()
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)

driver.get('http://demo.automationtesting.in/FileDownload.html')

# Download Text File
driver.find_element_by_id('textbox').send_keys('Download Demo 1')
driver.find_element_by_id('createTxt').click()

wait = WebDriverWait(driver, 5)

text_download_link = wait.until(EC.visibility_of_element_located((By.ID, 'link-to-download')))

text_download_link.click()

time.sleep(3)

# Download PDF File

driver.find_element_by_id('pdfbox').send_keys('Download Demo 2')
driver.find_element_by_id('createPdf').click()

pdf_download_link = wait.until(EC.visibility_of_element_located((By.ID, 'pdf-link-to-download')))

pdf_download_link.click()
time.sleep(3)

# close instance
driver.quit()
