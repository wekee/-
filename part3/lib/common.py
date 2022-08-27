# 提供共有资源的模块
import logging
import logging.config
from part3.conf import setting
def fn():
    print(setting.LOGGING_DIC)


import logging.config
from part3.conf import setting
def getLogger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger
