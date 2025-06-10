### Nearest Neighbor ###
def nearest_neighbor(distance_matrix):
    n = len(distance_matrix)
    unvisited = set(range(n))
    current = 0
    route = [current]
    unvisited.remove(current)

    while unvisited:
        nearest = min(unvisited, key=lambda city: distance_matrix[current][city])
        route.append(nearest)
        current = nearest
        unvisited.remove(nearest)

    route.append(route[0])
    return route