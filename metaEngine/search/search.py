import sys
import requests
sys.path.append("engine/")
import google
import bing
import yahoo
import result
from search_news import searchNews

def defaultParameter():
    return {'method': 'GET', 'headers': {}, 'data': {}, 'url': '', \
            'cookies': {}, 'language':'all'}

def googleSearch(request):
    data = None
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = google.request(request, param)
        r = requests.get(ret['url'])
    except:
        return None
    data = google.response(r)
    return data

def yahooSearch(request):
    data = None
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = yahoo.request(request, param)
        r = requests.get(ret['url'])
    except:
        return None
    data = yahoo.response(r)
    return data

def bingSearch(request):
    data = None
    param = defaultParameter()
    ret = bing.request(request, param)
    try:
        r = requests.get(ret['url'])
        r.headers['content-type']
    except:
        return None
    data = bing.response(r)
    return data

def search(request):
    if request == None:
        return
    dataGoogle = googleSearch(request)
    dataYahoo = yahooSearch(request)
    dataBing = bingSearch(request)

    searchNews(request)
    
    return result.parseResponse(dataGoogle, dataYahoo, dataBing)
