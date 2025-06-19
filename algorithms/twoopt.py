#Code permettant de résoudre le TSP avec la méthode 2-opt
#Se basant sur des 2-permutations

def two_opt(path, distance_matrix):
    """
    METHODE 2-OPT : Amélioration d'un chemin du TSP
    Prend en entrée un chemin (une liste d'indices) et une matrice de distance
    Renvoie un chemin amélioré à l'aide de 2-permutations (inversion d'arête)
    """
    n = len(path)
    improve = True              #Initialisation du booléen d'amélioration à Vrai

    max_iterations = 1000       #Maximum d'itération avant arrêt de l'algorithme
    iteration = 0               #Comptage d'itération

    while improve and iteration < max_iterations:         #Evite que le calcul ne boucle trop longtemps lorsque la solution initiale n'est pas du tout optimale
        improve = False
        iteration += 1
    
        for i in range(n-1):
                for j in range(i+2, n if i>0 else n-1):   #Empêche les inversions invalides
                    a, b = path[i], path[i+1]             # a --> b
                    c, d = path[j], path[(j+1)%n]         # c --> d
                    
                    #Calcul du gain de distance
                    delta = -distance_matrix[a][b] -distance_matrix[c][d] + distance_matrix[a][c] + distance_matrix[b][d]

                    if delta < 0 :                       #Si delta est négatif, il y a un gain donc on procède à l'échange des arêtes
                        path[i+1:j+1] = reversed(path[i+1:j+1])
                        improve = True

        if iteration >= max_iterations :                 #Condition permettant d'éviter de rallonger le calcul lorsque la solution initale n'est pas du tout optimale 
             print(f"Avertissement : Arret apres {iteration} iterations, limite maximum\n")
    return path