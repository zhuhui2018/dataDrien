#encoding:utf-8

from configparser import ConfigParser
from Proj_Var.Var import *

class ParsePageObjectRepositionConfig(object):
    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(page_object_reposition_path)

    def getItemsFromSection(self,sectionName):
        #转换成字典类型，通过键值对获取内容
        return dict(self.cf.items(sectionName))

    def getOptionsValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)

if __name__ == "__main__":
    p=ParsePageObjectRepositionConfig()
    print(p.getItemsFromSection("126mail_login")['login_page.passwordlogin'])
    print(p.getOptionsValue("126mail_homepage","login_page.addressbook"))