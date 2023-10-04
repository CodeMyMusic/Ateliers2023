from random import *

def gen_list_random_int(int_binf = 0, int_bsup = 10, len_lst =10)->list:
    """Génère une liste de nombres
    aléatoires compris entre int_binf et int_bsup

    Args:
        int_binf: min (par défaut 0)
        int_bsup : max (par défaut 10)
        len_lst : longeur de la liste
    
    Returns:
        list: la liste
    """
    lst = []
    for _ in range(len_lst):
        lst.append(int(random()*(int_bsup-int_binf)+int_binf))
    return lst

print(gen_list_random_int())
print(gen_list_random_int(247, 500, 30))

