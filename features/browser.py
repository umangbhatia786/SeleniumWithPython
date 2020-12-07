from selenium import webdriver
import os

dirpath = os.getcwd()
winium_driver_path_used = dirpath + r'/features/resources/drivers/Winium.Desktop.Driver.exe'

class Browser(object):
    os.startfile(winium_driver_path_used)
    driver = webdriver.Remote(
        command_executor='http://localhost:9999',
        desired_capabilities={
            "debugConnectToRunningApp": 'false',
            "app": r"C:\Windows\System32\notepad.exe"
    })
    '''driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()'''
    #print('====== Opening Chrome browser ======')

    '''def closeBrowser(context):
        context.driver.close()
        # context.driver.quit()'''
