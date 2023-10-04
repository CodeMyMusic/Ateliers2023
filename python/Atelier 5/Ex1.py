import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
print(arr)

x = np.searchsorted(arr, 4)
print(x)

x = np.where(arr == 4)

print(x)


def my_searchsorted(table: object, elmt : int) -> int:
    """Cherche un élément dans un tableau
    et renvoie sa place

    Args:
        table (object): le tableau
        elmt (int): l'elmt à trouver

    Returns:
        int: l'indice de l'elmt
    """
    trouve = 0
    i = 0
    len_table = len(table)
    while i < len_table and not trouve:
        if table[i] == elmt:
            trouve = True
        else:
            i += 1
    return i

def my_where(table: object, elmt = int) -> list:
    """Cherche un élément dans un tableau
    et renvoie sa place

    Args:
        table (object): le tableau
        elmt (int): l'elmt à trouver

    Returns:
        int: l'indice de l'elmt
    """
    lst_index_elmt = []
    for i in range(len(table)):
        e = table[i]
        if e == elmt:
            lst_index_elmt.append(i)

    return lst_index_elmt

print(my_searchsorted(arr, 4))
print(my_where(arr, 4))