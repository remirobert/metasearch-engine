class DataResult(object):

    def __init__(self, data, rankGoogle, rankYahoo, rankBing):
        self.url = data
        self.rankGoogle = rankGoogle
        self.rankYahoo = rankYahoo
        self.rankBing = rankBing
        if rankGoogle == -1:
            rankGoogle = 1
        if rankBing == -1:
            rankBing = 1
        if rankYahoo == -1:
            rankYahoo = 1
        self.totalRank = rankGoogle + rankYahoo + rankBing
    

    def addInformation(self, title, content):
        self.title = title
        self.content = content
