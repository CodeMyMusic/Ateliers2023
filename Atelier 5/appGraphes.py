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
mes_chemins = [(0,1), (0, 2), (1,2), (1, 4), (2, 3), (3, 4), (4, 2)]
mes_sommets = [0, 1, 2, 3, 4]
mat_adj = matriceAdjacences(mes_sommets, mes_chemins)
print("matrice adjacence: \n",mat_adj)
mes_chemins_ponderes = [(0,1, 12), (0, 2, 14), (1,2, 8), (1, 4, 3), (2, 3, 21), (3, 4, 18), (4, 2, 19)]
mat_adj_pond = matriceAdjacencePond(mes_sommets, mes_chemins_ponderes)
print("matrice adjacence pondérée: \n",mat_adj_pond)

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
    for i in range(len(mat)):
        lst_sommets.append(i)
    return lst_sommets

def listArcs(mat : object)-> [(float, float)]:
    lst_arcs = []
    # comme la matrice d'adjacence se lit NBSOMMETS * NBSOMMETS
    for i in range(len(mat)):
        for j in range(len(mat)):
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
    nb_sommets = len(tousLesSommets(mat))
    nb_chemins = len(listArcs(mat))

    matrice_incidence = np.zeros([nb_sommets, nb_chemins])

    nb_chem = 0

    # la matrice d'adjacence se lit NBSOMMETS * NBSOMMETS
    # i représente donc un SOMMET (LIGNES dans la matrice d'adjcence)
    # j représente donc un SOMMET (COLONNES dans la matrice d'ajdacence)
    for i in range(nb_sommets):
        for j in range(nb_sommets):
            if mat[i, j] == 1:
                # le sommet i est associé au chemin sortant nb_chem
                matrice_incidence[i][nb_chem] = -1
                # le sommet j est associé au chemin entrant nb_chem
                matrice_incidence[j][nb_chem] = 1
                nb_chem += 1               

    return matrice_incidence

print("matrice incidence: \n", matriceIncidence(mat_adj))

def est_voisin(mat_adj, sommet_S, sommet_V)-> bool:
    return mat_adj[sommet_S][sommet_V] == 1

print("(0,3): ", est_voisin(mat_adj, 0, 3))
print("(0,2): ", est_voisin(mat_adj, 0, 2))
