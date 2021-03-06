import time
start_time = time.time()
from timsort import timSort_dict, dictToListOfLists

import sys
sys.path.append("../WIA2005-algorithm-group-project/Problem 1") #point path dekat folder Problem 1
from distanceMerge import findTotalDistance
sys.path.append("../WIA2005-algorithm-group-project/Problem 2") #point path dekat folder Problem 2
import sentimentanalysis

def sorter(sentiment, distance, cust):

    def ranker(list):
        for x in range (len(list)):
            if(list[x]=='City-Link'):
                total_score['City-Link'] += (len(list)-x)
                courier_ranking['City-Link'] += (len(list)-x)
            if(list[x]=='Pos Laju'):
                total_score['Pos Laju'] += (len(list)-x)
                courier_ranking['Pos Laju'] += (len(list)-x)
            if(list[x]=='GDEX'):
                total_score['GDEX'] += (len(list)-x)
                courier_ranking['GDEX'] += (len(list)-x)
            if(list[x]=='J&T'):
                total_score['J&T'] += (len(list)-x)
                courier_ranking['J&T'] += (len(list)-x)
            if(list[x]=='DHL'):
                total_score['DHL'] += (len(list)-x)
                courier_ranking['DHL'] += (len(list)-x)

    # this part boleh implement sorting algo i think ehe
    # sort_distance = sorted(distance.items(), key=lambda x: x[1], reverse=True)
    # sort_sentiment = sorted(sentiment.items(), key=lambda x: x[1], reverse=True)
    
    distance_arr = dictToListOfLists(distance)
    sentiment_arr = dictToListOfLists(sentiment)
    sort_distance = timSort_dict(distance_arr)
    sort_sentiment = timSort_dict(sentiment_arr)

    rank_distance = []
    rank_sentiment = []

    if cust == 1:
        print("\nCourier sentiments in descending order:")
        for i in sort_sentiment:
            print(i[0], i[1])
        print('_'*50)
    
    for i in sort_sentiment:
            rank_sentiment.append(i[0])

    print("\nCourier distances in descending order for customer ",cust)
    for i in sort_distance:
        print(i[0], i[1])
        rank_distance.append(i[0])

    total_score = {  # total score - max score is 10 (5 for distance, 5 for sentiment)
    'City-Link' : 0, 
    'Pos Laju': 0, 
    'GDEX': 0, 
    'J&T': 0, 
    'DHL': 0
    }

    ranker(rank_distance)
    ranker(rank_sentiment)

    # sort_ranks = sorted(total_score.items(), key=lambda x: x[1], reverse=True)
    total_score_list = dictToListOfLists(total_score)
    sort_ranks = timSort_dict(total_score_list)

    print("\nTotal score for each courier (the higher the better):")

    for i in sort_ranks:
        print(i[0], i[1])

    print("\nThe best courier for customer",cust, "is",sort_ranks[0])
    print('_'*50)

    if cust == 3:
        total_courier_ranking = dictToListOfLists(courier_ranking)
        sort_total_ranking = timSort_dict(total_courier_ranking)
        print("\nThe total ranking score for the couriers(in descending order:")
        for i in sort_total_ranking:
            print(i[0]+":"+ str(i[1]), end="| ")
        
        print("\n\nThe best courier service among the customers is "+(sort_total_ranking[0][0])+" with a score of "+str(sort_total_ranking[0][1]))



# to find the probability of distances
def calculate(dist, sumOf):
  return (1/dist)/sumOf


def calculateSum(list):
  sumList = []
  for i in range(len(list)):
    temp = 1/(list[i])
    sumList.append(temp)
  
  return sum(sumList)


#calculate the sentiment analysis
def calculateSentiment(positive, total):
    res = positive / (total)
    return res


if __name__ == "__main__":

    distance_c1, distance_c2, distance_c3 = {}, {}, {}
    courierName = ["City-Link", "Pos Laju", "GDEX", "J&T", "DHL"]

    total1_list, total2_list, total3_list = findTotalDistance(1), findTotalDistance(2), findTotalDistance(3)

    sum_c1, sum_c2, sum_c3 = calculateSum(total1_list), calculateSum(total2_list), calculateSum(total3_list)

    for i in range(len(courierName)):
        distance_c1[courierName[i]] = calculate(total1_list[i], sum_c1)
        distance_c2[courierName[i]] = calculate(total2_list[i], sum_c2)
        distance_c3[courierName[i]] = calculate(total3_list[i], sum_c3)

    sentiment = {  # cari from question 2.
        'City-Link' : calculateSentiment(sentimentanalysis.positiveWordListCountscitylink, sentimentanalysis.wordListNoStopWordsCountscitylink), 
        'Pos Laju': calculateSentiment(sentimentanalysis.positiveWordListCountsposlaju, sentimentanalysis.wordListNoStopWordsCountsposlaju), 
        'GDEX': calculateSentiment(sentimentanalysis.positiveWordListCountsgdex, sentimentanalysis.wordListNoStopWordsCountsgdex), 
        'J&T': calculateSentiment(sentimentanalysis.positiveWordListCountsjnt, sentimentanalysis.wordListNoStopWordsCountsjnt), 
        'DHL': calculateSentiment(sentimentanalysis.positiveWordListCountsdhl, sentimentanalysis.wordListNoStopWordsCountsdhl)
        }
    """
    sentiment value = (positive word / (total filtered words))
    """

    # to do the overall ranking 
    courier_ranking = { 
        'City-Link' : 0, 
        'Pos Laju': 0, 
        'GDEX': 0, 
        'J&T': 0, 
        'DHL': 0
    }

    sorter(sentiment, distance_c1, 1)
    sorter(sentiment, distance_c2, 2)
    sorter(sentiment, distance_c3, 3)

    print("\n--- %s seconds ---" % (time.time() - start_time))