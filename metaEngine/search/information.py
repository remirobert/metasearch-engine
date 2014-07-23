def listDataPerRank(currentRank, dataGoogle, dataYahoo, dataBing):
    if dataGoogle != None:
        for currentData in dataGoogle:
            if len(currentData) == 3 and currentData["url"] == currentRank.url:
                currentRank.addInformation(currentData["title"], currentData["content"])
                return
    if dataYahoo != None:
        for currentData in dataYahoo:
            if len(currentData) == 3 and currentData["url"] == currentRank.url:
                currentRank.addInformation(currentData["title"], currentData["content"])
                return
    if dataBing != None:
        for currentData in dataBing:
            if len(currentData) == 3 and currentData["url"] == currentRank.url:
                currentRank.addInformation(currentData["title"], currentData["content"])
                return

def pushInformationInData(classRank, dataGoogle, dataYahoo, dataBing):
    if classRank == None:
        return
    for currentRank in classRank:
        listDataPerRank(currentRank, dataGoogle, dataYahoo, dataBing)


def cleanInformation(data):
    for currentData in data:
        if len(currentData) == 1 or currentData == None or currentData["url"] == "":
            data.remove(currentData)
