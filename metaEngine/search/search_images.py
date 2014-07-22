import sys
import requests
sys.path.append("engine/")
import google_images
import deviantart
import bing
import yahoo
import result

def defaultParameter():
    return {'method': 'GET', 'headers': {}, 'data': {}, 'url': '', \
            'cookies': {}, 'language':'all'}

def google_images_search(request):
    data = None
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = google_images.request(request, param)
        r = requests.get(ret['url'])
    except:
        return None
    data = google_images.response(r)
    return data

def devianart_images_search(request):
    data = None
    param = defaultParameter()
    param['pageno'] = 10
    try:
        ret = deviantart.request(request, param)
        r = requests.get(ret['url'])
    except:
        return None
    data = deviantart.response(r)
    return data

def search_image(request):
    print google_images_search(request)
    print devianart_images_search(request)
    
