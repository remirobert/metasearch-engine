import sys
import requests
sys.path.append("engine/")
import google_news
import bing_news
import yahoo_news
import result
from data import DataResult
from printDebug import printResult

def defaultParameter():
    return {'method': 'GET', 'headers': {}, 'data': {}, 'url': '', \
            'cookies': {}, 'language':'all'}


def google_news_search(request):
    data = []
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = google_news.request(request, param)
        r = requests.get(ret['url'])
    except:
        return []
    data = google_news.response(r)
    return data

def yahoo_news_search(request):
    data = []
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = yahoo_news.request(request, param)
        r = requests.get(ret['url'])
    except:
        return []
    data = yahoo_news.response(r)
    return data

def bing_news_search(request):
    data = []
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = bing_news.request(request, param)
        r = requests.get(ret['url'])
    except:
        return []
    data = bing_news.response(r)
    return data

def searchNews(request):
    dataGoogle = google_news_search(request)
    dataYahoo = yahoo_news_search(request)

    finalData = []
    for i in dataGoogle:
        current_dict = {}
        current_dict["url"] = i["url"]
        current_dict["title"] = i["title"]
        current_dict["content"] = i["content"]
        current_dict["date"] = i["publishedDate"]
        finalData.append(current_dict)

    for i in dataYahoo:
        if len(i) > 1:
            current_dict = {}
            current_dict["url"] = i["url"]
            current_dict["title"] = i["title"]
            current_dict["content"] = i["content"]
            current_dict["date"] = i["publishedDate"]
            finalData.append(current_dict)
    return finalData

