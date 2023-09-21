import numpy as np

A = np.array(([2, 5], [6,4]))
B = np.array(([1, 8], [4, 2]))

# print(A + B)

def my_add(tabA: object, tabB: object)-> object:
    """Réalise l'addition de deux matrices dont
    la taille est identique

    Args:
        tabA (object): la matrice A
        tabB (object): la matrice B

    Returns:
        object: la matrice résultante de l'addition
    """
    valide = True
    addition_matrices = []
    len_tab_a = len(tabA) 
    if len_tab_a == len(tabB):
        valide = True
        nb_lst = 0
        while valide and nb_lst < len_tab_a:
            list_in_tab_a = tabA[nb_lst]
            list_in_tab_b = tabB[nb_lst]
            if list_in_tab_a is float or list_in_tab_b is float: 
                valide = False
            else:
                if len(tabA[nb_lst]) != len(tabB[nb_lst]):
                    valide = False
                else:
                    len_lists = len(list_in_tab_a)
                    addition_listes = []
                    for i in range(len_lists):
                        addition_listes.append(list_in_tab_a[i] + list_in_tab_b[i])
                    addition_matrices.append(addition_listes)
                    nb_lst += 1
    else:
        valide = False

    if valide:
        res = addition_matrices
    else:
        res = "Erreur"
    
    return res

print(my_add(A, B))

C = np.array(([1, 2, 3], [4, 5, 6], [7, 8, 9]))
print(C)

# 2. Opérations élémentaires

C+= 10

print(C)

C*= 2

print(C)

# 3. Slicing et indexation

print(C[1])
print(C[:, 2])

D = C[:2, :2]

print(D)