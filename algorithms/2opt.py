#Code permettant de résoudre le TSP avec la méthode 2-opt
#Se basant sur des 2-permutations

def path_length_matrix(path, dist_matrix):
    """
    Calcule la longueur totale d'un chemin donné en fonction d'une matrice de distance
    """
    tot = 0                                #Valeur initialisée à 0
    for i in range(len(path)):
        first = path[i]
        second = path[(i+1)%len(path)]     #Format = (i+1) mod longueur du chemin car parcours cyclique
        tot += dist_matrix[first][second]  #Ajout de la distance entre deux villes au total
    return tot 

def two_opt(path, dist_matrix):
    """
    METHODE 2-OPT : Amélioration d'un chemin du TSP
    Prend en entrée un chemin (une liste d'indices) et une matrice de distance
    Renvoie un chemin amélioré à l'aide de 2-permutations (inversion d'arête)
    """
    n = len(path)
    improve = True #Initialisation du booléen d'amélioration à Vrai
    
    while improve:
        improve = False
    
        for i in range(n-1):
                for j in range(i+2, n if i>0 else n-1):   #Empêche les inversions invalides
                    a, b = path[i], path[i+1]             # a --> b
                    c, d = path[j], path[(j+1)%n]         # c --> d
                    
                    #Calcul du gain de distance
                    delta = -dist_matrix[a][b] -dist_matrix[c][d] + dist_matrix[a][c] + dist_matrix[b][d]

                    if delta < 0: #Si delta <0 alors le chemin est plus court, on procède à l'échange
                        path[i+1:j+1] = reversed(path[i+1:j+1])
                        improve = True
    return path