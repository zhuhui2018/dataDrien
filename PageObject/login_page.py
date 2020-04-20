#encoding:utf-8

from Util.ParsePageObjectReposition import *
from Util.waitUtil import *

class LoginPage(object):
    def __init__(self,driver):
        self.driver = driver
        self.login_page_items = ParsePageObjectRepositionConfig().getItemsFromSection("126mail_login")

    #获取密码登录元素
    def passwordlogin(self):
        #定位登录登录元素
        locateMethod,locateExpression = self.login_page_items["login_page.passwordlogin"].split(">")
        passwordLogin =  WaitUtil(self.driver).getElement(locateMethod,locateExpression)
        return passwordLogin

    #定位iframe元素
    def iframe(self):
        locateMethod,locateExpression = self.login_page_items["login_page.iframe"].split(">")
        iframe =  WaitUtil(self.driver).getElement(locateMethod,locateExpression)
        return iframe

    #定位账号输入框元素
    def username(self):
        locateMethod,locateExpression = self.login_page_items["login_page.username"].split(">")
        username =  WaitUtil(self.driver).getElement(locateMethod,locateExpression)
        return username

    #定位密码输入框
    def password(self):
        "定位密码输入框元素"
        locateMethod,locateExpression=self.login_page_items["login_page.password"].split(">")
        password =  WaitUtil(self.driver).getElement(locateMethod,locateExpression)
        return password

    #定位登录按钮
    def loginButton(self):
        locateMethod, locateExpression = self.login_page_items["login_page.loginbutton"].split(">")
        login = WaitUtil(self.driver).getElement(locateMethod, locateExpression)
        return login

    #封装登录方法
    def login(self,username,password):
        self.driver.get("http://mail.126.com")
        self.driver.implicitly_wait(5)
        self.passwordlogin().click()
        self.driver.switch_to.frame(self.iframe())
        self.username().clear()
        self.username().send_keys(username)
        self.password().clear()
        self.password().send_keys(password)
        self.loginButton().click()
        time.sleep(2)



if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    lg=LoginPage(driver)
    lg.login("zhuhui202","zhuhui19930809.")