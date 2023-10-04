from random import *

def choose_elmt(lst: list)-> float:
    """Choisi un élément au hasard dans une 
    liste

    Args:
        lst (list): la liste
    Returns:
        float : l'élément choisi
    """

    # on prend un indice au hasard
    index = int(random()*len(lst))

    return lst[index]

# Test de votre code
lst_sorted = [i + 27 for i in range(20)]
print('Liste triée de départ', lst_sorted)
e1 = choose_elmt(lst_sorted)
print('A la première exécution', e1, 'a été sélectionné')
e2 = choose_elmt(lst_sorted)
print('A la deuxième exécution', e2, 'a été sélectionné')
assert e1 != e2, "Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"