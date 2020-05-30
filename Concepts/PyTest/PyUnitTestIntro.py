import unittest

from selenium import webdriver


class SearchEngineTest(unittest.TestCase):

    def test_google(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.get('https://www.google.co.in/')
        self.driver.set_page_load_timeout(15)
        self.driver.maximize_window()
        self.assertEqual(self.driver.title, 'Google', 'The Title of the Page is not google')
        self.driver.quit()

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Umang Bhatia\Documents\Drivers\chromedriver.exe")
        self.driver.delete_all_cookies()
        self.driver.get('https://www.bing.com/')
        self.driver.set_page_load_timeout(15)
        self.driver.maximize_window()
        self.assertEqual(self.driver.title, 'Bing', 'The Title of the Page is not google')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
