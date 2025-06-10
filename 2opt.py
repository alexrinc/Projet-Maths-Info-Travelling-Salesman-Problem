#Code permettant de résoudre le TSP avec la méthode 2-opt
#Se basant sur des 2-permutations

def path_lenght_matrix(path):
    """
    Fonction permettant le calcul de la longueur du chemin initial
    """
    tot = 0                                #Valeur initialisée à 0
    for i in range(len(path)):
        first = path[i]
        second = path[(i+1)%len(path)]     #Format = (i+1) mod longueur du chemin car parcours cyclique
        tot += build_matrix[first][second] #Ajout à la matrice des distances
    return tot 

def two_opt(index, dist_matrix):
    """
    METHODE 2-OPT : Implémentation d'une heuristique afin de résoudre le TSP
    """
    n = len(index)
    improve = True #Initialisation du booléen d'amélioration à Vrai
    
    while improve:
        improve = False
    
        for i in range(n-1):
                for j in range(i+2, n if i>0 else n-1):     #Boucle sur les paires d'arêtes
                    a, b = index[i], index[i+1]             # a --> b
                    c, d = index[j], index[(j+1)%n]         # c --> d
                    
                    #Calcul du gain de distance
                    delta = -dist_matrix[a][b] -dist_matrix[c][d] + dist_matrix[a][c] + dist_matrix[b][d]

                    if delta < 0: #Si delta <0 alors le chemin est plus court, on procède à l'échange
                        index[i+1:j+1] = reversed(index[i+1, j+1])
                        improve = True
    return index