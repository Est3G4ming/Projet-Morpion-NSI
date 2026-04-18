import doctest

g = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
f = [[1, 1, 1], [1, 1, 2], [2, 1, 2]] # Grille créé pour les tests.

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
    for nombre in g[i] :
        if nombre == pion :
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

doctest.testmod()

