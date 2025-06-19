"""
PROJET MATHS-INFO
"""

### IMPORTS ###
import functions.generate as generate
import algorithms.neighbor as neighbor
import algorithms.insertion as insertion
import algorithms.twoopt as twoopt
import algorithms.annealing as annealing
import functions.visualisation as vs
import functions.quality as qc
import functions.distance as distance

### MAIN ###
distance_matrix, coords = generate.distance_matrix(50)

print("Matrice des distances entre les villes: \n")
print(distance_matrix)
print("\n")

algo1 = neighbor.nearest_neighbor(distance_matrix)
lower_bound = distance.total_path_distance(algo1, distance_matrix) # Référence pour les autres algorithmes
qc.evaluate_quality("Nearest Neighbor", algo1, distance_matrix, lower_bound)

#Copie du chemin obtenu avec Nearest Neighbor, pour TwoOpt et Simulated Annealing
path = algo1.copy()

algo2 = insertion.cheapest_insertion(distance_matrix)
qc.evaluate_quality("Cheapest Insertion", algo2, distance_matrix, lower_bound)

# Choix du chemin de Nearest Neighbor pour le calcul des deux prochaines heuristiques
algo3 = twoopt.two_opt(path, distance_matrix)
qc.evaluate_quality("2-Opt", algo3, distance_matrix, lower_bound)

# Paramètres de Simulated Annealing
initial_temperature = 5000
cooling_rate = 0.995
path = algo1.copy()
path.pop() # On enlève le dernier 0 de Nearest Neighbor pour éviter les doublons

algo4_path, algo4_length = annealing.simulated_annealing(distance_matrix, path, lower_bound, initial_temperature, 0.001, cooling_rate)
qc.evaluate_quality("Simulated Annealing", algo4_path, distance_matrix, lower_bound)

# Affichage sur la même figure des visualisations des 4 heuristiques
vs.plot_path(coords, [algo1, algo2, algo3, algo4_path], ["Nearest Neighbor", "Insertion", "Two Opt", "Simulated Annealing"])
