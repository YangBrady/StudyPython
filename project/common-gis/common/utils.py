import datetime
import os


def getTimeSpanS(starttime):
    endtime = datetime.datetime.now()
    totalSeconds = (endtime - starttime).seconds
    return totalSeconds


def getTimeSpanMin(starttime):
    totalSeconds = getTimeSpanS(starttime)
    return totalSeconds / 60


def getFileName(restivePath):
    (filepath, tempfilename) = os.path.split(restivePath)
    (filename, extension) = os.path.splitext(tempfilename)
    return filename


def mkdir(dirPath):
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)
