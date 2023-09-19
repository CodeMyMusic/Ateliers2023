from random import *

def mix_list(list_to_mix : list)->list:
    """Mélange une liste potentiellement triée
    et retourne la liste mélangée

    Args:
        list_to_mix (list): la liste à mélanger

    Returns:
        list: la liste mélangée
    """
    # liste des indices de list_to_mix
    lst_index = []
    len_lst_index = len(list_to_mix)
    i = len_lst_index
    while i > 0:
        # on prend un indice au hasard
        index = int(random()*len_lst_index)
        if index not in lst_index:
            # on ajoute l'indice à la liste d'indices
            lst_index.append(index)
            # on a donc mélangé 1 élément
            i-= 1

    # grâces aux indices des éléments piochés, on reconstitue la liste mélangée
    list_mixed = [list_to_mix[lst_index[i]] for i in range(len_lst_index)]
    return list_mixed

# Test de votre code
lst_sorted = [i for i in range(10)]
print('Liste triée de départ', lst_sorted)
mixed_list = mix_list(lst_sorted)
print('Liste mélangée obtenue', mixed_list)
print('Liste triée de départ après appel à mixList, elle doit être inchangée', lst_sorted)
# assert (cf. doc en ligne) permet de vérifier qu’une condition
# est vérifiée en mode debug (désactivable)
assert lst_sorted != mixed_list, "Les deux listes doivent être différentes après l'appel à mixList..."

# Test de votre code
lst_sorted = [i+42 for i in range(20)]
print('Liste triée de départ', lst_sorted)
mixed_list = mix_list(lst_sorted)
print('Liste mélangée obtenue', mixed_list)
print('Liste triée de départ après appel à mixList, elle doit être inchangée', lst_sorted)
# assert (cf. doc en ligne) permet de vérifier qu’une condition
# est vérifiée en mode debug (désactivable)
assert lst_sorted != mixed_list, "Les deux listes doivent être différentes après l'appel à mixList..."