# stop words list
st = open("stopwords.txt")
stop = st.read()
stopwords = stop.split(",")

# positive words list
f = open("positive.txt")
positive = f.read()
PositiveWord = positive.split(",")

# negative words list
g = open("negative.txt")
negative = g.read()
NegativeWord = negative.split(",")

# return positive words
def inPositive(wordlist, PositiveWord):
    return [p for p in wordlist if p in PositiveWord]

# return negative words
def inNegative(wordlist, NegativeWord):
    return [n for n in wordlist if n in NegativeWord]

# remove stop words
def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist, wordfreq)))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux