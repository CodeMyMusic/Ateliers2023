liste_L = [1, 10, 100, 1000, 10000]

def sommme_boucle_for_index(lst : list) -> int:
    """Retourne la somme des valeurs d'une liste
    avec pour moyen une boucle for basée sur les
    indices

    Args:
        liste (list): la liste

    Returns:
        int: la somme
    """
    somme = 0
    for i in range(len(lst)):
        somme += lst[i]
    return somme

def somme_boucle_for_elmt(lst : list) -> bool:
    """Retourne la somme des valeurs d'une liste
    avec pour moyen une boucle for basée sur les
    éléments

    Args:
        liste (list): la liste

    Returns:
        int: la somme
    """
    somme = 0
    for e in lst:
        somme += e
    return somme

def somme_boucle_while(lst : list) -> bool:
    """Retourne la somme des valeurs d'une liste
    avec pour moyen une boucle while

    Args:
        liste (list): la liste

    Returns:
        int: la somme
    """
    somme = 0
    i = 0
    while i < len(lst):
        somme += lst[i]
        i += 1
    return somme

def tester():
    """Teste nos fonctions qui somment une liste
    """

    print("TEST SOMME")
    # test liste vide
    print("Test liste vide (boucle for basée sur les indices) : ", 
    sommme_boucle_for_index([]))
    print("Test liste vide (boucle for basée sur les éléments) : ", 
    somme_boucle_for_elmt([]))
    print("Test liste vide (boucle while) : ", 
    somme_boucle_while([]))

    #test somme 11111
    liste = [1, 10, 100, 1000, 10000]
    print("Test liste d'entiers (boucle for basée sur les indices) : ", 
    sommme_boucle_for_index(liste))
    print("Test liste d'entiers (boucle for basée sur les éléments) : ", 
    somme_boucle_for_elmt(liste))
    print("Test liste d'entiers (boucle while) : ", 
    somme_boucle_while(liste))

def main():
    tester()

def moyenne(lst : list) -> float:
    """Retourne la moyenne des valeurs d'une liste

    Args:
        lst (list): la liste

    Returns:
        float: la moyenne
    """
    # si la liste n'est pas vide
    if len(lst) > 0:
        moy = somme_boucle_for_elmt(lst) / len(lst)
    else:
        # on définit la moyenne à 0 quand la liste est vide
        moy = 0
    return moy

def nb_sup_for_elmt(lst : list, elmt : int) -> list:
    """Renvoie le 

    Args:
        lst (list): _description_
        elmt (int): _description_

    Returns:
        list: _description_
    """
    lst_values_inferior_than_elmt = []
    for value in lst:
        if value > elmt:
            lst_values_inferior_than_elmt.append(value)

    return lst_values_inferior_than_elmt

def nb_sup_for_index(lst : list, elmt : int) -> list:
    lst_values_inferior_than_elmt = []
    for i in range(len(lst)):
        if lst[i] > elmt:
            lst_values_inferior_than_elmt.append(lst[i])

    return lst_values_inferior_than_elmt

#--- EXECUTION ---# 
if __name__ == "__main__":
    main()
