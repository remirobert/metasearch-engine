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
    data = []
    param = defaultParameter()
    ret = youtube.request(request, param)
    try:
        r = requests.get(ret['url'])
        r.headers['content-type']
    except:
        return []
    data = youtube.response(r)
    return data    

def dailymotion_search(request):
    data = []
    param = defaultParameter()
    ret = dailymotion.request(request, param)
    try:
        r = requests.get(ret['url'])
        r.headers['content-type']
    except:
        return []
    data = dailymotion.response(r)
    return data    

def extractImgSrc(currentContent):
    link = ""
    try:
        link = currentContent.split("<img src=\"")[1].split("\"")[0]
    except:
        print "notfound"
    return None

def search_video(request):
    finalData = []
    dataYoutube =  youtube_search(request)
    dataDailymotion = dailymotion_search(request)
    for i in dataYoutube:
        finalData.append(i)
    for i in range(0, 5):
        if i < len(dataDailymotion):
            finalData.append(dataDailymotion[i])

    print finalData
    return finalData
