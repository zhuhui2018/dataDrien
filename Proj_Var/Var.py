#encoding:utf-8

import os
import os.path

proj_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#用例存放路径
excel_file_path = os.path.join(proj_path,"TestData","126邮箱联系人.xlsx")

#元素定位方法配置文件所在路径
page_object_reposition_path = os.path.join(proj_path,"conf","PageObjectReposition.ini")
#print(page_object_reposition_path)

#日志文件所在路径
LogPath=os.path.join(proj_path,"conf","Logger.conf")
print(LogPath)

#驱动存放路径
chromeDriverPath=r"c:\chromedriver.exe"


