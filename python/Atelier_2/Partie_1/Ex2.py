### CONSTANTES ####

liste_non_triee_sans_doublons = [5, 1, 12, 2, 24, 18, 17, 3, 8, 87, 6, 278, 210]
liste_non_triee_doublons = [2, 1, 24, 1, 0, 25, 24, 12, 3, 1]
liste_non_triee = [1, 2, 3, 2, 1]
liste_triee = [2, 4, 6, 8, 9, 10, 11, 15, 34, 35, 70, 73, 78, 79, 81, 90]
liste_triee_doublons = [2, 2, 3, 3, 4, 5, 10]

#### ////// #####

#// FONCTIONS

def position_for(lst : list, e : int) -> int:
    """Retourne l'indice de l'entier e dans la liste lst
    (en utilisant une boucle for)

    Args:
        lst (list): la liste
        e (int): l'entier

    Returns:
        int: l'indice de l'entier dans la liste
    """
    index = -1
    lst_len = len(lst)
    for i in range (lst_len):
        if lst[i] == e:
            index = i
    return index

def position_tri(lst : list, e : int) -> int:
    """Trouve l'indice d'un entier dans une liste en supposant qu'elle est
    triee (recherche dichotomique)

    Args:
        lst (list): la liste
        e (int): l'entier

    Returns:
        int: _description_
    """
    index = -1
    # on rend la taille de la liste divisible (paire)
    len_lst_pair = len(lst) - (len(lst) % 2)
    len_moitie_lst = int(len_lst_pair / 2)
    if lst[len_moitie_lst] == e:
        index = len_moitie_lst
    # si inferieur à e
    elif lst[len_moitie_lst] < e:
        # on veut tester de la moitie à la fin de la liste
        lst = lst[len_moitie_lst:]

        # e est dans la seconde partie du tableau
        # donc on rajoute l'indice de la moitié du tableau actuel à l'index de
        # la seconde moitié renvoyé par la fonction position_tri
        index = len_moitie_lst + position_tri(lst, e)
    else:
        # on veut tester du debut à la moitie de la liste
        lst = lst[0:len_moitie_lst]
        
        # e est dans la première moitié, on a juste à chercher
        # son index dans la première moitié
        index = position_tri(lst, e)

    return index


def position_while(lst : list, e : int) -> int:
    """Retourne l'indice de l'entier e dans la liste lst
    (en utilisant une boucle while)

    Args:
        lst (list): la liste
        e (int): l'entier

    Returns:
        int: l'indice de l'entier dans la liste
    """
    index = -1
    i = 0
    lst_len = len(lst)
    trouveIndice = False
    while i < lst_len and not trouveIndice:
        if lst[i] == e:
            index = i
            trouveIndice = True
        else:
            i += 1
    return index

def nb_occurrences(lst : list, e : int) -> int:
    """Retourne le nombre d'occurences de l'entier e dans la liste lst

    Args:
        lst (list): la liste
        e (int): l'entier

    Returns:
        int: le nombre d'occurences dans la liste
    """
    nb_occ = 0
    lst_len = len(lst)
    for i in range (lst_len):
        if lst[i] == e:
            nb_occ += 1
    return nb_occ

def est_triee_for(lst : list) -> bool:
    """Détermine si une liste est triee par ordre croissant
    (boucle for)

    Args:
        lst (list): la liste

    Returns:
        bool: la liste est triee ou non
    """
    trie = True
    lst_len = len(lst)
    minVal = lst[0]
    for i in range (1, lst_len):
        # si l'emlt est inferieur à l'elmt precedent
        if lst[i] < minVal:
            trie = False
        else:
            # on définit l'elmt precedent comme l'elmt actuel
            minVal = lst[i]

    return trie

def est_triee_while(lst : list) -> bool:
    """Détermine si une liste est triee par ordre croissant
    (boucle while)

    Args:
        lst (list): la liste

    Returns:
        bool: la liste est triee ou non
    """
    trie = True
    lst_len = len(lst)
    minVal = lst[0]
    i = 0
    while i < lst_len and trie:
        # si l'emlt est inferieur à l'elmt precedent
        if lst[i] < minVal:
            trie = False
        else:
            # on définit l'elmt precedent comme l'elmt actuel
            minVal = lst[i]
            i += 1

    return trie


def a_repetitions(lst : list) -> bool:
    """Détermine si une liste comporte des répétitions de valeurs

    Args:
        list (list): la liste

    Returns:
        bool: la liste comporte des répétitions
    """
    t_list = []
    repetition = False
    i = 0
    list_len = len(lst)
    while not repetition and i < list_len:
        if lst[i] not in t_list:
            t_list.append(lst[i])
            i += 1
        else:
            repetition = True
    return repetition
    
def tester():
    """Fonction de test
    """
    # TESTS INDICES
    indice_boucle_for = position_for(liste_non_triee_sans_doublons, 2)
    indice_boucle_while = position_while(liste_non_triee_sans_doublons, 2)
    print("indice boucle for : ", indice_boucle_for)
    print("indice boucle while : ", indice_boucle_while)

    # TEST OCCURENCE
    print("nb occ :", nb_occurrences(liste_non_triee_doublons, 1))

    # TEST TRI
    print("TEST POUR SAVOIR SI LISTE TRIEE PAR ORDRE CROISSANT")
    print("test liste triee par ordre croissant boucle for : ", est_triee_for(liste_triee))
    print("test liste triee par ordre croissant boucle while : ", est_triee_while(liste_triee))
    print("test liste triee par ordre croissant avec doublons double for: ", est_triee_for(liste_triee_doublons))
    print("test liste triee par ordre croissant avec doublons boucle while: ", est_triee_while(liste_triee_doublons))
    print("test liste non triee boucle for : ", est_triee_for(liste_non_triee))
    print("test liste non triee boucle while : ", est_triee_while(liste_non_triee))

    # TEST INDICE LISTE SUPPOSEE TRIEE
    print("test liste position indice supposee triee (e : 15) : ", position_tri(liste_triee, 15))
    print("test liste position indice supposee triee (e : 15) : ", position_tri(liste_triee, 90))
    print("test liste position indice supposee triee (e : 15) : ", position_tri(sorted(liste_non_triee_sans_doublons), 278))

    # TEST REPETITIONS
    print("test liste avec doublons repetition: ", a_repetitions(liste_non_triee_doublons))
    print("test liste sans doublons repetition: ", a_repetitions(liste_non_triee_sans_doublons))


# MAIN
def main():
    tester()

#--- EXECUTION ---# 
if __name__ == "__main__":
    main()