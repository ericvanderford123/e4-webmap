import folium
dir(folium)
map = folium.Map(location=(35.61,-82.44), zoom_start = 10)
map.save('map1.html')


