def add_subway_edge(network, name, stn_tuple):
    station_name, connecting_station_name, travel_time = stn_tuple
    if station_name not in network:
        network[station_name] = {}
    (network[station_name])[connecting_station_name] = { 'time': travel_time, 'line': name }
