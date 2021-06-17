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

# # return positive words
# def inPositivefuvv(wordlist, PositiveWord):
#     return [p for p in wordlist if p in PositiveWord]

# # return negative words
# def inNegativefuvv(wordlist, NegativeWord):
#     return [n for n in wordlist if n in NegativeWord]

# # remove stop words
# def removeStopwordsfuvv(wordlist, stopwords):
#     return [w for w in wordlist if w not in stopwords]

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
    def find_prefix(pattern, patt_len, temp_array):
        length = 0
        temp_array[0] = 0

        for i in range(1,patt_len):
            if(pattern[i] == pattern[length]):
                length += 1
                temp_array[i] = length
            else:
                if length != 0:
                    length = temp_array[length-1]
                    i -= 1
                else:
                    temp_array[i] = 0


    def kmp(text,pattern):
        stop=[]
        for el in text:
            for pa in pattern:
                text_size = len(el)
                p_size = len(pa)
                lps = [0] * p_size

                find_prefix(pa, p_size, lps)

                i,j = 0,0
                while i < text_size:
                    if len(el) != len(pa):
                        break
                    if el[i] == pa[j]:
                        i += 1
                        j += 1
                    if j == p_size:
                        stop.append(el)
                        j = lps[j-1]
                    elif(i < text_size and pa[j] != el[i]):
                        if j != 0:
                            j = lps[j-1]
                        else:
                            i += 1
        return [w for w in text if w not in stop]

    text = wordlist
    tempStopWords = stopwords
    
    return kmp(text, tempStopWords)


def select(wordlist):
    def find_prefix(pattern, patt_len, temp_array):
        length = 0
        temp_array[0] = 0

        for i in range(1,patt_len):
            if(pattern[i] == pattern[length]):
                length += 1
                temp_array[i] = length
            else:
                if length != 0:
                    length = temp_array[length-1]
                    i -= 1
                else:
                    temp_array[i] = 0

    def kmp(text,pattern):
        word=[]
        for el in text:
            for pa in pattern:
                text_size = len(el)
                p_size = len(pa)
                lps = [0] * p_size

                find_prefix(pa, p_size, lps)

                i,j = 0,0
                while i < text_size:
                    if len(el) != len(pa):
                        break
                    if el[i] == pa[j]:
                        i += 1
                        j += 1
                    if j == p_size:
                        word.append(el)
                        j = lps[j-1]
                    elif(i < text_size and pa[j] != el[i]):
                        if j != 0:
                            j = lps[j-1]
                        else:
                            i += 1
        return [w for w in word]


    print(kmp(wordlist, PositiveWord))
    print()
    print(kmp(wordlist, NegativeWord))


# return positive words
def inPositive(wordlist,positive):
    def find_prefix(pattern, patt_len, temp_array):
        length = 0
        temp_array[0] = 0

        for i in range(1,patt_len):
            if(pattern[i] == pattern[length]):
                length += 1
                temp_array[i] = length
            else:
                if length != 0:
                    length = temp_array[length-1]
                    i -= 1
                else:
                    temp_array[i] = 0

    def kmp(text,pattern):
        word=[]
        for el in text:
            for pa in pattern:
                text_size = len(el)
                p_size = len(pa)
                lps = [0] * p_size

                find_prefix(pa, p_size, lps)

                i,j = 0,0
                while i < text_size:
                    if len(el) != len(pa):
                        break
                    if el[i] == pa[j]:
                        i += 1
                        j += 1
                    if j == p_size:
                        word.append(el)
                        j = lps[j-1]
                    elif(i < text_size and pa[j] != el[i]):
                        if j != 0:
                            j = lps[j-1]
                        else:
                            i += 1
        return [w for w in word]

    return kmp(wordlist,PositiveWord)


# return negative words
def inNegative(wordlist,negative):
    def find_prefix(pattern, patt_len, temp_array):
        length = 0
        temp_array[0] = 0

        for i in range(1,patt_len):
            if(pattern[i] == pattern[length]):
                length += 1
                temp_array[i] = length
            else:
                if length != 0:
                    length = temp_array[length-1]
                    i -= 1
                else:
                    temp_array[i] = 0

    def kmp(text,pattern):
        word=[]
        for el in text:
            for pa in pattern:
                text_size = len(el)
                p_size = len(pa)
                lps = [0] * p_size

                find_prefix(pa, p_size, lps)

                i,j = 0,0
                while i < text_size:
                    if len(el) != len(pa):
                        break
                    if el[i] == pa[j]:
                        i += 1
                        j += 1
                    if j == p_size:
                        word.append(el)
                        j = lps[j-1]
                    elif(i < text_size and pa[j] != el[i]):
                        if j != 0:
                            j = lps[j-1]
                        else:
                            i += 1
        return [w for w in word]

    return kmp(wordlist,NegativeWord)