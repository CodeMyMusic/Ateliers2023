import numpy as np

def matriceAdjacences(S: list, A: [(float, float)])-> object:
    """Retourne la matrice d'adjacence associée à une liste S de
    sommets et une liste A d'arcs

    Args:
        S (list): liste de sommets
        A (float, float): liste d'arcs (liste typles (i, j))

    Returns:
        object: la matrice d'adjacence associée (array 2d)
    """
    len_S = len(S)
    # la matrice est carrée et sa taille représente le nombre de sommets
    matrice_adj = np.zeros([len_S, len_S], int)
    for depart, arrivee in A:
        # le départ se lit par le numéro de la ligne et l'arrivée par le
        # numéro de la colonne
        matrice_adj[depart][arrivee] = 1
    return matrice_adj

def matriceAdjacencePond(S: list, A: (float, float, float))-> object:
    """Retourne la matrice d'adjacence associée à une liste S de
    sommets et une liste A d'arcs pondérées

    Args:
        S (list): liste de sommets
        A (float, float): liste d'arcs pondérés (triplets (i, j, poids))

    Returns:
        object: la matrice d'adjacence associée (array 2d)
    """
    len_S = len(S)
    # la matrice est carrée et sa taille représente le nombre de sommets
    matrice_adj = np.zeros([len_S, len_S], float)
    for depart, arrivee, poids in A:
        # le départ se lit par le numéro de la ligne et l'arrivée par le
        # numéro de la colonne
        matrice_adj[depart][arrivee] = poids
    return matrice_adj

# TESTS
mat_adj = matriceAdjacences([0, 1, 2, 3, 4], [(0,1), (0, 2), (1,2), (1, 4), (2, 3), (3, 4), (4, 2)])
print(mat_adj)
mat_adj_pond = matriceAdjacencePond([0, 1, 2, 3, 4], [(0,1, 15), (0, 2, 10), (1,2, 4), (1, 4, 8), (2, 3, 23), (3, 4, 12), (4, 2, 11)])
print(mat_adj_pond)

def lireMatriceFichier(nomFichier: str)->object:
    """Renvoie une matrice carrée contenue dans le fichier

    Args:
        nomFichier (str): _description_

    Returns:
        object: _description_
    """

def tousLesSommets(mat: object)->list:
    """Renvoie tous les sommets d'une matrice d'adjacence

    Args:
        mat (object): la matrice d'adjacence

    Returns:
        list: la liste de tous les sommets
    """
    lst_sommets = []
    len_mat = len(mat)
    for i in range(len_mat):
        lst_sommets.append(i)
    return lst_sommets

def listArcs(mat : object)-> [(float, float)]:
    lst_arcs = []
    len_mat_carre = len(mat)
    for i in range(len_mat_carre):
        for j in range(len_mat_carre):
            if mat[i][j]==1:
                lst_arcs.append((i, j))
    return lst_arcs

def matriceIncidence(mat : object)->object:
    """Retourne la matrice d'incidence associée au graphe
    défini par la matrice d'adjacence

    Args:
        mat (object): la matrice d'adjacence

    Returns:
        object: la matrice d'incidence
    """
    nb_sommets = tousLesSommets(nb_sommets)
    nb_chemins = listArcs(mat)

    matrice_incidence = np.zeros([nb_sommets, nb_chemins])

    nb_chem = 0

    for i in range(nb_sommets):
        for j in range(nb_sommets):
            if mat[i, j] == 1:
                matrice_incidence[i][nb_chem] = -1
                matrice_incidence[j][nb_chem] = 1
                nb_chem += 1               

    return matrice_incidence

print(tousLesSommets(mat_adj))
print(listArcs(mat_adj))

print("matrice incidence:", matriceIncidence(mat_adj))

def est_voisin(mat_adj, sommet_S, sommet_V)