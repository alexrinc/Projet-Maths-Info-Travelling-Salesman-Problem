"""
BROUILLON : PROJET MATHS-INFO
"""

### IMPORTS ###
import functions.generate as generate
import algorithms.neighbor as neighbor
import algorithms.insertion as insertion
import algorithms.twoopt as twoopt
import functions.visualisation as vs

### MAIN ###
distance_matrix, coords = generate.distance_matrix(50)

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

#Affichage sur la même figure des visualisations des 3 heuristiques
vs.plot_path(coords, [algo1, algo2, algo3], ["Nearest Neighbor", "Insertion", "Two Opt"])