#encoding:utf-8

from selenium import webdriver
import time
from PageObject.login_page import *
from Action.login import *

def visit_address_page(driver):
    hp=HomePage(driver)
    hp.address_book_page_link().click()
    time.sleep(3)

if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    login(driver, "zhuhui202", "zhuhui19930809.")
    visit_address_page(driver)