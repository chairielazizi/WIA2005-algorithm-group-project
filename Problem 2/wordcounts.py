import extractarticle

openArticle = open("courier_text/citylink1.txt")
readArticle = openArticle.read()
wordList = readArticle.split()

wordListNoStopWords = extractarticle.removeStopwords(wordList, extractarticle.stopwords)
positiveWordList = extractarticle.inPositive(wordListNoStopWords, extractarticle.PositiveWord)
negativeWordList = extractarticle.inNegative(wordListNoStopWords, extractarticle.NegativeWord)
dictionary = extractarticle.wordListToFreqDict(wordListNoStopWords)
sorteddict = extractarticle.sortFreqDict(dictionary)

wordListCounts = len(wordList)
wordListNoStopWordsCounts = len(wordListNoStopWords)
positiveWordListCounts = len(positiveWordList)
negativeWordListCounts = len(negativeWordList)

sentiment = positiveWordListCounts - negativeWordListCounts
if(sentiment>0):
    print("Sentiment valued +", sentiment)
else:
    print("Sentiment valued ", sentiment)

print("Word counts with stop words:", wordListCounts)
print("Word counts without stop words:", wordListNoStopWordsCounts)
print("Positive word counts:", positiveWordListCounts)
print("Negative word counts:", negativeWordListCounts)

# display word and frequency
print("Words and its count:")
for t in sorteddict: print(str(t))

