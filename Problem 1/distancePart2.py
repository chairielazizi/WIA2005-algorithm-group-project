import googlemaps

import time
start_time = time.time()

gmaps = googlemaps.Client(key='AIzaSyDBQehfRCytJvvYHu4pelPuRw49m9gzYoc')

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


oriCus1 = (3.3615395462207878, 101.56318183511695)
oriCus2 = (3.049398375759954, 101.58546611160301)
oriCus3 = (3.141855957281073, 101.76158583424586)

desCus1 = (3.1000170516638885, 101.53071480907951)
desCus2 = (3.227994355250716, 101.42730357605375)
desCus3 = (2.9188704151716256, 101.65251821655471)

courierCompany = [(3.0319924887507144, 101.37344116244806), #City-link Express
                  (3.112924170027219, 101.63982650389863),  #Pos Laju
                  (3.265154613796736, 101.68024844550233),  #GDEX
                  (2.9441205329488325, 101.7901521759029),  #J&T
                  (3.2127230893650065, 101.57467295692778)]  #DHL
                  
#initilize the list
total_list1=[]
total_list2=[]
total_list3=[]

#get distance from 3 points
for z in courierCompany:
    d1 = gmaps.distance_matrix( oriCus1, z , mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    d2 = gmaps.distance_matrix( z , desCus1, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    result1 = d1/1000
    result2 = d2/1000

    total = result1 + result2
    total_list1.append(total)
    print("Delivery Hubs",z,"=",total,"km")
    
#insert quicksort to sort the list    
quickSort(total_list1, 0, len(total_list1)-1)
print(total_list1,"\n")

print("The shortest distance parcel travel from Rawang to Bukit Jelutong is",total_list1[0],"km\n\n")

for z in courierCompany:
    d1 = gmaps.distance_matrix( oriCus2, z , mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    d2 = gmaps.distance_matrix( z , desCus2, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    result1 = d1/1000
    result2 = d2/1000

    total = result1 + result2
    total_list2.append(total)
    print("Delivery Hubs",z,"=",total,"km")
quickSort(total_list2, 0, len(total_list2)-1)
print(total_list2,"\n")

print("The shortest distance parcel travel from Subang Jaya to Puncak Alam is",total_list2[0],"km\n\n")

for z in courierCompany:
    d1 = gmaps.distance_matrix( oriCus3, z , mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    d2 = gmaps.distance_matrix( z , desCus3, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    result1 = d1/1000
    result2 = d2/1000

    total = result1 + result2
    total_list3.append(total)
    print("Delivery Hubs",z,"=",total,"km")
quickSort(total_list3, 0, len(total_list3)-1)
print(total_list3,"\n")

print("The shortest distance parcel travel from Ampang to Cyberjaya is",total_list3[0],"km")

print('_'*50)
print("--- %s seconds ---" % (time.time() - start_time))

