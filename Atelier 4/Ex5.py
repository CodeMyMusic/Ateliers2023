import time

from Ex2 import mix_list
from Ex4 import extract_elmts_list
from random import *

# TEST COMPARATIF MIX_LIST ET SHUFFLE
def perf_mix(mix_list : callable, shuffle: callable, int_taille_lst : list, nb_exec: int)-> (float, float):
    """Calcule le temps moyen d'éxécution de mix_list et shuffle

    Args:
        mix_list (_type_): ma fonction mélangeant une liste
        float (_type_): la fonction de python mélangeant une liste

    Returns:
        _type_: renvoie un tuple contenant les temps moyen d'éxécution
    """
    total_time_mix_list = 0
    total_time_shuffle = 0
    # on parcoure les différentes tailles
    for taille in int_taille_lst:
        # on crée un tableau ayant pour taille la valeur taille
        lst = [i for i in range(taille)]
        # nbr exécutions
        for _ in range(nb_exec):
            start_pc = time.perf_counter()
            mix_list(lst)
            end_pc = time.perf_counter()
            total_time_mix_list += end_pc - start_pc

            start_pc = time.perf_counter()
            shuffle(lst)
            end_pc = time.perf_counter()
            total_time_shuffle += end_pc - start_pc
    # total_time = total_time_mix_list + total_time_shuffle
    time_exec_average_mix_list = total_time_mix_list / (len(int_taille_lst)*nb_exec)
    time_exec_average_shuffle = total_time_shuffle/ (len(int_taille_lst)*nb_exec)

    return (time_exec_average_mix_list, time_exec_average_shuffle)


# TEST COMPARATIF EXTRACT_ELMTS ET SAMPLE
def perf_extract(extract_elmts : callable, sample: callable, int_taille_lst : list, nb_exec: int)-> (float, float):
    """Calcule le temps moyen d'éxécution de extract_elmts list et de sample

    Args:
        mix_list (_type_): ma fonction qui extrait des éléments d'une liste
        au hasard
        float (_type_): la fonction de python prenant au hasard des éléments
        dans une liste

    Returns:
        _type_: renvoie un tuple contenant les temps moyen d'éxécution
    """
    total_time_extract_elmts = 0
    total_time_shuffle = 0

    # on parcoure les différentes tailles
    for taille in int_taille_lst:
        # on crée un tableau ayant pour taille la valeur taille
        lst = [i for i in range(taille)]
        nb_elmts_extract = randint(1, len(lst))
        # nbr exécutions
        for _ in range(nb_exec):
            start_pc = time.perf_counter()
            
            extract_elmts(lst, nb_elmts_extract)
            end_pc = time.perf_counter()
            total_time_extract_elmts += end_pc - start_pc

            start_pc = time.perf_counter()
            sample(lst, nb_elmts_extract)
            end_pc = time.perf_counter()
            total_time_shuffle += end_pc - start_pc
    time_exec_average_1 = total_time_extract_elmts / (len(int_taille_lst)*nb_exec)
    time_exec_average_2 = total_time_shuffle/ (len(int_taille_lst)*nb_exec)

    return (time_exec_average_1, time_exec_average_2)


def tester():

    print(perf_mix(mix_list, shuffle, [500], 900))
    print(perf_extract(extract_elmts_list, sample, [500], 900))

tester()



