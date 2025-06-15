### Fonction qui testera la qualité et les performances d'un algorithme TSP ###
import time

def total_path_distance(path, distance_matrix):
    path_length = 0
    for i in range(len(path) - 1):
        path_length += distance_matrix[path[i]][path[i + 1]]
    path_length += distance_matrix[path[-1]][path[0]]
    return path_length

def gap(total_path_distance, lower_bound):
    return f"{(total_path_distance - lower_bound) / lower_bound * 100} %"

def evaluate_quality(name, algo, distance_matrix, lower_bound):
    start_time = time.process_time()
    
    path = total_path_distance(algo, distance_matrix)
    print(f'Route la plus courte pour l\'algorithme " {name} " : \n{algo}')
    print(f"Longueur totale du chemin trouvé : {path}")
    print(f"Qualité de la solution par rapport à la borne inférieure (Nearest Neighbor) : {gap(path, lower_bound)} de distance en moins")
    
    end_time = time.process_time()
    print(f"Temps de calcul : {end_time} s\n")