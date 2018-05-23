import folium

map = folium.Map(location=[38.58, -99.09],zoom_start=6,tiles="Mapbox Bright")

#create feature group object to organize
fg = folium.FeatureGroup(name="My Map")
#fg.add_child(folium.Marker(location=[38.2,-99.1],popup="Hello, I am Marker", icon=folium.Icon(color="green")))
#fg.add_child(folium.Marker(location=[39.2,-100.1],popup="Hello, I am Marker", icon=folium.Icon(color="green")))

for coordinates in [[38.2,-99.1],[39.2,-100.1]]:
    fg.add_child(folium.Marker(location=coordinates,popup="Hello, I am Marker", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("map2.html")
