def factorielle_recursive(n: int)-> int:
    """Prend en entrée un nombre et
    retourne la factorielle de ce nombre
    par la récursivité

    Args:
        lst_int (list): la liste d'entiers

    Returns:
        int: la factorielle
    """
    if n > 0:
        produit = n * factorielle_recursive(n-1)
    else:
        produit = 1

    return produit

print(factorielle_recursive(5))