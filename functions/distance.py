# Distance total d'un chemin
def total_path_distance(path, distance_matrix):
    path_length = 0
    for i in range(len(path) - 1):         # On cumule les distances entre les villes i et i + 1                    
        path_length += distance_matrix[path[i]][path[i + 1]]
    path_length += distance_matrix[path[-1]][path[0]]
    return path_length