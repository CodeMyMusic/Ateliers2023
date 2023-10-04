import numpy as np
from random import *

# matrice de 4x4 valeurs aléatoires en 0 et 10
A = np.array([[ randint(0, 9) for _ in range(4)] for _ in range(4)])

print("A:", A)

# matrice de 4x4 valeurs aléatoires en 0 et 10
A = np.random.randint(0, 9, (4, 4))
print("A (built-in):", A)

# matrice identité de dimension 4x4
B = np.zeros([4, 4], int)
# diagonale principale on met que des 1
np.fill_diagonal(B, 1)
print("B:", B)


def matrice_trace(matrice : object)-> int:
    """Prend en entrée une matrice carrée et
    retourne sa trace

    Args:
        matrice (object): la matrice

    Returns:
        int: la somme des valeurs de la diagonale
        de la matrice
    """
    trace = 0
    for i in range(len(matrice)):
        trace += matrice[i][i]
    return trace

def est_symetrique(matrice : object)->bool:
    """Détermine si une matrice est symétrique ou non

    Args:
        matrice (object): la matrice (doit être carrée)

    Returns:
        bool: renvoie si oui ou non la matrice est symétrique
    """
    valide = True
    i = 0
    len_matrice = len(matrice)
    while i <len_matrice and valide:
        len_ligne = len(matrice[i])
        j = 0
        while j < len_ligne and valide:
            if matrice[i][j] == matrice[j][i]:
                j += 1
            else:
                valide = False
        i+=1

    return valide


def produit_diagonal(matrice : object)-> float:
    """Retourne le produit des éléments de la diagonale
    principale de la matrice carrée

    Args:
        matrice (object): la matrice (doit être carrée)

    Returns:
        float: le produit des elmts de la diago principale
    """
    produit = 1
    for i in range(len(matrice)):
        produit *= matrice[i][i]
    return produit

print(matrice_trace(B), matrice_trace(A))
print(est_symetrique((A + A.T)/2)) # True

print("produit diagonal matrice identité:", produit_diagonal(B))

print(np.transpose(A)*A)

if produit_diagonal(A) != 0:
    print("matrice proche matrice i ?",np.dot(np.linalg.inv(A), A))
else:
    print("matrice a non inversible")