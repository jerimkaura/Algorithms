graph = {
    'A': {'B':3, 'C':4, 'D':7},
    'B': {'C':1,'F':5},
    'C': {'F':6, 'D':2},
    'D': {'E':3, 'G':6},
    'E': {'G':3, 'H':4},
    'F': {'E':1,'H':8},
    'G': {'H':2},
    'H': {'G':2}
}

def dijkstr(graph, start_node, end_node):
    # the cost to reach a given node
    shortest_distance = {}

    # track path that lead to this node
    track_predecessor = {}

    # iterate the whole graph
    unvisited = graph

    # must be grather than cummulative of the nodes
    infinity = 9999999

    #path journey to the start_node(optimal route)
    track_path = []

    for node in unvisited:
        shortest_distance[node] = infinity
    shortest_distance[start_node] = 0

    while unvisited:
        min_distance_node = None
        for node in unvisited:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node 
        path_options = graph[min_distance_node].items()

        for child_node, wieght in path_options:
            if wieght+ shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = wieght + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node
        unvisited.pop(min_distance_node)

    current_node = end_node
    while current_node != start_node:
        try:
            track_path.insert(0, current_node)
            current_node = track_predecessor[current_node]
        except KeyError:
            print("Path is not reachable")
    track_path.insert(0, start_node)

    if shortest_distance[end_node] != infinity:
        print("Shortest: "+ str(shortest_distance[end_node]))
        print("Optimal path is "+ str(track_path))

dijkstr(graph, 'A', 'H')