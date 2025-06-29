import functions.distance as distance

def cheapest_insertion(distance_matrix):
    """
    METHODE D'INSERTION :
    Construit une solution approchée du TSP par heuristique d'insertion

    La fonction prend en entrée une matrice carrée des distances entre les villes et
    renvoie un ordre de visite minimisant approximativment la distance totale du chemin

    """
    n = len(distance_matrix)                             #Nombre total des villes
    unvisited = list(range(n))                           #Liste des indices des villes non inserees dans le circuit
    path = [unvisited.pop(0), unvisited.pop(0)]          #Initialisation du chemin avec les deux premières villes


    while unvisited:
        #Recherche la meilleure ville à inserer et de sa position optimale

        best_cost = float('inf')                            #Init avec la valeur infini pour la technique de borne inférieure
        best_place = None
        to_insert = None                                    #Ville à insérer lorsque celle-ci a la plus faible augmentation du coût total

        for v in unvisited:                                 #Insertion de chaque ville restantes une à une
            for i in range(len(path)):
                test_path = path[:i+1] + [v] + path[i+1:]   #Création d'un nouveau chemin hypothétique avec la ville v
                new_cost = distance.total_path_distance(test_path, distance_matrix)

                #Si l'insertion donne un cout plus optimal alors conservation en mémoire comme meilleure option
                if new_cost < best_cost:
                    best_cost = new_cost    
                    best_place = i+1
                    to_insert = v

        #Insertion de la "meilleure ville" à la "meilleure position"
        path.insert(best_place, to_insert)
        unvisited.remove(to_insert)

    path.append(path[0])  #Ajout de la première ville à la fin pour fermer le chemin
    return path





