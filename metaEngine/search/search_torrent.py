import sys
import requests
sys.path.append("engine/")
import piratebay

def defaultParameter():
    return {'method': 'GET', 'headers': {}, 'data': {}, 'url': '', \
            'cookies': {}, 'language':'all'}

def piratebay_search(request):
    data = None
    param = defaultParameter()
    param['pageno'] = 0
    param['category'] = "videos"
    try:
        ret = piratebay.request(request, param)
        r = requests.get(ret['url'])
    except:
        return None
    data = piratebay.response(r)
    return data

def search_torrent(request):
    print piratebay_search(request)
