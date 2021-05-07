import gmplot

apikey = "AIzaSyCYZRncOcdMwesgHTAr4W5_Rh_E_lqnFp8"

lat, lng = zip(*[
    #(3.0319924887507144, 101.37344116244806), #CityLinkExpress
    #(3.112924170027219, 101.63982650389863), #PosLaju
    #(3.265154613796736, 101.68024844550233),  #GDEX
    (2.9441205329488325, 101.7901521759029),  #J&T
    (3.2127230893650065, 101.57467295692778), #DHL
    (3.3615395462207878, 101.56318183511695), #Rawang
    (3.1000170516638885, 101.53071480907951), #BukitJelutong
    (3.049398375759954, 101.58546611160301), #SubangJaya
    (3.227994355250716, 101.42730357605375), #PuncakAlam
    (3.141855957281073, 101.76158583424586), #Ampang
    (2.9188704151716256, 101.65251821655471) #Cyberjaya

])

#returns map object
gmapOne = gmplot.GoogleMapPlotter(3.209247, 101.524803, 10, apikey=apikey)

#plots the points on the map
gmapOne.scatter(lat, lng, color='red', size=50)

#joins all the points
#gmapOne.plot(lat, lng, 'red', edge_width=2.5)

gmapOne.draw( "d:/SEM2.ALGORITHMdesignANAYSIS/Problem1Algo/createmap.html" )



