import math
import random

def simulated_annealing(distance_matrix, path, lower_bound, initial_temperature, final_temperature, cooling_rate):
    """
    MÉTHODE DU RECUIT SIMULÉ :
    Technique inspirée de la métallurgie acceptant temporairement des solutions moins bonnes pour éviter les minimas locaux.
    Implique l'aléatoire et une diminution de la température au fil des itérations puis se base sur le 2-opt pour la permutation des arêtes.
    """
    n = len(path)
    best_length = lower_bound
    best_path = path
    T = initial_temperature
    iteration = 0
    while T > final_temperature:
        i = random.randint(0, n-1)              # La première ville est choisie au hasard
        j = (i + random.randint(2, n-2)) % n    # La deuxième ville est également choisie au hasard et forcément différente de la première
        if j < i:
            i, j = j, i                         # j est toujours après i dans l'ordre du chemin
            
        delta = distance_matrix[path[i]][path[j]] + distance_matrix[path[i+1]][path[(j+1) % n]]\
                - distance_matrix[path[i]][path[i + 1]] - distance_matrix[path[j]][path[(j + 1) % n]] # Calcule la variation de la longueur totale du chemin s'il y a une inversion
                
        if delta < 0 or math.exp(-delta / T) > random.random():             # Si delta négatif, amélioration donc on accepte, sinon on accepte en fonction de delta et de la température
            lower_bound = lower_bound + delta
            for k in range((j - i) // 2):
                path[k + i + 1], path[j - k] = path[j - k], path[k + i + 1] # Inversion d'arête venant du 2-opt

        # Vérifie s'il y a une amélioration de la solution
        if best_length > lower_bound:
            best_length = lower_bound
            best_path = path
        iteration += 1
        if iteration % (n * n) == 0:
            T *= cooling_rate # Réduction de la température

    return best_path, best_length
