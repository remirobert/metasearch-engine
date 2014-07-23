from data import DataResult
from information import pushInformationInData

def extractUrl(data):
    urls = []
    for currentUrl in data:
        if len(currentUrl) == 3:
            urls.append(currentUrl["url"])
    return urls

def parseGoogleLink(urlsGoogle, urlsYahoo, urlsBing, currentGoogleRank, \
                    restGoogle, finalData):
    rankGoogle = 0

    if urlsGoogle == None or len(urlsGoogle) == 0:
        return 1

    for currentGoogleUrl in urlsGoogle:
        rankYahoo = -1
        rankBing = -1
        index = 0

        if currentGoogleUrl == None or currentGoogleUrl == "":
            return 0
        for currentYahooUrl in urlsYahoo:
            if currentYahooUrl != None and currentYahooUrl != "" and \
               currentGoogleUrl.split("//")[1] == currentYahooUrl.split("//")[1]:
                rankYahoo = index
                break
            index += 1
        index = 0
        for currentBingUrl in urlsBing:
            if currentBingUrl != None and currentBingUrl != "" and \
               currentGoogleUrl.split("//")[1] == currentBingUrl.split("//")[1]:
                rankBing = index
                break
            index += 1
        if rankBing == -1 and rankYahoo == -1:
            restGoogle.append(currentGoogleUrl)
            urlsGoogle.remove(currentGoogleUrl)
            return 0
        else:
            finalData.append(DataResult(currentGoogleUrl, currentGoogleRank, rankYahoo, rankBing))
            if rankBing != -1:
                urlsBing.remove(currentBingUrl)
            if rankYahoo != -1:
                urlsYahoo.remove(currentYahooUrl)
            urlsGoogle.remove(currentGoogleUrl)
            return 0
        rankGoogle += 1

def parseYahooLink(urlsYahoo, urlsBing, currentYahooRank, \
                    restYahoo, finalData):

    if urlsYahoo == None or len(urlsYahoo) == 0:
        return 1

    for currentYahooUrl in urlsYahoo:
        rankBing = -1
        index = 0
        for currentBingUrl in urlsBing:
            if currentYahooUrl.split("//")[1] == currentBingUrl.split("//")[1]:
                rankBing = index
                break
            index += 1
        if rankBing == -1:
            restYahoo.append(currentYahooUrl)
            urlsYahoo.remove(currentYahooUrl)
            return 0
        else:
            finalData.append(DataResult(currentYahooUrl, -1, currentYahooRank, rankBing))
            if rankBing != -1:
                urlsBing.remove(currentBingUrl)
            urlsYahoo.remove(currentYahooUrl)
            return 0

def sortRank(finalUrls, classRank):
    currentRank = 1000000
    currentIndexRank = 0
    index = 0
    for currentUrl in finalUrls:
        if currentUrl.totalRank < currentRank:
            currentIndexRank = index
            currentRank = currentUrl.totalRank
        index += 1
    classRank.append(finalUrls[currentIndexRank])
    finalUrls.remove(finalUrls[currentIndexRank])

def addRestUrls(finalData, restGoogle, restYahoo, restBing):
    if restGoogle != None:
        for i in restGoogle:
            finalData.append(DataResult(i, 1, -1, -1))
    if restYahoo != None:
        for i in restYahoo:
            finalData.append(DataResult(i, -1, 1, -1))
    if restBing != None:
        for i in restBing:
            finalData.append(DataResult(i, -1, -1, 1))

def parseResponse(dataGoogle, dataYahoo, dataBing):
    finalData = []
    restGoogle = []
    restYahoo = []
    urlsGoogle = extractUrl(dataGoogle)
    urlsYahoo = extractUrl(dataYahoo)
    urlsBing = extractUrl(dataBing)
    rank = 0
    while parseGoogleLink(urlsGoogle, urlsYahoo, urlsBing, rank, restGoogle, finalData) == 0:
        rank += 1
    rank = 0
    while parseYahooLink(urlsYahoo, urlsBing, rank, restYahoo, finalData) == 0:
        rank += 1
    classRank = []
    for i in range(0, len(finalData)):
        sortRank(finalData, classRank)
    addRestUrls(classRank, restGoogle, restYahoo, urlsBing)
    pushInformationInData(classRank, dataGoogle, dataYahoo, dataBing)
    return classRank
