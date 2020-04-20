#encoding:utf-8

from Util.ParsePageObjectReposition import *
from Util.waitUtil import *
from Action.login import *

class HomePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.login_page_items = ParsePageObjectRepositionConfig().getItemsFromSection("126mail_homepage")

    def address_book_page_link(self):
        #点击通讯录
        locateMethod,locateExpression=self.login_page_items["login_page.addressbook"].split(">")
        homepage= WaitUtil(self.driver).getElement(locateMethod,locateExpression)
        return homepage

if __name__=="__main__":
    driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    login(driver, "zhuhui202", "zhuhui19930809.")
