import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

LOG_DIR = os.path.join(BASE_DIR, 'part3', 'log')
MY_LOG = os.path.join(LOG_DIR, 'my.log')

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'o_fmt1': {
            'format': '%(name)s:%(asctime)s - %(message)s'
        },
        'o_fmt2': {
            'format': '%(name)s:%(asctime)s [%(levelname)s] - %(message)s'
        }
    },
    'filters': {},
    'handlers': {
        'o_cmd': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'o_fmt1'
        },
        'o_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'o_fmt2',
            'filename': MY_LOG,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5, #日志文件最大个数
            'encoding': 'utf-8',  # 日志文件的编码
        }
    },
    'loggers': {
        'o_owen': {
            'level': 'DEBUG',
            'handlers': ['o_cmd', 'o_file']
        },
        'o_zero': {
            'level': 'DEBUG',
            'handlers': ['o_cmd', 'o_file']
        }
    }
}


