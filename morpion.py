import doctest
import copy

g = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
f = [[1, 1, 1], [1, 1, 2], [2, 1, 2]] # Grille créé pour les tests.

def affiche(g : list) -> None :
    """
    Affiche la grille du morpion sous forme de lignes et de colonnes :
    -> Entrée : Une liste g qui est la grille du morpion.
    -> Sortie : Renvoyant None et affichant la grille du morpion sous forme de lignes et de colonnes : None

    Tests avec des entiers :
    >>> affiche(f)
    1 | 1 | 1
    1 | 1 | 2
    2 | 1 | 2
    <BLANKLINE>
    >>> affiche(g)
    0 | 0 | 0
    0 | 0 | 0
    0 | 0 | 0
    <BLANKLINE>
    """
    for i in range(len(g)) :
        print(f"{g[i][0]} | {g[i][1]} | {g[i][2]}") # Affiche la ligne i de la grille g en séparant les éléments par des " | ".
    print()
    return None

def ligne(i : int, g : list) -> list :
    """
    Renvoie la ligne i de la grille g :
    -> Entrée : Une variable i pour la ligne : int et une liste g qui est la grille.
    -> Sortie : Renvoyant la ligne i de la grille g : list
    
    Tests avec des entiers :
    >>> ligne(1,f)
    [1, 1, 2]
    >>> ligne(0,g)
    [1, 0, 0]
    
    """
    return g[i] # Renvoyant la ligne i de la grille g.

def colonne(j : int, g : list) -> list :
    """
    Renvoie la colonne j de la grille g :
    -> Entrée : Une variable j pour la colonne : int et une liste g qui est la grille.
    -> Sortie : Renvoyant la colonne j de la grille g : list
    
    Tests avec des entiers :
    >>> colonne(1,f)
    [1, 1, 1]
    >>> colonne(0,g)
    [0, 0, 0]
    """
    colonne = []
    for i in range(len(g)) :
        colonne.append(g[i][j]) # Ajoute à la liste colonne l'élément de la ligne i et de la colonne j de la grille g.
    return colonne

def diagPrincipale(g : list) -> list :
    """
    Renvoie la liste de tous les éléments de la diagonale principale :
    -> Entrée : Aucun paramètre en entrée.
    -> Sortie : Renvoyant la liste de tous les éléments de la diagonale principale : list

    Tests avec des entiers :
    >>> diagPrincipale(f)
    [1, 1, 2]
    >>> diagPrincipale(g)
    [0, 0, 0]
    """
    diag = []
    j = 0
    for i in range(len(g)) :
        diag.append(g[i][j]) # Ajoute à la liste diag l'élément de la ligne i et de la colonne j de la grille g.
        j += 1
    return diag

def diagSecondaire(g : list) -> list :
    """
    Renvoie la liste de tous les éléments de la diagonale secondaire :
    -> Entrée : Aucun paramètre en entrée.
    -> Sortie : Renvoyant la liste de tous les éléments de la diagonale secondaire : list
    Tests avec des entiers :
    >>> diagSecondaire(f)
    [1, 1, 2]
    >>> diagSecondaire(g)
    [0, 0, 0]
    """
    diag = []
    j = len(g) - 1
    for i in range(len(g)) :
        diag.append(g[i][j]) # Ajoute à la liste diag l'élément de la ligne i et de la colonne j de la grille g.
        j -= 1
    return diag

def joue(joueur : int, i : int, j : int) -> None :

    """
    Place la valeur correspondante au joueur dans la grille g, au point de coordonnées (i,j) :
    -> Entrée : Une variable joueur qui représente le numéro du joueur qui joue : int et une variable i pour la ligne : int et une variable j pour la colonne : int.
    -> Sortie : Renvoie None et place la valeur correspondante au joueur dans la grille g, au point de coordonnées (i,j) : None

    Tests avec des entiers :
    >>> joue(1,0,0)
    >>> affiche(g)
    1 | 0 | 0
    0 | 0 | 0
    0 | 0 | 0
    <BLANKLINE>
    >>> joue(2,1,1)
    >>> affiche(g)
    1 | 0 | 0
    0 | 2 | 0
    0 | 0 | 0
    <BLANKLINE>

    """

    g[i][j] = joueur # Place la valeur correspondante au joueur dans la grille g, au point de coordonnées (i,j).
    return None


