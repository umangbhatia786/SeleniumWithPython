from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
import time
from nose.tools import assert_equal, assert_true
from features.pages.test_base import TestBase
from features.pages.page_base import PageBase

test_base = TestBase()

@then(u'I write some "{text}" into the NotePad Console')
def step_impl(context, text):
    context.notepad_app.write_text(text)
    '''time.sleep(20)
    test_base.takesScreenshot()'''

@then(u'I open Font window from Format Dropdown in Menu')
def step_impl(context):
    context.notepad_app.open_font_menu()

@then(u'I change the Font Size as "{size}" and click ok')
def step_impl(context, size):
    context.font_form.set_font_size(size)

@then(u'I close the Notepad without saving any changes')
def step_impl(context):
    context.notepad_app.close_notepad()






