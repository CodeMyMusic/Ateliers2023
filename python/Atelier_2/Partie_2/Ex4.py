from Partie_1.Ex1 import val_max
import matplotlib.pyplot as plt

import sys

# adding Folder_2 to the system path
sys.path.insert(0, "C:/Users/aurel/Desktop/ATELIERS_2023/Atelier_2")


# CONSTANTES
F1 = [6, 5, 6, 7, 4, 2, 1, 5]
F2 = [3, 0, 6, 7, 4, 2, 1, 5]
F3 = [1, 0, 2, 3, 4, 5, 6, 0]
F4 = [2, 3, 1, 4, 4, 8, 8, 10, 1, 2, 3, 7, 7, 9, 11, 13]
F5 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]


def histo(F: list) -> list:
    """Renvoie à partir d'une liste d'entiers F
    une liste d'entiers H représentant l'histogramme
    de F

    Args:
        F (list): la liste d'entiers F

    Returns:
        list: la liste d'entiers H
    """
    # calcul de la valeur max (+1 pour compter le 0)
    max_val = val_max(F) + 1
    H = [0] * max_val

    # Parcourir la liste F et incrémenter les cases correspondantes de la liste H
    for elmt in F:
        H[elmt] += 1
    return H


def est_injective(F: list) -> bool:
    """Cette fonction renvoie la valeur True si la fonction 
    représentée par la liste F est une injection.
Dans le cas contraire, elle renvoie False.


    Args:
        F (list): liste d'entiers

    Returns: 
        bool: est-ce une injection
    """
    H = histo(F)
    i = 0
    injective = True
    len_H = len(H)
    while injective and i < len_H:
        if H[i] > 1:
            injective = False
        else:
            i += 1
    return injective


def est_surjective(F: list) -> bool:
    """Cette fonction renvoie la valeur True si 
    la fonction représentée par la liste F 
    est une surjection.
Dans le cas contraire, elle renvoie False.


    Args:
        F (list): liste d'entiers

    Returns: 
        bool: est-ce une surjection
    """
    H = histo(F)
    i = 0
    surjective = True
    len_H = len(H)
    while surjective and i < len_H:
        if H[i] < 1:
            surjective = False
        else:
            i += 1
    return surjective


def est_bijective(F: list) -> bool:
    """Cette fonction renvoie la valeur True si 
    la fonction représentée par la liste F 
    est une bijection.
Dans le cas contraire, elle renvoie False.


    Args:
        F (list): liste d'entiers

    Returns: 
        bool: est-ce une bijection
    """
    H = histo(F)
    i = 0
    bijective = True
    len_H = len(H)
    while bijective and i < len_H:
        if H[i] != 1:
            bijective = False
        else:
            i += 1
    return bijective


def afficher_histo(F: list):
    """Affiche l'histogramme à partir d'une liste

    Args:
        F (list): la liste d'entiers
    """
    H = histo(F)
    print("TEST HISTOGRAMME")
    print("F=", F)
    print("HISTOGRAMME")

    nb_lignes = val_max(H)
    len_h = len(H)
    # on itère en partant du nombre de lignes
    # et en terminant à zéro
    for l in range(nb_lignes, 0, -1):
        for c in range(len_h):
            if (H[c] >= l):
                print("   # ", end="")
            else:
                print("     ", end="")
        print('')
    for _ in range(len_h):
        print("| -- ", end='')
    print('')
    for c in range(len_h):
        if c < 10:
            print(" ", c, " ", end='')
        else:
            print(" ", c, "", end='')


def afficher_histo_lib(F: list):
    """Affiche l'histogramme à partir d'une liste
    grâce à la librairie MatplotLib.pyplot

    Args:
        F (list): la liste d'entiers
    """

    # pour l'axe des abscisses on sait que cela va jusqu'à la maleur max de F
    num_bins = max(F)

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.hist(F, bins=num_bins, rwidth=0.8)

    # pour ne pas dépasser la taille du tableau F dans l'axe des ordonnées
    plt.yticks(range(0, len(F)))

    plt.show()


# MAIN
def main():
    print("histo de ", F4, " : ", histo(F4))
    print("est injective : ", F1, " ", est_injective(F1))
    print("est injective : ", F2, " ", est_injective(F2))
    print("est injective : ", F3, " ", est_injective(F3))
    print("est bijective : ", F1, " ", est_bijective(F1))
    print("est bijective : ", F2, " ", est_bijective(F2))
    print("est bijective : ", F3, " ", est_bijective(F3))
    print("est surjective : ", F1, " ", est_surjective(F1))
    print("est surjective : ", F2, " ", est_surjective(F2))
    print("est surjective : ", F3, " ", est_surjective(F3))

    afficher_histo(F4)
    afficher_histo_lib(F4)

    # afficher_histo_lib(F5)


# --- EXECUTION ---#
if __name__ == "__main__":
    main()
