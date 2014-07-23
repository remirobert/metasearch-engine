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
    data = None
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = google_news.request(request, param)
        r = requests.get(ret['url'])
    except:
        return None
    data = google_news.response(r)
    return data

def yahoo_news_search(request):
    data = None
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = yahoo_news.request(request, param)
        print ret["url"]
        r = requests.get(ret['url'])
    except:
        print "Errror get google news"
        return None

    print r
    
    data = yahoo_news.response(r)
    return data

def bing_news_search(request):
    data = None
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = bing_news.request(request, param)
        print ret["url"]
        r = requests.get(ret['url'])
    except:
        print "Errror get google news"
        return None

    print r
    
    data = bing_news.response(r)
    return data

def searchNews(request):
    dataGoogle = google_news_search(request)
    dataYahoo = yahoo_news_search(request)

    finalData = []
    for i in dataGoogle:
        data = DataResult(i["url"], 1, 0, 0)
        data.addInformation(i["title"], i["content"], i["publishedDate"])
        finalData.append(data)

    for currentYahooData in dataYahoo:
        if len(currentYahooData) > 1:
            data = DataResult(currentYahooData["url"], 1, 0, 0)
            data.addInformation(currentYahooData["title"], \
                                currentYahooData["content"], \
                                currentYahooData["publishedDate"])
            finalData.append(data)

    for i in finalData:
        print i.date
        #print i['publishedDate']
    return finalData

