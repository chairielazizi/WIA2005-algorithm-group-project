# stop words list
st = open("stopwords.txt")
stop = st.read()
stopwords = stop.split(",")

# positive words list
f = open("Positive.txt")
positive = f.read()
PositiveWord = positive.split(",")

# negative words list
g = open("Negative.txt")
negative = g.read()
NegativeWord = negative.split(",")


# turn html to text
def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text

    # remove all non-alphanumeric characters (using Unicode definition of alphanumeric).


def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)


def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(list(zip(wordlist, wordfreq)))


def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

    # remove stop words


def removeStopwords(wordlist, stopwords):
    return [w for w in wordlist if w not in stopwords]

    # return positive words


def inPositive(wordlist, PositiveWord):
    return [p for p in wordlist if p in PositiveWord]

    # return negative words


def inNegative(wordlist, NegativeWord):
    return [n for n in wordlist if n in NegativeWord]
