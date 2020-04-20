#encodng:utf-8

from PageObject.addressBook import *

def add_contact(driver,name="",email="",is_star=True,mobile="",other_info=""):
    ap=AddressPage(driver)
    ap.add_contact_button().click()
    time.sleep(2)
    ap.contact_name().send_keys(name)
    ap.contact_email().send_keys(email)
    if is_star=="True":
        ap.contact_is_star().click()
    ap.contact_mobile().send_keys(mobile)
    ap.contact_other_info().send_keys(other_info)
    ap.contact_save_button().click()
    time.sleep(2)

if __name__=="__main__":
    driver=webdriver.Chrome(executable_path=r"c:\chromedriver.exe")
    login(driver,"zhuhui202", "zhuhui19930809.")
    visit_address_page(driver)
    add_contact(driver,"zhuhui","1223@qq.com",True,"13830102012","ceshi")
    driver.quit()