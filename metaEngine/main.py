import urllib2
import urllib
import sys
import mechanize
import json
import requests
sys.path.append("engine/")
import google
import bing
import yahoo
import result
from search import search
from printDebug import printResult

def googleEngine():
  param = {'method': 'GET', 'headers': {}, 'data': {}, 'url': '', 'cookies': {}, 'language':'all'}
  param['pageno'] = 10
  ret = google.request("iphone", param)
  print "ret Google ", ret
  r = requests.get(ret['url'])
  data = google.response(r)
  print len(data)
  for i in data:
    print i
  return data


def yahooEngine():
  param = {'method': 'GET', 'headers': {}, 'data': {}, 'url': '', 'cookies': {}, 'language':'all'}
  param['pageno'] = 11
  ret = yahoo.request("iphone", param)
  r = requests.get(ret['url'])
  print r
  print ret
  data = yahoo.response(r)
  print len(data)
  for i in data:
    print i
  return data

def bingEngine():
  param = {'method': 'GET', 'headers': {}, 'data': {}, 'url': '', 'cookies': {}}
  param['laguage'] = 'all'
  ret = bing.request("iphone", param)
  print ret['url']
  try:
    r = requests.get(ret['url'])
    r.headers['content-type']
    data = bing.response(r)
  except:
    print "Error parse bing"
  print len(data)
  for i in data:
    print i
  return data

if __name__ == "__main__":
  
  resultSearch = search("iphone")
  printResult(resultSearch)
  exit(0)
  
  yahooData = yahooEngine()
  bingData = bingEngine()
  googleData = googleEngine()

  result.parseResponse(googleData, yahooData, bingData)
  
