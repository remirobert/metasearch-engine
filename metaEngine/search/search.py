import sys
import requests
sys.path.append("engine/")
import google
import bing
import yahoo
import result
from search_news import searchNews
from search_video import search_video
from search_images import search_image
from search_torrent import search_torrent
from information import cleanInformation

def defaultParameter():
    return {'method': 'GET', 'headers': {}, 'data': {}, 'url': '', \
            'cookies': {}, 'language':'all'}

def googleSearch(request):
    data = []
    param = defaultParameter()
    param['pageno'] = 0
    try:
        ret = google.request(request, param)
        r = requests.get(ret['url'])
    except:
        return []
    data = google.response(r)
    return data

def yahooSearch(request):
    data = []
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = yahoo.request(request, param)
        r = requests.get(ret['url'])
    except:
        return []
    data = yahoo.response(r)
    return data

def bingSearch(request):
    data = []
    param = defaultParameter()
    ret = bing.request(request, param)
    try:
        r = requests.get(ret['url'])
        r.headers['content-type']
    except:
        return []
    data = bing.response(r)
    return data

def search(request):
    if request == None:
        return
    dataGoogle = googleSearch(request)
    dataYahoo = yahooSearch(request)
    dataBing = bingSearch(request)
    cleanInformation(dataGoogle)
    cleanInformation(dataYahoo)
    cleanInformation(dataBing)
    result_data = result.parseResponse(dataGoogle, dataYahoo, dataBing)
    final_result = []
    for i in result_data:
        current_dict = {}
        current_dict["url"] = i.url
        current_dict["title"] = i.title
        current_dict["content"] = i.content
        final_result.append(current_dict)
    return final_result
