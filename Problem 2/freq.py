import urllib.request, urllib.error, urllib.parse, obo
import plotly, plotly.graph_objects as go

# article's URL
url = 'https://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'

# words without stop words
response = urllib.request.urlopen(url)
html = response.read()
text = obo.stripTags(html).lower()
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

# display word and frequency
for s in sorteddict: print(str(s))

positivewordlist = obo.inPositive(wordlist, obo.PositiveWord)
negativewordlist = obo.inNegative(wordlist, obo.NegativeWord)

# plot histogram of word frequency
for s in wordlist:
    x = [a for a in wordlist]
    y = [wordlist.count(p) for p in wordlist]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.show()

# plot histogram of positive word frequency
for s in positivewordlist:
    x = [a for a in positivewordlist]
    y = [positivewordlist.count(p) for p in positivewordlist]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.show()

# plot histogram of negative word frequency
for s in negativewordlist:
    x = [a for a in negativewordlist]
    y = [negativewordlist.count(p) for p in negativewordlist]
fig = go.Figure()
fig.add_trace(go.Histogram(histfunc="count", y=y, x=x, name="count"))
fig.show()
