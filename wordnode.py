
class WordNode(object):
    def __init__(self, word):
        self.word = word;
        self.bWords = dict();
        self.fWords = dict();
        self.nextWord = '';
    
    def addForward(self, fWord):
        if (fWord not in self.fWords.keys()):
            self.fWords[fWord] = 1;
        else:
            self.fWords[fWord] += 1;

    def addBackward(self, bWord):
        if (bWord not in self.bWords.keys()):
            self.bWords[bWord] = 1;
        else:
            self.bWords[bWord] += 1;

    # computes forward and backward word probabilities based on history
    def getForwardDistribution(self, salt={}):
        print "Computing forward distribution for", self.word
        return self._computeDistribution(self.fWords, salt);
    def getBackwardDistribution(self, salt={}):
        print "Computing forward distribution for", self.word
        return self._computeDistribution(self.bWords, salt);
    def _computeDistribution(self, dic, salt={}):
        overall = dict(dic, **salt);
        total = float(sum(overall.values()))
        for key, val in overall.items():
            overall[key] /= total
            
    def getForwardDistributionList(self, salt={}):
        return self._computeDistributionList(self.fWords,salt)
    def getBackwardDistributionList(self, salt={}):
        return self._computeDistributionList(self.bWords,salt)    
    def _computeDistributionList(self, dic, salt={}):
        overall = dict(dic, **salt)
        l = []
        for key, val in overall.items():
            for k in range(0,val):
                l.append(key)
        return l