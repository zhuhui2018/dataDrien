#encoding:utf-8

from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import traceback
from selenium.webdriver.support import expected_conditions as EC

class WaitUtil(object):
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,5)
        self.locate_method = {
                "id":By.ID,
                "xpath":By.XPATH,
                "partial_link_text":By.PARTIAL_LINK_TEXT,
                "name":By.NAME,
                "link_text":By.LINK_TEXT
        }

    def getElement(self,locateMethod,locateExpression):
        #获取单个页面元素对象
        try:
            element = self.wait.until(lambda x:x.find_element \
                (self.locate_method[locateMethod],locateExpression))
            return element
        except:
            traceback.print_exc()
            raise Exception("所定位的元素不存在")

    def getElements(self,locateMethod,locateExpression):
        #获取多个页面元素，以list返回
        try:
            elements = self.wait.until(lambda x:x.find_element \
            (self.locate_method[locateMethod],locateExpression))
            return elements
        except Exception as e:
            raise e

    def presenceOfElement(self,locateMethod,locateExpression):
        try:
            element = self.wait.until(lambda x:x.find_element(self.locate_method[locateMethod],locateExpression))
            return element
        except:
            traceback.print_exc()
            raise Exception("所定位的素不存在")

    #显示等待，显示在DOM中才能找到
    def visibleOfElement(self,locateMethod,locateExpression):
        try:
            element = self.wait.until(EC.visibility_of_element_located((self.locate_method[locateMethod],
                                                                       locateExpression)))
            return element
        except:
            traceback.print_exc()
            raise Exception("所定位的元素不存在")

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
    waitutil = WaitUtil(driver)
    driver.get("http://mail.126.com")
    time.sleep(3)
    print(waitutil.getElement(driver,"xpath","//a[@id='switchAccountLogin']"))