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

### MAIN ###
distance_matrix, coords = generate.distance_matrix(10)

print("Matrice des distances entre les villes: \n")
print(distance_matrix)
print("\n")

algo1 = neighbor.nearest_neighbor(distance_matrix)
print(f'Route la plus courte pour l\'algorithme " Nearest Neighbor " : \n{algo1}')

algo2 = insertion.cheapest_insertion(distance_matrix)
print(f'Route la plus courte pour l\'algorithme " Insertion " : \n{algo2}')

#Choix du chemin de Nearest Neighbor pour le calcul de cette heuristique
algo3 = twoopt.two_opt(algo1.copy(), distance_matrix)
print(f'Route la plus courte pour l\'algorithme " Two Opt " : \n{algo3}')

initial_temperature = 10000
cooling_rate = 0.995
path = algo1.copy()
path.pop() # On enlève le dernier 0 de Nearest Neighbor pour éviter les doublons
algo4_tour, algo4_length = annealing.simulated_annealing(coords, path, initial_temperature, cooling_rate)
print(f'Route la plus courte pour l\'algorithme " Simulated Annealing " : \n{algo4_tour}')

#Affichage sur la même figure des visualisations des 3 heuristiques
vs.plot_path(coords, [algo1, algo2, algo3], ["Nearest Neighbor", "Insertion", "Two Opt"])