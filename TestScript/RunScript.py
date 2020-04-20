# -*-coding:utf-8 -*-


from selenium import webdriver
from Util.Log import *
from Util.getTime import *
from Util.Excel import *
import time
from Action.login import *
from Action.add_contact import  *
from Action.visit_address_page import *
from Proj_Var.Var import *

def main():
    pe=ParseExcel(excel_file_path)
    pe.get_sheet_by_index(0)  # 防止默认sheet不是要操作的sheet对象，下同
    "获取第一个sheet的所有行"
    rows=pe.get_all_rows()
    for index,row in enumerate(rows[1:]):
        if row[4].value.lower()=="y":
            username=pe.get_cell_content(index + 2,2)
            password=pe.get_cell_content(index + 2,3)
            driver=webdriver.Chrome(chromeDriverPath)
            try:
                login(driver,username,password)
                visit_address_page(driver)
                sheetName=pe.get_cell_content(index+2,4)
                print("sheetName %s",sheetName)
                pe.get_sheet_by_name(sheetName)
                data_max_row=pe.get_max_row()
                for id in range(2,data_max_row+1):
                    whether_execute = pe.get_cell_content(id,8)
                    #print ("*************",whether_execute)
                    if whether_execute.lower() == "y":
                        #print("****************")
                        name=pe.get_cell_content(id, 2)
                        email=pe.get_cell_content(id, 3)
                        is_star=pe.get_cell_content(id, 4)
                        mobile=pe.get_cell_content(id, 5)
                        other_info=pe.get_cell_content(id, 6)
                        assert_word=pe.get_cell_content(id, 7)
                        try:
                            add_contact(driver, name=name, email=email, is_star=True, mobile=mobile,other_info=other_info)
                        except Exception as e:
                            pe.write_cell_content(id, 10, "添加联系人失败",color="red")
                        else:
                            try:
                                assert assert_word in driver.page_source
                            except Exception as e:
                                pe.write_cell_content(id, 10, "断言失败",color="red")
                            else:
                                pe.write_cell_content(id, 10, "成功",color="green")
                        finally:
                            pe.write_cell_current_time(id, 9)
                            pe.save_excel_file()
                    else:
                        pe.write_cell_current_time(id, 9)
                        pe.write_cell_content(id, 10, "忽略")
                        pe.save_excel_file()
            except Exception as e:
                print (e)
                pe.get_sheet_by_name("126账号")
                pe.write_cell_content(index+2, 6, "失败",color="red")
            else:
                pe.get_sheet_by_name("126账号")  # 之所以要加，是因为操作的sheet不同，否则会加错sheet
                pe.write_cell_content(index+2, 6, "成功",color="green")
            finally:
                pe.save_excel_file()
            driver.quit()
        else:
            pe.get_sheet_by_name("126账号")
            # print ("this case is ignored!")
            # row[5].value="忽略"      # 往测试结果中写入
            pe.write_cell_content(index+2,6,"忽略")  # 调用内部写的方法写入结果
            pe.save_excel_file()     # 写入内容后保存文件

if __name__=="__main__":
    main()