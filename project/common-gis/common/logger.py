import logging


def configLog(logFile, enableConsle=False):
    clearLog(logFile=logFile)
    logFormatter = '%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s'
    logging.basicConfig(filename=logFile, level=logging.DEBUG, format=logFormatter)
    if (enableConsle):
        log2Console(logFormatter)


def log2Console(logFormatter):
    # 创建一个handler，用于输出到控制台
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # 设置格式
    formatter = logging.Formatter(logFormatter)
    # 告诉handler使用这个格式
    console.setFormatter(formatter)
    # 为root logger添加handler
    logging.getLogger('').addHandler(console)


def clearLog(logFile):
    # 清空log
    with open(logFile, 'w') as fLog:
        fLog.truncate()
        fLog.close()
