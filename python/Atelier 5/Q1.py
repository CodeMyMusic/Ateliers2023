def somme_recursive(lst_int: list)-> int:
    """Prend en entrée une liste de nombre et
    retourne la somme de tous les éléments de la
    liste en utilisant la récursivité

    Args:
        lst_int (list): la liste d'entiers

    Returns:
        int: la somme des éléments de la liste
    """
    if lst_int:
        somme = lst_int.pop(0) + somme_recursive(lst_int)
    else:
        somme = 0

    return somme

print(somme_recursive([1, 2, 3]))