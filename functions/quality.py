### Fonction qui testera la qualité et les performances d'un algorithme TSP ###
import functions.distance as distance
import time

def gap(total_path_distance, lower_bound):
    return f"{(total_path_distance - lower_bound) / lower_bound * 100} %"

def evaluate_quality(name, algo, distance_matrix, lower_bound):
    start_time = time.process_time()
    
    path = distance.total_path_distance(algo, distance_matrix)
    print(f'Route la plus courte pour l\'algorithme " {name} " : \n{algo}')
    print(f"Longueur totale du chemin trouvé : {path}")
    print(f"Qualité de la solution par rapport à la borne inférieure (Nearest Neighbor) : {gap(path, lower_bound)} de distance en moins")
    
    end_time = time.process_time()
    print(f"Temps de calcul : {end_time} s\n")