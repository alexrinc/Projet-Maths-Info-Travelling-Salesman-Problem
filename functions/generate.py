import numpy as np
import random

class City:
    
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

    def distance_to(self, other: 'City'):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)   # Distance euclidienne entre deux villes en fonction des coordonnées

def distance_matrix(matrix_size):
    cities = [City(random.uniform(0, 100), random.uniform(0, 100), i) for i in range(matrix_size)] # Liste contenant n villes (selon matrix_size) avec des coordonnées aléatoires
    distance_matrix = np.zeros((len(cities), len(cities)))                                         # La matrice est remplie de 0 pour l'initialiser

    for i, city1 in enumerate(cities):
        for j, city2 in enumerate(cities):
            distance_matrix[i][j] = city1.distance_to(city2)                                       # Calcule des distances entre chaques villes

    # Retour des coordonénes des villes pour la visualisation
    coords = [(v.x, v.y) for v in cities]
    
    return distance_matrix, coords