import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.set_page_load_timeout(15)
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_google(self):
        self.driver.get('https://www.google.co.in/')
        self.assertEqual(self.driver.title, 'Google', 'The Title of the Page is not google')

    def test_bing(self):
        self.driver.get('https://www.bing.com/')
        self.assertEqual(self.driver.title, 'Bing', 'The Title of the Page is not google')


if __name__ == '__main__':
    unittest.main()