def nbPionDansLigne(pion : int, i : int, g : list) -> int :

    """
    Compte le nombre de pion qu'il y a dans une ligne :
    -> Entrée : Une variable 'pion' : La ligne représentant int et une variable i et la grille représentant int et une liste g.
    -> Sortie : Renvoyant le nombre d'occurrences de pion à la ligne i : int

    Tests avec des entiers :
    >>> nbPionDansLigne(1,1,f) 
    2
    >>> nbPionDansLigne(2,0,f)
    0
    """
    
    compteur = 0
    for j in range(len(g)) :
        if g[i][j] == pion :
            compteur += 1
    return compteur

def nbPionDansColonne(pion : int, j : int, g : list) -> int :
    """
    Compte le nombre de pion qu'il y a dans une colonne :
    -> Entrée : Une variable 'pion' : La colonne représentant int et une variable j et la grille représentant int et une liste g. 
    -> Sortie : Renvoyant le nombre d'occurrences de pion à la colonne j : int

    Tests avec des entiers :
    >>> nbPionDansColonne(2,1,f) 
    0
    >>> nbPionDansColonne(1,0,f)
    2

    """
    compteur = 0
    for i in range(len(g)) :
        if g[i][j] == pion :
            compteur += 1
    return compteur

def nbPionDiagPrincipale(pion : int, g : list) -> int :
    """
    Compte le nombre de pion qu'il y a dans une diagonale principale :
    -> Entrée : Une variable 'pion' : La diagonale principale représentant int et une liste g qui est la grille.
    -> Sortie : Renvoyant le nombre d'occurrences de pion à la diagonale principale : int

    Tests avec des entiers :
    >>> nbPionDiagPrincipale(1,f) 
    2
    >>> nbPionDiagPrincipale(2,f)
    1

    """
    compteur = 0
    j = 0
    for i in range(len(g)) :
        if g[i][j] == pion :
            compteur += 1
        j += 1
    return compteur

def nbPionDiagSecondaire(pion : int, g : list) -> int:
    """
    Compte le nombre de pion qu'il y a dans une diagonale secondaire :
    -> Entrée : Une variable 'pion' : La diagonale secondaire représentant int et une liste g qui est la grille.
    -> Sortie : Renvoyant le nombre d'occurrences de pion à la diagonale secondaire : int

    Tests avec des entiers :
    >>> nbPionDiagSecondaire(1,f) 
    2
    >>> nbPionDiagSecondaire(2,f)
    1

    """
    compteur = 0
    j = len(g) - 1
    for i in range(len(g)) :
        if g[i][j] == pion :
            compteur += 1
        j -= 1
    return compteur

def gagne(pion : int, g : list) -> bool:
    """
    Renvoie True si il y a un gagnant ou False sinon :
    -> Entrée : Une variable 'pion' : Le joueur qui joue représentant int et une liste g qui est la grille.
    -> Sortie : Renvoyant un booléen : True si il y a un gagnant ou False sinon : bool

    Tests avec des entiers :
    >>> gagne(1,f) 
    True
    >>> gagne(2,f)
    False

    """
    for i in range(len(g)) :
        if nbPionDansLigne(pion,i,g) == 3 :
            return True
    for j in range(len(g)):
        if nbPionDansColonne(pion,j,g) == 3 :
            return True
    if nbPionDiagPrincipale(pion,g) == 3 :
        return True
    elif nbPionDiagSecondaire(pion,g) == 3 :
        return True
    return False

