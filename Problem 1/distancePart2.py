import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDBQehfRCytJvvYHu4pelPuRw49m9gzYoc')


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
                  

total_list=[]
for z in courierCompany:
    d1 = gmaps.distance_matrix( oriCus1, z , mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    d2 = gmaps.distance_matrix( z , desCus1, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    result1 = d1/1000
    result2 = d2/1000

    total = result1 + result2
    total_list.append(total)
    print("Delivery Hubs",z,"=",total,"km")
print("The shortest distance parcel travel from Rawang to Bukit Jelutong is",min(total_list),"km\n\n")

for z in courierCompany:
    d1 = gmaps.distance_matrix( oriCus2, z , mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    d2 = gmaps.distance_matrix( z , desCus2, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    result1 = d1/1000
    result2 = d2/1000

    total = result1 + result2
    total_list.append(total)
    print("Delivery Hubs",z,"=",total,"km")
print("The shortest distance parcel travel from Subang Jaya to Puncak Alam is",min(total_list),"km\n\n")

for z in courierCompany:
    d1 = gmaps.distance_matrix( oriCus3, z , mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    d2 = gmaps.distance_matrix( z , desCus3, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    result1 = d1/1000
    result2 = d2/1000

    total = result1 + result2
    total_list.append(total)
    print("Delivery Hubs",z,"=",total,"km")
print("The shortest distance parcel travel from Ampang to Cyberjaya is",min(total_list),"km")


