import utils
import math
from collections import deque

class SubwaySystem(object):

    def __init__(self):
        self.network = {}

    def add_train_line(self, name, stops=[], time_between_stations=[]):
        num_of_stops = len(stops)
        default_weight = 1 # For consistency, a default weight is applied when time_between_stations is not provided
        list_of_connections = []

        if len(time_between_stations) > 0:
            list_of_connections = time_between_stations[:]
            for i, stop in enumerate(time_between_stations):
                list_of_connections.append((stop[1], stop[0], stop[2]))
        else:
            for n in range(len(stops) - 1):
                list_of_connections.append((stops[n], stops[n+1], default_weight))
                list_of_connections.append((stops[n+1], stops[n], default_weight))

        for stn_tuple in list_of_connections:
            utils.add_subway_edge(network=self.network, stn_tuple=stn_tuple, name=name)

    def take_train(self, origin, destination):
        distances_map = {}
        path_map = {}
        network = self.network

        for station in network:
            distances_map[station] = math.inf

        unvisited = network.keys()
        visited = []

        # Set source to 0 distance
        distances_map[origin] = 0

        while len(visited) < len(unvisited):

            still_unvisited = [station for station in unvisited if station not in visited]
            still_in = { station: distances_map[station] for station in still_unvisited }

            # extract minimum from unvisited
            closest = min(still_in, key = distances_map.get)

            # mark station as visited
            visited.append(closest)

            for neighbour in network[closest]:
                # If current distance is greater than the distance via closest + neighbour distance
                # update distance map and add path to path_map
                if distances_map[neighbour] > distances_map[closest] + network[closest][neighbour]['time']:
                    distances_map[neighbour] = distances_map[closest] + network[closest][neighbour]['time']
                    path_map[neighbour] = closest

        path = [destination]
        while origin not in path:
            path.append(path_map[path[-1]])

        if distances_map[destination] == (len(path) - 1):
            return path[::-1]
        else:
            return (path[::-1], distances_map[destination])

    # Original implementation of take_train. Breadth-first search suitable for naive solution to challenges 1 & 2
    # def take_train(self, origin, destination):
    #     path_from_origin = {}
    #     distance_map = {}
    #     queue = deque([origin])
    #     distance_map[origin]= 0
    #     path_from_origin[origin] = [origin]
    #
    #     while len(queue) > 0:
    #         current = queue[0]
    #         queue.popleft() # Remove leftmost element from queue
    #         neighbours = self.network[current].keys()
    #         for neighbour in neighbours:
    #             if neighbour not in path_from_origin:
    #                 path_from_origin[neighbour] = path_from_origin[current] + [neighbour]
    #                 distance_map[neighbour] = distance_map[current] + self.network[current][neighbour]['time']
    #                 if neighbour == destination:
    #                     distance = distance_map[destination]
    #                     path = path_from_origin[destination]
    #                     if distance == len(path) - 1:
    #                         return path
    #                     else:
    #                         return (path, distance)
    #                 queue.append(neighbour)
    #     return False


if __name__ == "__main__":
    subway_system = SubwaySystem()
    subway_system.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1")
    subway_system.add_train_line(stops=["Spring", "West 4th", "14th", "23rd"], name="E")
    subway_system.add_train_line(stops=["Park Place", "Chambers", "14th", "34th"], name="2")
    print(subway_system.network)
