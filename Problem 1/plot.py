import gmplot
import requests
import polyline
from distanceMerge import findLocation, findTotalDistance, courierSorting

# to find the coordinate of the delivery hubs
def findHub(index):
    if index == 1 or index == "City-Link":
        location = (3.0319924887507144,101.37344116244806) # citylink

    elif index == 2 or index == 'Pos Laju':
        location = (3.112924170027219,101.63982650389863) # poslaju

    elif index == 3 or index == 'GDEX':
        location = (3.265154613796736,101.68024844550233)  # gdex

    elif index == 4 or index =='J&T':
        location = (2.9441205329488325,101.7901521759029) # j&t

    elif index == 5 or index == "DHL":
        location = (3.2127230893650065,101.57467295692778)  # dhl

    return location


# scatter the markers
def scatter():
	latMark, lngMark = zip(*[
		findLocation(1), findLocation(2), findLocation(3),				# origins
		findLocation(4), findLocation(5), findLocation(6),				# destinations
		findHub(1), findHub(2), findHub(3), findHub(4), findHub(5)])	# couriers

	title = ["Customer 1 Origin", "Customer 2 Origin", "Customer 3 Origin", "Customer 1 Destination", "Customer 2 Destination",
			"Customer 3 Destination", "City-Link Express", "Poslaju", "GDEX", "J&T", "DHL"]

	label = ["1", "2", "3", "1", "2", "3", "C", "P", "G", "J", "D"]

	gmap.scatter(latMark, lngMark, color="#FF0000", size=50, title=title, label=label)
	gmap.draw("Problem 1/mapInitial.html")


# choose map to draw
def draw(num):
	if num == 0:
		gmap.draw("Problem 1/map1.html")   

	elif num == 1:
		gmap.draw("Problem 1/map2.html")   

	else:
		gmap.draw("Problem 1/map3.html") 


# plot all 5 routes for each customer
def plot():
	colours = ["#008000", "#808000", "#2E8B57", "#90EE90", "#00FF00",   # customer 1
				"#00008B", "#0000CD", "#6495ED", "#87CEFA", "#1E90FF",  # customer 2
				"#C71585", "#FF69B4", "#DB7093", "#FF1493", "#FFB6C1"]  # customer 3

	k = 0   # initiate colours

	for i in range(3):

		for j in range(5):

			url = ("https://maps.googleapis.com/maps/api/directions/json?&origin=\"{}\"&destination=\"{}\"&waypoints=\"{}\"&key={}"
					).format(findLocation(i+1), findLocation(i+4), findHub(j+1), apikey)

			r = requests.get(url) 
			latPlot, lngPlot = zip(*polyline.decode(r.json()["routes"][0]["overview_polyline"]["points"]))
			gmap.plot(latPlot, lngPlot, colours[k], edge_width=7.5)         # plot routes with colours
			k = k + 1       # change colours

		draw(i)


# plot shortest route for each customer
def plotShortest():
	
	total1_list, total2_list, total3_list = findTotalDistance(1), findTotalDistance(2), findTotalDistance(3)
	total1_list, total2_list, total3_list = courierSorting(total1_list), courierSorting(total2_list), courierSorting(total3_list)
	waypoints = [findHub(total1_list[0][1]), findHub(total2_list[0][1]), findHub(total3_list[0][1])]

	colours = ["#00FF00", "#1E90FF", "#FF1493"]

	for i in range(3):

		url = ("https://maps.googleapis.com/maps/api/directions/json?&origin=\"{}\"&destination=\"{}\"&waypoints=\"{}\"&key={}"
				).format(findLocation(i+1), findLocation(i+4), waypoints[i], apikey)

		r = requests.get(url) 
		latPlot, lngPlot = zip(*polyline.decode(r.json()["routes"][0]["overview_polyline"]["points"]))
		gmap.plot(latPlot, lngPlot, colours[i], edge_width=7.5)         # plot shortest route with colour

	gmap.draw("Problem 1/mapShortest.html") 


if __name__ == "__main__":
	apikey = "AIzaSyDBQehfRCytJvvYHu4pelPuRw49m9gzYoc"

	gmap = gmplot.GoogleMapPlotter(3.104637, 101.581797, zoom=10, apikey=apikey)    # whole map before plotting

	scatter()
	plot()
	plotShortest()
