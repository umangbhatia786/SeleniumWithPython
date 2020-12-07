from selenium.webdriver.common.by import By
# from browser import Browser
from features.pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
class FontFormLocator(object):
    TEXT_SIZE_PARENT = (By.ID, '1138')
    TEXT_SIZE_CHILD = (By.ID, '1001')
    BTN_OK = (By.ID, '1')

class FontForm(PageBase):

    def set_font_size(self, font_size):
        sleep(4)
        #self.wait_for_element_present(*FontFormLocator.TEXT_SIZE_PARENT)
        self.click_element_advanced(FontFormLocator.TEXT_SIZE_PARENT, FontFormLocator.TEXT_SIZE_CHILD)
        sleep(3)
        self.enter_text_advanced(font_size,FontFormLocator.TEXT_SIZE_PARENT,FontFormLocator.TEXT_SIZE_CHILD)
        #self.wait_for_element_present(*FontFormLocator.BTN_OK)
        sleep(3)
        self.click_element(*FontFormLocator.BTN_OK)