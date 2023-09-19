from random import *

def extract_elmts_list(lst: list, nbr : int) -> list:
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
