liste_L = [1, 10, 100, 1000, 10000]

def sommme_boucle_for_index(liste : list) -> int:
    """Retourne la somme des valeurs d'une liste
    avec pour moyen une boucle for basée sur les
    indices

    Args:
        liste (list): la liste

    Returns:
        int: la somme
    """
    somme = 0
    for i in range(0, len(liste)):
        somme += liste[i]
    return somme

def somme_boucle_for_elmt(liste : list) -> bool:
    """Retourne la somme des valeurs d'une liste
    avec pour moyen une boucle for basée sur les
    éléments

    Args:
        liste (list): la liste

    Returns:
        int: la somme
    """
    somme = 0
    for e in liste:
        somme += e
    return somme

def somme_boucle_while(liste : list) -> bool:
    """Retourne la somme des valeurs d'une liste
    avec pour moyen une boucle while

    Args:
        liste (list): la liste

    Returns:
        int: la somme
    """
    somme = 0
    i = 0
    while i < len(liste):
        somme += liste[i]
        i += 1
    return somme

def tester():
    """Teste nos fonctions qui somment une liste
    """

    print("TEST SOMME")
    # test liste vide
    print("Test liste vide (boucle for basée sur les indices) : ", 
    sommme_boucle_for_index([]))
    print("Test liste vide (boucle for basée sur les éléments) : ", 
    somme_boucle_for_elmt([]))
    print("Test liste vide (boucle while) : ", 
    somme_boucle_while([]))

    #test somme 11111
    liste = [1, 10, 100, 1000, 10000]
    print("Test liste d'entiers (boucle for basée sur les indices) : ", 
    sommme_boucle_for_index(liste))
    print("Test liste d'entiers (boucle for basée sur les éléments) : ", 
    somme_boucle_for_elmt(liste))
    print("Test liste d'entiers (boucle while) : ", 
    somme_boucle_while(liste))

def main():
    tester()

#--- EXECUTION ---# 
if __name__ == "__main__":
    main()
