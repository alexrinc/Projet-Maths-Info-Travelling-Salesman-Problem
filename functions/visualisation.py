import matplotlib.pyplot as plt

def plot_path(coord, paths, names):
    """
    Visualisation des chemins obtenus avec :
        coord = Liste des coordonnées
        path = Ordre des villes visités 
        name = nom de la technique utilisée
    
    """
    fig, axis = plt.subplots(1, len(paths), figsize=(5 * len(paths), 6))
    
    if len(paths) == 1: #Si un seul chemin: objet unique, non une liste
        axis = [axis]

    for ax, path, name in zip(axis, paths, names):
        path_coords = [coord[i] for i in path] + [coord[path[0]]]
        
        # Séparation des coordonnées x et y pour créer deux listes avec chacunes d'entre elles
        x_path, y_path = zip(*path_coords)
        
        # --- VISUALISATION DU CHEMIN OBTENU ---
        #plt.figure(figsize=(8,6))
        ax.plot(x_path, y_path, 'ro-', label ='Chemin TSP', markersize=5) #r --> rouge ; o --> marqueur cercle ; "-" --> relié par des lignes 
        
        # --- AFFICHAGE DES NUMEROS DE VILLES --
        # On parcourt les coordonnées originales pour placer chaque numéros
        for i, (x,y) in enumerate(coord):
            #Affiche le numéro de la ville 'i' (on décale un peu pour la lisibilité)
            ax.text(x,y + 0.05, str(i), color='blue', fontsize=12, ha='center') 

        # Mise en évidence du point de départ
        start_city_coords = coord[path[0]]
        ax.plot(start_city_coords[0], start_city_coords[1], 'go', markersize=10, label="Ville de départ") #g --> vert ; o --> marqueur cercle


        # --- MISE EN FORME DU GRAPHIQUE ---
        ax.set_title(f"Méthode {name}")
        ax.set_xlabel("Coordonnée x")       #Axe des x
        ax.set_ylabel("Coordonnée y")       #Axe des y
        ax.legend()
        ax.grid(True)                       #Grille pour permettre une meilleure représentation des chemins
        ax.axis('equal')                    #Evite les distorsions des axes x et y 
    
    plt.tight_layout()
    plt.show()                              #Affichage de la fenêtre