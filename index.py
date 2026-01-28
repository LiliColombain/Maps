import networkx as nx
import osmnx as ox
import folium


ox.settingsuse_cache = True
G = ox.graph.graph_from_point((47.63995, 6.86199), dist=750, network_type="drive")
G = ox.routing.add_edge_speeds(G, hwy_speeds=None, fallback=None, agg=numpy.mean)
G = ox.routing.add_edge_travel_times(G)

ox.io.save_graph_geopackage(G, filepath="./graph.gpkg")


orig = (47.6397, 6.8645) 

chemin = nx.Graph()

m = folium.Map(location=orig, zoom_start=14)

m.save("test_map.html")