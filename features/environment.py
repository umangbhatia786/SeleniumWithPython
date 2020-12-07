from features.pages.font_form import FontForm
from features.pages.notepad_app import NotePad
from selenium import webdriver
from features.browser import Browser
from behave import *


def before_all(context):
    context.browser = Browser()
    '''context.login_page = LoginPage()
    context.header = Header()
    context.home_page = HomePage()'''
    context.notepad_app = NotePad()
    context.font_form = FontForm()
        
def after_all(context):
    #context.browser.closeBrowser()
    print('====== Closing the browser ======')

# def before_scenario(context, scenario):
#     if 'TC_' in str(scenario):
#         print ('===Before Scenario===' + str(scenario))
#         context.browser = Browser()
#         context.login_page = LoginPage()

# def after_scenario(context, scenario):
#     if 'TC_' in str(scenario):
#         print ('===After Scenario===' + str(scenario))
#         context.browser.close()
