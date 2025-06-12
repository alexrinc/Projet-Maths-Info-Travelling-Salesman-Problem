import mathplotlib as plt

def plot_path(coord, path, name):
    """
    Visualisation des chemins obtenus avec :
        coord = Liste des coordonnées
        path = Ordre des villes visités 
        name = nom de la technique utilisée
    
    """
    
    path_coords = [coord[i] for i in path] + [coord[0]]
    
    #Séparation des coordonnées x et y pour créer deux listes avec chacunes d'entre elles
    x_path, y_path = zip(*path_coords)
    
    #Visualisation du chemin obtenu
    plt.figure(figsize=(8,6))
    plt.plot(x_path, y_path, 'bo-')  #b --> couleur bleue; o --> marqueur cercle ; "-" --> relié par des lignes 
    plt.title(f"Méthode {name}")
    plt.xlabel("Coordonnée x")       #Axe des x
    plt.ylabel("Coordonnée y")       #Axe des y
    plt.grid(True)                   #Grille
    plt.show()                       #Affichage de la fenêtre