import gmplot
import requests
import json
import polyline

apikey = "insert_apikey_here"

gmap = gmplot.GoogleMapPlotter(3.104637, 101.581797, zoom=10, apikey=apikey)    # whole map before plotting

# scatter the markers
latMark, lngMark = zip(*[(3.3615395462207878, 101.56318183511695), (3.1000170516638885, 101.53071480907951),    # customer 1
                        (3.049398375759954, 101.58546611160301), (3.227994355250716, 101.42730357605375),       # customer 2
                        (3.141855957281073, 101.76158583424586), (2.9188704151716256, 101.65251821655471),      # customer 3
                        (3.0319924887507144, 101.37344116244806), (3.112924170027219, 101.63982650389863), (3.265154613796736, 101.68024844550233),     #courier
                        (2.9441205329488325, 101.7901521759029), (3.2127230893650065, 101.57467295692778)])     #courier

title = ["Customer 1 Origin", "Customer 1 Destination", "Customer 2 Origin", "Customer 2 Destination", "Customer 3 Origin", "Customer 3 Destination",
                "City-Link Express", "Poslaju", "GDEX", "J&T", "DHL"]

label = ["1", "1", "2", "2", "3", "3", "C", "P", "G", "J", "D"]

gmap.scatter(latMark, lngMark, color="#FF0000", size=50, title=title, label=label)

# plot shortest route for each customer
origin = ["3.3615395462207878,101.56318183511695", "3.049398375759954,101.58546611160301", "3.141855957281073,101.76158583424586"]

destination = ["3.1000170516638885,101.53071480907951", "3.227994355250716,101.42730357605375", "2.9188704151716256,101.65251821655471"]

waypoints = ["3.2127230893650065,101.57467295692778", "3.2127230893650065,101.57467295692778", "2.9441205329488325,101.7901521759029"]

colours = ["#00FF00", "#1E90FF", "#FF1493"]

for i in range(len(origin)):

        url = ("https://maps.googleapis.com/maps/api/directions/json?&origin={}&destination={}&waypoints={}&key={}"
                ).format(origin[i], destination[i], waypoints[i], apikey)

        r = requests.get(url) 
        latPlot, lngPlot = zip(*polyline.decode(r.json()["routes"][0]["overview_polyline"]["points"]))
        gmap.plot(latPlot, lngPlot, colours[i], edge_width=7.5)         # plot shortest route with colour

gmap.draw("Problem 1/mapShortest.html")   # whole map after plotting