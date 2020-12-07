from selenium.webdriver.common.by import By
# from browser import Browser
from features.pages.page_base import PageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
from time import sleep

class NotePadLocator(object):
    # Header Locators
    TEXT_PANE = (By.ID, '15')
    DRP_FORMAT = (By.ID, 'Item 3')
    LST_ITEM_FONT = (By.ID, 'Item 33')
    CLOSE_BTN = (By.ID, 'Close')
    DONT_SAVE_BUTTON = (By.ID, 'CommandButton_7')

class NotePad(PageBase):
    #  Header Page Methods
    def write_text(self,text):
        self.enter_text(text,*NotePadLocator.TEXT_PANE)
        #self.click_element(*NotePadLocator.TEXT_PANE)

    def open_font_menu(self):
        self.click_element(*NotePadLocator.DRP_FORMAT)
        #self.wait_for_element_present(*NotePadLocator.LST_ITEM_FONT)
        sleep(3)
        self.click_element(*NotePadLocator.LST_ITEM_FONT)

    def close_notepad(self):
        sleep(2)
        self.click_element(*NotePadLocator.CLOSE_BTN)
        #self.wait_for_element_present(*NotePadLocator.DONT_SAVE_BUTTON)
        sleep(3)
        self.click_element(*NotePadLocator.DONT_SAVE_BUTTON)
        os.system("TASKKILL /F /IM Winium.Desktop.Driver.exe")