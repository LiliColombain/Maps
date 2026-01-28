import osmnx as ox
import folium


orig = (47.6397, 6.8645) 

m = folium.Map(location=orig, zoom_start=14)

m.save("test_map.html")