from data import DataResult

def printResult(resultData):
    for currentData in resultData:
        print "\033[31m", currentData.title, " \033[32m", currentData.url, \
            " \033[33m", currentData.content, "\033[0m\n"

def printVideo(resultData):
    for currentData in resultData:
        print "\033[31m", currentData["url"], " \033[32m", currentData["title"], \
            " \033[33m", currentData["content"], \
            "\033[0m\n"

