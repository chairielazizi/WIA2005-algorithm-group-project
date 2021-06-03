import time
start_time = time.time()
MIN_MERGE = 32

"""Returns the minimum length of a
    run from 32 to 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.
 
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
def calculate_min_run(num):
    run = 0
    while (num >= MIN_MERGE):
        run |= num & 1
        num >>= 1
    return num + run


# this will be use when the array size is less than MIN_MERGE because it is much faster
# this function sorts array from left index to right index which is of size atmost RUN
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while (j > left and arr[j] > arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr, left, middle, right):
    len1 = middle - left + 1
    len2 = right - middle
    left_part = []
    right_part = []

    for i in range(0, len1):
        left_part.append(arr[left + i])
    for i in range(0, len2):
        right_part.append(arr[middle + 1 + i])

    i, j, k = 0, 0, left
    #after comparing, merge the 2 array into a larger sub array
    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    #copy remaining elements of left, if any
    while i < len1:
        arr[k] = left_part[i]
        k += 1
        i += 1
    #copy remaining elements of right, if any
    while j < len2:
        arr[k] = right_part[j]
        k += 1
        j += 1


def timSort(arr):
    num = len(arr)
    minimum_run = calculate_min_run(num)

    #sort individual subarrays of size run
    for start in range(0, num, minimum_run):
        end = min(start + minimum_run - 1, num -1)
        insertion_sort(arr, start, end)

    #start merging from size run=32,It will merge to form size 64, then 128, 256 and so on ....
    size = minimum_run
    while size < num:
        for left in range(0, num, 2 * size):
            middle = min(num-1, left + size - 1)
            right = min((left + 2 * size -1),(num - 1))

            if middle < right:
                merge(arr, left, middle, right)

        size = 2 * size
    return arr


def timSort_dict(dictionary):
    num = len(dictionary)
    minimum_run = calculate_min_run(num)

    #sort individual subarrays of size run
    for start in range(0, num, minimum_run):
        end = min(start + minimum_run - 1, num -1)
        insertion_sort_dict(dictionary, start, end)

    #start merging from size run=32,It will merge to form size 64, then 128, 256 and so on ....
    size = minimum_run
    while size < num:
        for left in range(0, num, 2 * size):
            middle = min(num-1, left + size - 1)
            right = min((left + 2 * size -1),(num - 1))

            if middle < right:
                merge(dictionary, left, middle, right)

        size = 2 * size
    return dictionary

def insertion_sort_dict(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while (j > left and arr[j][1] > arr[j - 1][1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            # print(arr[j][0])

def dictToListOfLists(dictionary:dict):
    listoftuples = list(dictionary.items())
    return ([list(i) for i in listoftuples])

def listofListstoDict(listoflists:list):
    listoftuples = [tuple(i) for i in listoflists]
    return (dict(listoftuples))

distance_c1 = {  # probability of distance for customer 1 
    'City-Link' : 0.1467310449, 
    'Pos Laju': 0.2297765471, 
    'GDEX': 0.237874979, 
    'J&T': 0.116294138, 
    'DHL': 0.269323291
    } 

# print(dictToListOfLists(distance_c1))
test1 = dictToListOfLists(distance_c1)

import random
if __name__ == "__main__":

    print("Unsorted list")
    print(test1)

    timSort_dict(test1)
    print("\nSorted List:")
    print(test1)
    print(listofListstoDict(test1))

    print("--- %s seconds ---" % (time.time() - start_time))