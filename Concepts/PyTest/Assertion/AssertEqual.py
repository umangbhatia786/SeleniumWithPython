import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def testName(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)

        self.driver.get('https://www.google.co.in/')

        page_title = self.driver.title

        self.assertEqual('Google', page_title, 'Title did not match')

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
