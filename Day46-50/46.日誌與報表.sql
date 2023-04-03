#如何通過Django的配置文件來配置日誌。 Django的日誌配置基本可以參照官方文檔再結合項目實際需求來進行

LOGGING = {
    'version': 1,
    # 是否禁用已经存在的日志器
    'disable_existing_loggers': False,
    # 日志格式化器
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': '%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
                      '%(module)s.%(funcName)s line %(lineno)d: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    # 日志过滤器
    'filters': {
        # 只有在Django配置文件中DEBUG值为True时才起作用
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 日志处理器
    'handlers': {
        # 输出到控制台
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'formatter': 'simple',
        },
        # 输出到文件(每周切割一次)
        'file1': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'access.log',
            'when': 'W0',
            'backupCount': 12,
            'formatter': 'simple',
            'level': 'INFO',
        },
        # 输出到文件(每天切割一次)
        'file2': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'error.log',
            'when': 'D',
            'backupCount': 31,
            'formatter': 'verbose',
            'level': 'WARNING',
        },
    },
    # 日志器记录器
    'loggers': {
        'django': {
            # 需要使用的日志处理器
            'handlers': ['console', 'file1', 'file2'],
            # 是否向上传播日志信息
            'propagate': True,
            # 日志级别(不一定是最终的日志级别)
            'level': 'DEBUG',
        },
    }
}

1.%(name)s - 記錄器的名稱
2.%(levelno)s - 數字形式的日誌記錄級別
3.%(levelname)s - 日誌記錄級別的文本名稱
4.%(filename)s - 執行日誌記錄調用的源文件的文件名稱
5.%(pathname)s - 執行日誌記錄調用的源文件的路徑名稱
6.%(funcName)s - 執行日誌記錄調用的函數名稱
7.%(module)s - 執行日誌記錄調用的模塊名稱
8.%(lineno)s - 執行日誌記錄調用的行號
9.%(created)s - 執行日誌記錄的時間
10.%(asctime)s - 日期和時間
11.%(msecs)s - 毫秒部分
12.%(thread)d - 線程ID（整數）
13.%(threadName)s - 線程名稱
14.%(process)d - 進程ID （整數）