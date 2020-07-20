# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 11:20
# @Site    :
# @File    : config.py
import os
import time
import logging.config


class BaseConfig:
    SECRET_KEY = os.urandom(24)


class MySQLConfig:
    USERNAME = 'root'
    PASSWORD = 'lwh135190.'
    PORT = '3306'
    ADDRESS = 'localhost'
    DATABASE = 'component'
    DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{ADDRESS}:{PORT}/{DATABASE}'


class LoggingConfig:
    LOGS_BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
    if not os.path.isdir(LOGS_BASE_DIR):
        os.mkdir(LOGS_BASE_DIR)
    DATE = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'simple': {
                'format': '[%(asctime)s] - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s'
            }
        },
        'filters': {},
        'handlers': {
            # 打印到终端的日志
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            # 打印到文件的日志,收集info及以上的日志
            'default': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，按日期切割
                'filename': os.path.join(LOGS_BASE_DIR, f"info_{DATE}.log"),  # 日志文件
                'backupCount': 7,
                'interval': 1,
                'when': 'MIDNIGHT',
                'formatter': 'simple',
                'encoding': 'utf-8',
            },
            # 打印到文件的日志:收集错误及以上的日志
            'error': {
                'level': 'ERROR',
                'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，按日期切割
                'filename': os.path.join(LOGS_BASE_DIR, f"err_{DATE}.log"),  # 日志文件
                'backupCount': 7,
                'interval': 1,
                'when': 'MIDNIGHT',
                'formatter': 'simple',
                'encoding': 'utf-8',
            }
        },
        'loggers': {
            'info': {
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'error': {
                'handlers': ['console', 'error'],
                'level': 'ERROR',
            }
        },
    }


class Logger(object):
    def __init__(self):
        logging.config.dictConfig(LoggingConfig.LOGGING)
        self.INFO = logging.getLogger('info')
        self.ERROR = logging.getLogger('error')


config = {
    'base': BaseConfig,
    'mysql': MySQLConfig,
    'logger': Logger()
}
