import time

import matplotlib.pyplot as plt
import numpy as np

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
    temps_taille_mix_list = []
    temps_taille_shuffle = []

    # on parcoure les différentes tailles
    for taille in int_taille_lst:
        # on crée un tableau ayant pour taille la valeur taille
        lst = [i for i in range(taille)]
        nb_elmts_extract = randint(1, len(lst))

        total_time_mix_list = 0
        total_time_shuffle = 0
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

        temps_taille_mix_list.append(total_time_mix_list / nb_exec)
        temps_taille_shuffle.append(total_time_shuffle/ nb_exec)


    return (temps_taille_mix_list, temps_taille_shuffle)


# TEST COMPARATIF EXTRACT_ELMTS ET SAMPLE
def perf_extract(extract_elmts : callable, sample: callable, int_taille_lst : list, nb_exec: int)-> ([], []):
    """Calcule le temps moyen d'éxécution de extract_elmts list et de sample

    Args:
        mix_list (_type_): ma fonction qui extrait des éléments d'une liste
        au hasard
        float (_type_): la fonction de python prenant au hasard des éléments
        dans une liste

    Returns:
        tuple: renvoie un tuple contenant les temps moyen d'éxécution
        par taille
    """

    temps_taille_extract_elmts = []
    temps_taille_sample = []

    # on parcoure les différentes tailles
    for taille in int_taille_lst:
        # on crée un tableau ayant pour taille la valeur taille
        lst = [i for i in range(taille)]
        nb_elmts_extract = randint(1, len(lst))

        total_time_extract_elmts = 0
        total_time_sample = 0
        # nbr exécutions
        for _ in range(nb_exec):
            start_pc = time.perf_counter()
            
            extract_elmts(lst, nb_elmts_extract)
            end_pc = time.perf_counter()
            total_time_extract_elmts += end_pc - start_pc

            start_pc = time.perf_counter()
            sample(lst, nb_elmts_extract)
            end_pc = time.perf_counter()
            total_time_sample += end_pc - start_pc

        temps_taille_extract_elmts.append(total_time_extract_elmts / nb_exec)
        temps_taille_sample.append(total_time_sample/ nb_exec)


    return (temps_taille_extract_elmts, temps_taille_sample)


def tester():
    tailles_array = [10, 1000, 3000, 5000, 10000]

    fig, ax = plt.subplots()

    x_axis = np.arange(0, len(tailles_array))

    mix_list_time, shuffle_time = perf_mix(mix_list, shuffle, tailles_array, 20)
    extract_time, sample_time = perf_extract(extract_elmts_list, sample, tailles_array, 20)

    # plt.xticks = (x_axis, tailles_array)
    ax.set_xticks(x_axis)
    ax.set_xticklabels(tailles_array)

    # ax.set_yticks([i/10 for i in range(0, 10)])
    ax.set_yscale('log')

    ax.plot(x_axis, mix_list_time, 'r.-', label='list_mix')
    ax.plot(x_axis, shuffle_time, 'g.-', label='shuffle')
    ax.plot(x_axis, extract_time, 'y.-', label='extract_elmts_list')
    ax.plot(x_axis, sample_time, 'b.-', label='sample')

    ax.set(xlabel='Taille du tableau', ylabel="Temps d'execution moyen", title='Fonctions')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')

    plt.show()

    # ax.plot(x_axis_list, x_axis_list**2, 'r*-', label='Carré')
    # ax.plot(x_axis_list, x_axis_list**3, 'g*-', label='Cube')

tester()