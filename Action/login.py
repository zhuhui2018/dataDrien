#encoding:utf-8

from selenium import webdriver
from Util.Log import *
from Util.getTime import *
from PageObject.login_page import *
from PageObject.home_page import *

def login(driver,username,password):
    lg=LoginPage(driver)
    lg.login(username,password)
    info("login success")