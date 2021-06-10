import extractarticle

openArticle1dhl = open("courier_text/dhl1.txt", encoding="utf8")
openArticle2dhl = open("courier_text/dhl2.txt", encoding="utf8")
openArticle3dhl = open("courier_text/dhl3.txt", encoding="utf8")
openArticle1poslaju = open("courier_text/poslaju1.txt", encoding="utf8")
openArticle2poslaju = open("courier_text/poslaju2.txt", encoding="utf8")
openArticle3poslaju= open("courier_text/poslaju3.txt", encoding="utf8")
openArticle1jnt = open("courier_text/j&t1.txt", encoding="utf8")
openArticle2jnt = open("courier_text/j&t2.txt", encoding="utf8")
openArticle3jnt = open("courier_text/j&t3.txt", encoding="utf8")
openArticle1gdex = open("courier_text/gdex1.txt", encoding="utf8")
openArticle2gdex = open("courier_text/gdex2.txt", encoding="utf8")
openArticle3gdex = open("courier_text/gdex3.txt", encoding="utf8")
openArticle1citylink = open("courier_text/citylink1.txt", encoding="utf8")
openArticle2citylink = open("courier_text/citylink2.txt", encoding="utf8")
openArticle3citylink = open("courier_text/citylink3.txt", encoding="utf8")

readArticle1dhl = openArticle1dhl.read()
readArticle2dhl = openArticle2dhl.read()
readArticle3dhl = openArticle3dhl.read()
readArticle1poslaju = openArticle1poslaju.read()
readArticle2poslaju = openArticle2poslaju.read()
readArticle3poslaju = openArticle3poslaju.read()
readArticle1jnt = openArticle1jnt.read()
readArticle2jnt = openArticle2jnt.read()
readArticle3jnt = openArticle3jnt.read()
readArticle1gdex = openArticle1gdex.read()
readArticle2gdex = openArticle2gdex.read()
readArticle3gdex = openArticle3gdex.read()
readArticle1citylink = openArticle1citylink.read()
readArticle2citylink = openArticle2citylink.read()
readArticle3citylink = openArticle3citylink.read()

wordListdhl = readArticle1dhl.split() + readArticle2dhl.split() + readArticle3dhl.split()
wordListposlaju = readArticle1poslaju.split() + readArticle2poslaju.split() + readArticle3poslaju.split()
wordListjnt = readArticle1jnt.split() + readArticle2jnt.split() + readArticle3jnt.split()
wordListgdex = readArticle1gdex.split() + readArticle2gdex.split() + readArticle3gdex.split()
wordListcitylink = readArticle1citylink.split() + readArticle2citylink.split() + readArticle3citylink.split()

wordListNoStopWordsdhl = extractarticle.removeStopwords(wordListdhl, extractarticle.stopwords)
positiveWordListdhl = extractarticle.inPositive(wordListNoStopWordsdhl, extractarticle.PositiveWord)
negativeWordListdhl = extractarticle.inNegative(wordListNoStopWordsdhl, extractarticle.NegativeWord)
wordListNoStopWordsposlaju = extractarticle.removeStopwords(wordListposlaju, extractarticle.stopwords)
positiveWordListposlaju = extractarticle.inPositive(wordListNoStopWordsposlaju, extractarticle.PositiveWord)
negativeWordListposlaju = extractarticle.inNegative(wordListNoStopWordsposlaju, extractarticle.NegativeWord)
wordListNoStopWordsjnt = extractarticle.removeStopwords(wordListjnt, extractarticle.stopwords)
positiveWordListjnt = extractarticle.inPositive(wordListNoStopWordsjnt, extractarticle.PositiveWord)
negativeWordListjnt = extractarticle.inNegative(wordListNoStopWordsjnt, extractarticle.NegativeWord)
wordListNoStopWordsgdex = extractarticle.removeStopwords(wordListgdex, extractarticle.stopwords)
positiveWordListgdex = extractarticle.inPositive(wordListNoStopWordsgdex, extractarticle.PositiveWord)
negativeWordListgdex = extractarticle.inNegative(wordListNoStopWordsgdex, extractarticle.NegativeWord)
wordListNoStopWordscitylink = extractarticle.removeStopwords(wordListcitylink, extractarticle.stopwords)
positiveWordListcitylink = extractarticle.inPositive(wordListNoStopWordscitylink, extractarticle.PositiveWord)
negativeWordListcitylink = extractarticle.inNegative(wordListNoStopWordscitylink, extractarticle.NegativeWord)

