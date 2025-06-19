def nearest_neighbor(distance_matrix):
    """
    MÉTHODE DU VOISIN LE PLUS PROCHE : 
    Approche heuristique simple pour résoudre le TSP.
    Consiste tout simplement à chercher la ville la plus proche de la ville d'origine et ainsi de suite.
    
    Très rapide (mais pas du tout optimal) et permet d'offrir une base sur laquelle on peut apporter des améliorations (2-opt, simulated annealing)
    """
    n = len(distance_matrix)
    unvisited = set(range(n))   # Liste des villes non visitées
    current = 0
    path = [current]
    unvisited.remove(current)

    while unvisited:
        nearest = min(unvisited, key=lambda city: distance_matrix[current][city])   # On cherche la ville la plus proche
        path.append(nearest)                                                        # On l'ajoute au chemin final
        current = nearest
        unvisited.remove(nearest)                                                   # On enlève la ville la plus proche de unvisited

    path.append(path[0])                                                            # On ajoute la ville 0 pour compléter la boucle
    return path