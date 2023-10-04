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
    # pour éviter recalcul à chaque itération
    len_list = len(lst)
    for i in range(len_list):
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
    # pour éviter recalcul à chaque itération
    len_list = len(lst)
    i = 0
    while i < len_list:
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

    print(val_max([1, 503, 501, 70, 3, 1]))
    print(ind_max([1, 503, 501, 70, 3, 1]))

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

def nb_sup_for_elmt(lst : list, e : int) -> int:
    """Renvoie le nombre de valeurs dans la liste supérieures à un entier e
    en utilisant une boucle for basée sur les éléments

    Args:
        lst (list): la liste d'entiers
        elmt (int): l'entier

    Returns:
        int: le nombre d'éléments
    """
    nbr_sup_elmt = 0
    for value in lst:
        if value > e:
            nbr_sup_elmt += 1

    return nbr_sup_elmt

def nb_sup_for_index(lst : list, e : int) -> int:
    """Renvoie le nombre de valeurs dans la liste supérieures à un entier e
    en utilisant une boucle for basée sur les indices

    Args:
        lst (list): la liste d'entiers
        elmt (int): l'entier

    Returns:
        int: le nombre d'éléments
    """
    nbr_sup_elmt = 0
    for i in range(len(lst)):
        if lst[i] > e:
            nbr_sup_elmt += 1

    return nbr_sup_elmt

def moy_sup(lst : list, e : int) -> float:
    """Retourne la moyenne des valeurs d'une liste strictement
    supérieures à e

    Args:
        lst (list): la liste d'entiers
        e (int): l'entier

    Returns:
        float: la moyenne
    """
    nb_sup_lst = []
    for value in lst:
        if value > e:
            nb_sup_lst.append(value)
    
    return moyenne(nb_sup_lst)

def val_max(lst : list) -> int:
    """Retourne la valeur maximale d'une liste

    Args:
        lst (list): la liste

    Returns:
        int: la valeur max
    """
    len_lst = len(lst)
    if len_lst == 0:
        max_val = 0
    else:
        max_val = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > max_val:
                max_val = lst[i]
    return max_val

def ind_max(lst : list) -> int:
    """Retourne l'indice de la valeur maximale d'une liste

    Args:
        lst (list): la liste

    Returns:
        int: l'indice de la valeur max
    """
    max_val_index = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[max_val_index]:
            max_val = i
    return max_val

# MAIN
def main():
    tester()

#--- EXECUTION ---# 
if __name__ == "__main__":
    main()
