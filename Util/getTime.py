#encoding:utf-8

import datetime,time

#返回当前日期
def get_current_date():
    current_date = datetime.datetime.now()
    current_date = str(current_date.year) +"年"+str(current_date.month) +"月"+\
                   str(current_date.day)+"日"
    return current_date

#返回当前时间
def get_current_time():
    current_time=datetime.datetime.now()
    current_time = str(current_time.hour)+"时"+str(current_time.minute)+"分"+\
                   str(current_time.second)+"秒"
    return current_time

#返回当前日期时间
def get_current_datetime():
    current_datetime=get_current_date()+" "+get_current_time()
    return current_datetime

if __name__ == "__main__":
    print(get_current_date())
    print(get_current_time())
    print(get_current_datetime())
