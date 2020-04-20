#encoding:utf-8

import logging.config
from Proj_Var.Var import *

#读取日志的配置文件
logging.config.fileConfig(LogPath)
#选择一个日志格式
logger=logging.getLogger("example02")

def error(message):
    #打印error级别的信息
    logger.error(message)

def info(message):
    #打印info级别的信息
    logger.info(message)

def warning(message):
    #打印warnning级别的信息
    logger.warning(message)

if __name__ == "__main__":
    info("world")
    warning("passwrod")
    error("password")