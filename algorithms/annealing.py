import math
import random

def total_distance(route, coords): # à enlever ? Redondance avec quality
    dist = 0
    for i in range(len(route)):
        ville1 = coords[route[i]]
        ville2 = coords[route[(i + 1) % len(route)]]
        dist += math.sqrt((ville1[0] - ville2[0]) ** 2 + (ville1[1] - ville2[1]) ** 2)
    return dist

def simulated_annealing(coords, path, initial_temp, cooling_rate):   
    current_path = path
    current_distance = total_distance(current_path, coords)

    best_path = current_path[:]
    best_distance = current_distance

    T = initial_temp
    max_iterations = 50000

    for iteration in range(max_iterations):
        # 2-opt
        i = random.randint(0, len(coords) - 2)
        k = random.randint(i + 1, len(coords) - 1)
        
        new_path = current_path[:i] + current_path[i:k+1][::-1] + current_path[k+1:]
        new_distance = total_distance(new_path, coords)
        delta = new_distance - current_distance
        
        # Est-ce une meilleure solution ?
        if delta < 0 or random.random() < math.exp(-delta / T):
            current_path = new_path
            current_distance = new_distance
            # Mise à jour de la meilleure solution
            if new_distance < best_distance:
                best_path = new_path
                best_distance = new_distance

        # Réduit la température.
        T *= cooling_rate
        
        """ if iteration % 1000 == 0: # Pour suivre l'avancée
            print(f"Iteration {iteration}: distance actuelle = {current_distance:.4f}, meilleure distance = {best_distance:.4f}") """

    index = best_path.index(0)                          # L'index de la ville 0
    best_path = best_path[index:] + best_path[:index]   # On réarrange le chemin pour commencer par la ville 0 (le chemin reste le même)
    best_path.append(0)                                 # Retour à la ville de départ (0)
    return best_path, best_distance

if __name__ == '__main__': # TEST
    nb_villes = 10
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(nb_villes)]
    
    # Haute température de départ pour une exploration large des solutions, refroidissement lent pour une convergence graduelle
    initial_temp = 10000
    cooling_rate = 0.995
    
    path = [0, 2, 9, 3, 7, 6, 5, 1, 4, 8]
    
    best_path, best_distance = simulated_annealing(cities, path, initial_temp, cooling_rate)
    
    print("\nBest path :")
    print(best_path)
    print(f"Total distance: {best_distance:.4f}")