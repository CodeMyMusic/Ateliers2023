def present(L : list, e : int) -> int:
    """Retourne l'indice de l'entier e dans la liste lst
    (en utilisant une boucle while)

    Args:
        lst (list): la liste
        e (int): l'entier

    Returns:
        int: l'indice de l'entier dans la liste
    """
    i = 0
    lst_len = len(L)
    trouveIndice = False
    while i < lst_len and not trouveIndice:
        if L[i] == e:
            trouveIndice = True
        else:
            i += 1
    return trouveIndice

def test_present(present: callable):
    pass