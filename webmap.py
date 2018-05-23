pip install folium
python3
import folium
dir(folium)
help(folium.map.LegacyMap)
map = folium.Map(location=[21.148548, -86.841996] )# given in geo cordinates lat(-90 to 90) & long(-180 to 180)
#need to translate this object to browser readable
map.save("Map1.html")

#add points to map
