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

if __name__ == "__main__":
  
  resultSearch = search("")
  printResult(resultSearch)  
