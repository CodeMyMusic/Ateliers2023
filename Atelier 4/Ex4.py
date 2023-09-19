from random import *

def extract_elmts_list(lst: list, nbr : int) -> list:
    """Extrait un certain nombre d'éléments d'une liste

    Args:
        lst (list): la liste
        nbr (int): le nombre d'elmts à extraire

    Returns:
        list: la liste d'éléments extraits
    """
    lst_index_elmts = []
    i = 0
    while i < nbr:
        # on prend un indice au hasard
        index = int(random()*len(lst))
        if index not in lst_index_elmts:
            i += 1
            lst_index_elmts.append(index)
    lst_elmts = [lst[lst_index_elmts[i]] for i in range(len(lst_index_elmts))]
    return lst_elmts

# Test de votre code
lst_sorted = [i + 27 for i in range(20)]
print('Liste de départ',lst_sorted)
sublist = extract_elmts_list(lst_sorted,5)
print('La sous liste extraite est', sublist)
print('Liste de départ après appel de la fonction est',lst_sorted)
