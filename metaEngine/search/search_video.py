import sys
import requests
sys.path.append("engine/")
import result
import vimeo
import dailymotion
import youtube
from search_news import searchNews
from printDebug import printVideo

def defaultParameter():
    return {'method': 'GET', 'headers': {}, 'data': {}, 'url': '', \
            'cookies': {}, 'language':'all', 'pageno':10}

def youtube_search(request):
    data = None
    param = defaultParameter()
    ret = youtube.request(request, param)
    print "url vimeo : ", ret['url']
    try:
        r = requests.get(ret['url'])
        print r
        r.headers['content-type']
    except:
        return None
    print "repsonse vimeo :", r
    data = youtube.response(r)
    return data    

def dailymotion_search(request):
    data = None
    param = defaultParameter()
    ret = dailymotion.request(request, param)
    print "url vimeo : ", ret['url']
    try:
        r = requests.get(ret['url'])
        print r
        r.headers['content-type']
    except:
        return None
    print "repsonse vimeo :", r
    data = dailymotion.response(r)
    return data    

def vimeo_search(request):
    data = None
    param = defaultParameter()
    ret = vimeo.request(request, param)
    print "url vimeo : ", ret['url']
    try:
        r = requests.get(ret['url'])
        print r
        r.headers['content-type']
    except:
        return None
    print "repsonse vimeo :", r
    data = vimeo.response(r)
    return data


def search_video(request):
    finalData = []
    dataYoutube =  youtube_search(request)
    dataDailymotion = dailymotion_search(request)
    for i in range(0, 5):
        if i < len(dataYoutube):
            finalData.append(dataYoutube[i])
    for i in range(0, 5):
        if i < len(dataDailymotion):
            finalData.append(dataDailymotion[i])
    print dataDailymotion[0]
    printVideo(finalData)
    print finalData

