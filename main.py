"""
BROUILLON : PROJET MATHS-INFO
"""

### IMPORTS ###
import neighbor

import numpy as np
from dataclasses import dataclass
import random


### Génération d'un ensemble de villes et la distance entre elles ###
## Peut être généré en faisant une matrice tel que pour la i-ème ville et j-ième ville on ait 
# [len(i,i) = 0, len(i,j), len(i,j+1) ... ]
# [len(j,i), len(j,j) = 0, len(j+1,j+1) ... ]

matrix_size = 10

@dataclass
class Ville:
    
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def distance_to(self, other: 'Ville'):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

villes = [Ville(random.randrange(0, 100), random.randrange(0, 100), i) for i in range(matrix_size)] #uniform -> randrange pour du int au lieu de float
print(villes)
print("\n")
distance_matrix = np.zeros((len(villes), len(villes)))

for i, ville1 in enumerate(villes):
    for j, ville2 in enumerate(villes):
        distance_matrix[i][j] = ville1.distance_to(ville2)


### MAIN ###
print("Matrice des distances entre les villes: \n")
print(distance_matrix)
print("\n")

algo1 = neighbor.nearest_neighbor(distance_matrix)
print(f'Route la plus courte pour l\'algorithme " Nearest Neighbor " : \n{algo1}')