def estSurDiagPrincipale( i : int, j : int, g : list) -> bool :

    """
    Renvoie True si la cellule (i,j) appartient à la diagonale principale et False sinon :
    -> Entrée : Une variable i pour la ligne : int et une variable j pour la colonne : int et une liste g qui est la grille.
    -> Sortie : Renvoyant un booléen : True si la cellule appartient à la diagonale principale et False sinon : bool

    Tests avec des entiers :
    >>> estSurDiagPrincipale(1,1,f) 
    True
    >>> estSurDiagPrincipale(1,0,f)
    False

    """
    if i == j : # Si la ligne et la colonne sont égales, alors la cellule appartient à la diagonale principale.
        return True
    return False

def estSurDiagSecondaire(i : int, j : int, g : list) -> bool :
    """
    Renvoie True si la cellule (i,j) appartient à la diagonale secondaire et False sinon :
    -> Entrée : Une variable i pour la ligne : int et une variable j pour la colonne : int et une liste g qui est la grille.
    -> Sortie : Renvoyant un booléen : True si la cellule appartient à la diagonale secondaire et False sinon : bool

    Tests avec des entiers :
    >>> estSurDiagSecondaire(1,1,f) 
    True
    >>> estSurDiagSecondaire(0,0,f)
    False

    """
    x = 1
    for k in range(len(g)) :
        if (i,j) == (k, len(g)-x) : 
            return True
        x += 1
    return False
def coupsPossibles() -> list:
    """
    Renvoie les cases vides de la grille
    -> Sortie : coups qui représente une liste de tuple des coups possibles
    """
    global g
    coups = []
    for y in range(len(g)):
        for x in range(len(g[y])):
            if g[y][x] == 0:
                coups.append((y, x))
    return coups

def evaluation() -> int:
    """
    Renvoie le résultat de la partie
    -> Sortie : entier représentant l'issue de la partie
    """
    global g
    # Si l'ordinateur gagne
    if gagne(2, g):
        return 1
    # Si le joueur gagne
    if gagne(1, g):
        return -1
    # Si aucune victoire
    return 0

def minimax(joueur:int, tour:int=0) -> list:
    """
    Renvoie la valeur du coup joué à l'IA  en fonction de qui joue
    -> Entrée : joueur -> Entier qui représente qui joue le coup; tour -> entier qui représente le nombre de tour en cour du coup joue
    -> Sortie : meilleur_coup -> liste qui représente la valeur du coup joué et le nombre de tour pour l'atteindre
    """
    global g
    if coupsPossibles() == [] or gagne(1, g) or gagne(2, g) or tour >=2:
        return [evaluation(), tour]
    
    tour += 1

    gfactice = copy.deepcopy(g)
    if joueur == 2:
        meilleur_coup = [-2, 10]
        for coup in coupsPossibles():
            g = copy.deepcopy(gfactice)
            joue(2, coup[0], coup[1])
            coup_joue = minimax(1, tour)
            if meilleur_coup[0] < coup_joue[0]:
                meilleur_coup = coup_joue
        g = copy.deepcopy(gfactice)
        return meilleur_coup
    
    if joueur == 1:
        gfactice = copy.deepcopy(g)
        meilleur_coup = [2, 10]
        for coup in coupsPossibles():
            g = copy.deepcopy(gfactice)
            joue(1, coup[0], coup[1])
            coup_joue = minimax(2, tour)
            if meilleur_coup[0] > coup_joue[0]:
                meilleur_coup = coup_joue
        g = copy.deepcopy(gfactice)
        return meilleur_coup

