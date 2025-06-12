import mathplotlib as plt

def plot_path(coord, path, name):
    """
    Visualisation des chemins obtenus avec :
        coord = Liste des coordonnées
        path = Ordre des villes visités 
        name = nom de la technique utilisée
    
    """
    
    path_coords = [coord[i] for i in path] + [coord[path[0]]]
    
    # Séparation des coordonnées x et y pour créer deux listes avec chacunes d'entre elles
    x_path, y_path = zip(*path_coords)
    
    # --- Visualisation du chemin obtenu ---
    plt.figure(figsize=(8,6))
    plt.plot(x_path, y_path, 'bo-', label ='Chemin TSP', markersize=5)  #b --> couleur bleue; o --> marqueur cercle ; "-" --> relié par des lignes 
    
    # --- Affichage des numéros de villes ---
    # On parcourt les coordonnées originales pour placer chaque numéros
    for i, (x,y) in enumerate(coord):
        #Affiche le numéro de la ville 'i' (on décale un peu pour la lisibilité)
        plt.text(x,y + 0.05, str(i), color='red', fontsize=12, ha='center')

    # Mise en évidence du point de départ
    start_city_coords = coord[path[0]]
    plt.plot(start_city_coords[0], start_city_coords[1], 'go', markersize=10, label="Ville de départ")


    # --- Mise en forme du graphique ---
    plt.title(f"Méthode {name}")
    plt.xlabel("Coordonnée x")       #Axe des x
    plt.ylabel("Coordonnée y")       #Axe des y
    plt.legend()
    plt.grid(True)                   #Grille
    plt.axis('equal')                #Evite les distorsions
    plt.show()                       #Affichage de la fenêtre