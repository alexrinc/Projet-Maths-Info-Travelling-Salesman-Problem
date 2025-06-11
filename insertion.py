### IMPORTS ###

import math

def calcul_du_cout(chemin, matrice):
    """ 
    Calcule la longueur totale d'un chemin fermé donc retour à la ville de départ
    à partir d'un chemin donné et d'une matrice de distance

    """
    return sum(matrice[chemin[i]][chemin[(i + 1) % len(chemin)]] for i in range(len(chemin)))


def insertion_heuristique(matrice_villes):
    """
    METHODE D'INSERTION : 
    Construit une solution approchée du TSP par heuristique d'insertion

    La fonction prend en entrée une matrice carrée des distances entre les villes et
    renvoie un ordre de visite minimisant approximativment la distance totale du chemin

    """
    n = len(matrice_villes)                                 #Nombre total des villes
    non_visitees = list(range(n))                           #Liste des idices des villes non inserees dans le circuit
    chemin = [non_visitees.pop(0), non_visitees.pop(0)]     #Initialisation du chemin avec les deux premières villes


    while non_visitees:
        #Recherhce la meilleure ville à inserer et de sa position optimale

        meilleur_cout = float('inf')                            #Init avec la valeur infini pour technique borne inférieur
        meilleure_position = None
        ville_ainserer = None

        for v in non_visitees:                                  #Insertion de chaque ville restantes une à une
            for i in range(len(chemin)):
                test_chemin = chemin[:i+1] + [v] + chemin[i+1:] #Création d'un nouveau chemin hypothétique ave la ville v
                nouveau_cout = calcul_du_cout(test_chemin, matrice_villes)

                #Si l'insertion donne un meilleur cout alors on la garde en mémoire comme meilleure option
                if nouveau_cout < meilleur_cout:
                    meilleur_cout = nouveau_cout    
                    meilleure_position = i+1
                    ville_ainserer = v

        #Insertion de la meilleure ville à la meilleure position
        chemin.insert(meilleure_position, ville_ainserer)
        non_visitees.remove(ville_ainserer)

    return chemin