def meilleurCoupIA() -> tuple:
    """
    Renvoie la position du meilleur coup à l'IA
    Sortie : meilleur_coup : tuple de la position du meilleur coup pour l'IA
    """
    global g
    gfactice = copy.deepcopy(g)
    meilleur_coup = [(-1, -1), -10, 10]
    for coup in coupsPossibles():
        g = copy.deepcopy(gfactice)
        joue(2, coup[0], coup[1])
        coup_valeur = minimax(1)
        if coup_valeur[0] > meilleur_coup[1] or (coup_valeur[0] == meilleur_coup[1] and coup_valeur[1] < meilleur_coup[2]):
            meilleur_coup[1] = coup_valeur[0]
            meilleur_coup[2] = coup_valeur[1]
            meilleur_coup[0] = coup
    g = copy.deepcopy(gfactice)
    print("coup joue par IA : " + str(meilleur_coup))
    return meilleur_coup[0]

def partie() -> None:
    """
    Gère le déroulé d'une partie
    """
    global g
    print("=== Morpion IA (Minimax) ===")
    affiche(g)
    Humain = True
    while coupsPossibles() != []:
        if Humain == True:
            print("Votre tour ! (X)")
            x = int(input("Colonne (0..2) : "))
            y = int(input("Ligne (0..2) : "))
            while (y,x) not in coupsPossibles():
                print("Emplacement non disponible\nRéessayer")
                x = int(input("Colonne (0..2) : "))
                y = int(input("Ligne (0..2) : "))
            joue(1, y, x)
        else:
            print("Tour de l'IA (O)...")
            meilleur_coup = meilleurCoupIA()
            print(meilleur_coup)
            joue(2, meilleur_coup[0], meilleur_coup[1])
        affiche(g)
        Humain = not Humain

        print(coupsPossibles())
        if gagne(1, g):
            print("Vous Avez Gagné !")
            return
        if gagne(2, g):
            print("L'IA a Gagné !")
            return
    print("Match nul !")

        

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
    # Tests supplémentaires de la fonction joue()
    # Note : Réinitialiser g pour les tests après les doctests
    g = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert joue(1,0,0) == None
    assert g == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert joue(2,1,1) == None
    assert g == [[1, 0, 0], [0, 2, 0], [0, 0, 0]]

    # Test de la fonction coupsPossibles()
    g = [[1,1,2],[2,0,1],[0,2,1]]
    assert coupsPossibles() == [(1, 1), (2, 0)]
    g = [[1,1,2],[2,1,1],[1,2,1]]
    assert coupsPossibles() == []
    #--------------------------------#

    # Test de la fonction evaluation()
    g=[[1,1,1],[2,2,0],[0,0,0]]
    assert evaluation() == -1
    g=[[1,1,0],[2,2,2],[0,0,0]]
    assert evaluation() == 1
    g=[[1,1,2],[2,2,1],[1,2,1]]
    assert evaluation() == 0
    #--------------------------------#

    # --- Test de la fonction minimax() ---

    # Grille vide -> evaluation() = 0
    g = [[0,0,0],[0,0,0],[0,0,0]]
    assert minimax(2) == [0, 2]
    
    # L'IA (2) a déjà gagné -> evaluation() = 1
    g = [[2,2,2],[1,1,0],[0,0,0]]
    assert minimax(2) == [1, 0]
    
    # Le joueur (1) a déjà gagné -> evaluation() = -1
    g = [[1,1,1],[2,2,0],[0,0,0]]
    assert minimax(1) == [-1, 0]
    #--------------------------------#

    # --- Tests de meilleurCoupIA() ---
    
    # IA victoire en ligne
    assert gagne(2, [[1,0,0],[2,2,2],[0,0,0]]) == True
    g = [[1,0,0],[2,0,2],[0,0,0]]
    print(meilleurCoupIA())
    assert meilleurCoupIA() == (1, 1)

    # IA victoire en diagonale
    g = [[2,0,0],[0,2,0],[0,0,0]]
    assert meilleurCoupIA() == (2, 2)

    # IA bloque le joueur
    g = [[0,1,0],[0,0,0],[0,1,0]]
    print(meilleurCoupIA())
    assert meilleurCoupIA() == (1, 1)
    #--------------------------------#


g = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

partie()
