import time
start_time = time.time()
import googlemaps

# to find the coordinate of the customers origin & destination
def findLocation(index):
    if index == 1:
        location = (3.3615395462207878, 101.56318183511695) # customer 1 origin

    elif index == 2:
        location = (3.049398375759954, 101.58546611160301) # customer 2 origin

    elif index == 3:
        location = (3.141855957281073, 101.76158583424586)  # customer 3 origin

    elif index == 4:
        location = (3.1000170516638885, 101.53071480907951) # customer 1 destination

    elif index == 5:
        location = (3.227994355250716, 101.42730357605375)  # customer 2 destination

    else:
        location = (2.9188704151716256, 101.65251821655471) # customer 3 destination

    return location


# to find the distance between two points
def findDistance(cust):
    gmaps = googlemaps.Client(key='AIzaSyDBQehfRCytJvvYHu4pelPuRw49m9gzYoc')

    oriCus = findLocation(cust)
    desCus = findLocation(cust+3)
    my_dist = gmaps.distance_matrix(oriCus, desCus, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    result = my_dist/1000   # to convert into km

    return result


# to find distance between three points    
def findTotalDistance(cust):
    gmaps = googlemaps.Client(key='AIzaSyDBQehfRCytJvvYHu4pelPuRw49m9gzYoc')

    courierCompany = [(3.0319924887507144, 101.37344116244806), #City-link Express
                    (3.112924170027219, 101.63982650389863),  #Pos Laju
                    (3.265154613796736, 101.68024844550233),  #GDEX
                    (2.9441205329488325, 101.7901521759029),  #J&T
                    (3.2127230893650065, 101.57467295692778)]  #DHL

    #initilize the list
    rda_list, rdb_list, total_list = [], [], []

    #get distance from 3 points
    for x in courierCompany:
        oriCus = findLocation(cust)
        desCus = findLocation(cust+3)
        da = gmaps.distance_matrix( oriCus, x, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
        db = gmaps.distance_matrix( x, desCus, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 

        rda = da/1000
        rdb = db/1000
        rda_list.append(rda)
        rdb_list.append(rdb)

        total = rda + rdb
        total_list.append(total)

    return total_list


#sorting the total_list
def partition(array, low, high):
    
    pivot = array[high]   # choose the rightmost element as pivot
    i = low - 1           # pointer for greater element
    
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)

        quickSort(array, pi + 1, high)


def printTotalDistance(list):
    courierName = ["City-Link", "Pos Laju", "GDEX", "J&T", "DHL"]

    for j in range(len(courierName)):
        print(courierName[j], ": ", list[j], " km")

    print()

 
if __name__ == '__main__':
    #display the distance  
    print("The distance between Rawang and Bukit Jelutong is",findDistance(1), "km")
    print("The distance between Subang Jaya and Puncak Alam is",findDistance(2), "km")
    print("The distance between Ampang and Cyberjaya is",findDistance(3), "km")
    print()

    total1_list, total2_list, total3_list = findTotalDistance(1), findTotalDistance(2), findTotalDistance(3)

    #display all distances and insert quicksort to sort the list   
    printTotalDistance(total1_list)
    quickSort(total1_list, 0, len(total1_list)-1)
    print(total1_list)
    print("The shortest distance parcel travel from Rawang to Bukit Jelutong is",total1_list[0],"km\n")

    printTotalDistance(total2_list)
    quickSort(total2_list, 0, len(total2_list)-1)
    print(total2_list)
    print("The shortest distance parcel travel from Subang Jaya to Puncak Alam is",total2_list[0],"km\n")

    printTotalDistance(total3_list)
    quickSort(total3_list, 0, len(total3_list)-1)
    print(total3_list)
    print("The shortest distance parcel travel from Ampang to Cyberjaya is",total3_list[0],"km\n")

    print("--- %s seconds ---" % (time.time() - start_time))