wordListCountsdhl = len(wordListdhl)
wordListNoStopWordsCountsdhl = len(wordListNoStopWordsdhl)
positiveWordListCountsdhl = len(positiveWordListdhl)
negativeWordListCountsdhl = len(negativeWordListdhl)
wordListCountsposlaju = len(wordListposlaju)
wordListNoStopWordsCountsposlaju = len(wordListNoStopWordsposlaju)
positiveWordListCountsposlaju = len(positiveWordListposlaju)
negativeWordListCountsposlaju = len(negativeWordListposlaju)
wordListCountsjnt = len(wordListjnt)
wordListNoStopWordsCountsjnt = len(wordListNoStopWordsjnt)
positiveWordListCountsjnt = len(positiveWordListjnt)
negativeWordListCountsjnt = len(negativeWordListjnt)
wordListCountsgdex = len(wordListgdex)
wordListNoStopWordsCountsgdex = len(wordListNoStopWordsgdex)
positiveWordListCountsgdex = len(positiveWordListgdex)
negativeWordListCountsgdex = len(negativeWordListgdex)
wordListCountscitylink = len(wordListcitylink)
wordListNoStopWordsCountscitylink = len(wordListNoStopWordscitylink)
positiveWordListCountscitylink = len(positiveWordListcitylink)
negativeWordListCountscitylink = len(negativeWordListcitylink)

if __name__ == '__main__':
    print("DHL word counts with stop words:", wordListCountsdhl)
    print("DHL word counts without stop words:", wordListNoStopWordsCountsdhl)
    print("DHL positive word counts:", positiveWordListCountsdhl)
    print("DHL negative word counts:", negativeWordListCountsdhl)

    print()

    print("PosLaju word counts with stop words:", wordListCountsposlaju)
    print("PosLaju word counts without stop words:", wordListNoStopWordsCountsposlaju)
    print("PosLaju positive word counts:", positiveWordListCountsposlaju)
    print("PosLaju negative word counts:", negativeWordListCountsposlaju)

    print()

    print("J&T word counts with stop words:", wordListCountsjnt)
    print("J&T word counts without stop words:", wordListNoStopWordsCountsjnt)
    print("J&T positive word counts:", positiveWordListCountsjnt)
    print("J&T negative word counts:", negativeWordListCountsjnt)

    print()

    print("GDex word counts with stop words:", wordListCountsgdex)
    print("GDex word counts without stop words:", wordListNoStopWordsCountsgdex)
    print("GDex positive word counts:", positiveWordListCountsgdex)
    print("GDex negative word counts:", negativeWordListCountsgdex)

    print()

    print("CityLink word counts with stop words:", wordListCountscitylink)
    print("CityLink word counts without stop words:", wordListNoStopWordsCountscitylink)
    print("CityLink positive word counts:", positiveWordListCountscitylink)
    print("CityLink negative word counts:", negativeWordListCountscitylink)

    print()

    sentimentdhl = positiveWordListCountsdhl - negativeWordListCountsdhl
    if(sentimentdhl>0):
        print("DHL sentiment valued +", sentimentdhl)
    else:
        print("DHL sentiment valued -", sentimentdhl)

    sentimentposlaju = positiveWordListCountsposlaju - negativeWordListCountsposlaju
    if(sentimentposlaju>0):
        print("PosLaju sentiment valued +", sentimentposlaju)
    else:
        print("PosLaju sentiment valued -", sentimentposlaju)

    sentimentjnt = positiveWordListCountsjnt - negativeWordListCountsjnt
    if(sentimentjnt>0):
        print("J&T sentiment valued +", sentimentjnt)
    else:
        print("J&T sentiment valued -", sentimentjnt)

    sentimentgdex = positiveWordListCountsgdex - negativeWordListCountsgdex
    if(sentimentgdex>0):
        print("GDex sentiment valued +", sentimentgdex)
    else:
        print("GDex sentiment valued -", sentimentgdex)

    sentimentcitylink = positiveWordListCountscitylink - negativeWordListCountscitylink
    if(sentimentcitylink>0):
        print("CityLink sentiment valued +", sentimentcitylink)
    else:
        print("CityLink sentiment valued -", sentimentcitylink)

    print()

    a = sentimentdhl
    b = sentimentposlaju
    c = sentimentjnt
    d = sentimentgdex
    e = sentimentcitylink

    if(a > b and a > c and a > d and a > e):
        print("DHL has the highest sentiment value which is",a)
        print("Therefore, DHL is the best courier")
    elif(b > a and b > c and b > d and b > e):
        print("PosLaju has the highest sentiment value which is",b)
        print("Therefore, PosLaju is the best courier")
    elif(c > a and c > b and c > d and c > e):
        print("J&T has the highest sentiment value which is",c)
        print("Therefore, J&T is the best courier")
    elif(d > a and d > b and d > c and d > e):
        print("GDex has the highest sentiment value which is",d)
        print("Therefore, GDex is the best courier")
    else:
        print("CityLink has the highest sentiment value which is",e)
        print("Therefore, CityLink is the best courier")