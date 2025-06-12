"""
BROUILLON : PROJET MATHS-INFO
"""

### IMPORTS ###
import functions.generate as generate
import algorithms.neighbor as neighbor
import algorithms.insertion as insertion

### MAIN ###
distance_matrix = generate.distance_matrix(10)

print("Matrice des distances entre les villes: \n")
print(distance_matrix)
print("\n")

algo1 = neighbor.nearest_neighbor(distance_matrix)
print(f'Route la plus courte pour l\'algorithme " Nearest Neighbor " : \n{algo1}')

algo2 = insertion.insertion_heuristique(distance_matrix)
print(f'Route la plus courte pour l\'algorithme " Insertion " : \n{algo2}')