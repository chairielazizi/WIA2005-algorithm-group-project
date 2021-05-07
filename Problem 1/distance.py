
import googlemaps
  
gmaps = googlemaps.Client(key='AIzaSyDBQehfRCytJvvYHu4pelPuRw49m9gzYoc')

oriCus1 = (3.3615395462207878, 101.56318183511695)
oriCus2 = (3.049398375759954, 101.58546611160301)
oriCus3 = (3.141855957281073, 101.76158583424586)

desCus1 = (3.1000170516638885, 101.53071480907951)
desCus2 = (3.227994355250716, 101.42730357605375)
desCus3 = (2.9188704151716256, 101.65251821655471)

my_dist1 = gmaps.distance_matrix( oriCus1, desCus1, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
result1 = my_dist1/1000

my_dist2 = gmaps.distance_matrix( oriCus2, desCus2, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
result2 = my_dist2/1000

my_dist3 = gmaps.distance_matrix( oriCus3, desCus3, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
result3 = my_dist3/1000

  
print("The distance between Rawang and Bukit Jelutong is",result1, "km")
print("The distance between Subang Jaya and Puncak Alam is",result2, "km")
print("The distance between Ampang and Cyberjaya is",result3, "km")
print()


courierCompany = [(3.0319924887507144, 101.37344116244806), #City-link Express
                  (3.112924170027219, 101.63982650389863),  #Pos Laju
                  (3.265154613796736, 101.68024844550233),  #GDEX
                  (2.9441205329488325, 101.7901521759029),  #J&T
                  (3.2127230893650065, 101.57467295692778)]  #DHL

rd1_list, rda_list, rdx_list = [], [], []
rd2_list, rdb_list, rdy_list = [], [], []
total1_list, total2_list, total3_list = [], [], []

print("City-link Express       Pos Laju        GDEX       J&T       DHL")
for x in courierCompany:
    d1 = gmaps.distance_matrix( oriCus1, x, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    d2 = gmaps.distance_matrix( x, desCus1, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    
    da = gmaps.distance_matrix( oriCus2, x, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    db = gmaps.distance_matrix( x, desCus2, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 

    dx = gmaps.distance_matrix( oriCus3, x, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 
    dy = gmaps.distance_matrix( x, desCus3, mode='driving')['rows'][0]['elements'][0]["distance"]["value"] 

    
    rd1 = d1/1000
    rd2 = d2/1000
    rd1_list.append(rd1)
    rd2_list.append(rd2)

    rda = da/1000
    rdb = db/1000
    rda_list.append(rda)
    rdb_list.append(rdb)

    rdx = dx/1000
    rdy = dy/1000
    rdx_list.append(rdx)
    rdy_list.append(rdy)

    #print(rd1,"km")
    total1 = rd1 + rd2
    total2 = rda + rdb
    total3 = rdx + rdy
    total1_list.append(total1)
    total2_list.append(total2)
    total3_list.append(total3)
    
#print(rd1_list)
print(total1_list,"\n",total2_list,"\n",total3_list)
print("The parcel travel from Rawang to Bukit Jelutong\nThe least distance that the parcel has to travel for Customer 1 using every courier company is",min(total1_list),"km")
print()
print("The parcel travel from Subang Jaya to Puncak Alam\nThe least distance that the parcel has to travel for Customer 1 using every courier company is",min(total2_list),"km")
print()
print("The parcel travel from Ampang to Cyberjaya\nThe least distance that the parcel has to travel for Customer 1 using every courier company is",min(total3_list),"km")

