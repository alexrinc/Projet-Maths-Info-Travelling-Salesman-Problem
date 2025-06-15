"""
BROUILLON : PROJET MATHS-INFO
"""

### IMPORTS ###
import functions.generate as generate
import algorithms.neighbor as neighbor
import algorithms.insertion as insertion
import algorithms.twoopt as twoopt
import algorithms.annealing as annealing
import functions.visualisation as vs
import functions.quality as qc

### MAIN ###
distance_matrix, coords = generate.distance_matrix(50)

print("Matrice des distances entre les villes: \n")
print(distance_matrix)
print("\n")

algo1 = neighbor.nearest_neighbor(distance_matrix)
lower_bound = qc.total_path_distance(algo1, distance_matrix) # Référence pour les autres algorithmes
qc.evaluate_quality("Nearest Neighbor", algo1, distance_matrix, lower_bound)

algo2 = insertion.cheapest_insertion(distance_matrix)
qc.evaluate_quality("Cheapest Insertion", algo2, distance_matrix, lower_bound)

# Choix du chemin de Nearest Neighbor pour le calcul des deux prochaines heuristiques
algo3 = twoopt.two_opt(algo1.copy(), distance_matrix)
qc.evaluate_quality("2-Opt", algo3, distance_matrix, lower_bound)

# Paramètres de Simulated Annealing
initial_temperature = 10000
cooling_rate = 0.995
path = algo1.copy()

path.pop() # On enlève le dernier 0 de Nearest Neighbor pour éviter les doublons

algo4_path, algo4_length = annealing.simulated_annealing(coords, path, initial_temperature, cooling_rate)
qc.evaluate_quality("Simulated Annealing", algo4_path, distance_matrix, lower_bound)

# Affichage sur la même figure des visualisations des 3 heuristiques
vs.plot_path(coords, [algo1, algo2, algo3], ["Nearest Neighbor", "Insertion", "Two Opt"])
