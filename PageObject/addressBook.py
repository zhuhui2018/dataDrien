#encoding:utf-8

import time
from Util.waitUtil import *
from Util.ParsePageObjectReposition import *
from selenium import webdriver
from Action.login import *
from Action.visit_address_page import *


class AddressPage(object):

    def __init__(self,driver):
        "初始化参数，加载配置文件，将'126mail_addcontactspage'section内容读取出来"
        self.driver=driver
        self.login_page_items=self.login_page_items = ParsePageObjectRepositionConfig().getItemsFromSection("126mail_addcontactspage")

    def add_contact_button(self):
        locateMethod,locateExpression=self.login_page_items["addcontacts_page.createcontactsbtn"].split(">")
        return WaitUtil(self.driver).getElement(locateMethod,locateExpression)

    def contact_name(self):
        locateMethod,locateExpression=self.login_page_items["addcontacts_page.contactpersonname"].split(">")
        return WaitUtil(self.driver).getElement(locateMethod,locateExpression)

    def contact_email(self):
        locateMethod,locateExpression=self.login_page_items["addcontacts_page.contactpersonemail"].split(">")
        return WaitUtil(self.driver).getElement(locateMethod,locateExpression)

    def contact_is_star(self):
        locateMethod,locateExpression=self.login_page_items["addcontacts_page.starcontacts"].split(">")
        return WaitUtil(self.driver).getElement(locateMethod,locateExpression)

    def contact_mobile(self):
        locateMethod,locateExpression=self.login_page_items["addcontacts_page.contactpersonmobile"].split(">")
        return WaitUtil(self.driver).getElement(locateMethod,locateExpression)

    def contact_other_info(self):
        locateMethod,locateExpression=self.login_page_items["addcontacts_page.contactpersoncomment"].split(">")
        return WaitUtil(self.driver).getElement(locateMethod,locateExpression)

    def contact_save_button(self):
        locateMethod,locateExpression=self.login_page_items["addcontacts_page.savecontactperson"].split(">")
        return WaitUtil(self.driver).getElement(locateMethod,locateExpression)