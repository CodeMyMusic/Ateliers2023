from Ex4 import histo


def agencer_test(lstObjets: list):
    """Ma propre fonction d'agencement
    renvoie à partir d'une liste d'objets
    deux vitrines dont aucun doublon n'est présent

    Args:
        lstObjets (list): la liste d'objets

    Returns:
        error or list
    """
    H = histo(lstObjets)
    vitrines = [[], []]
    len_H = len(H)
    for i in range(len_H):
        if H[i] > 2:
            vitrines = "erreur"
        else:
            if H[i] == 2:
                vitrines[0].append(i)
                vitrines[1].append(i)
            elif H[i] == 1:
                if len(vitrines[0]) <= len(vitrines[1]):
                    vitrines[0].append(i)
                else:
                    vitrines[1].append(i)
    return vitrines


def agencer(nbEmplacements: int, lstObjets: list) -> tuple:
    """Agence des objets dans deux vitrines. Retourne
    -1 si aucune solution n'est possible

    Args:
        nbEmplacements (int): nombre d'emplacements disponibles pour
        chaque vitrine
        lstObjets (list): la liste d'objets

    Returns:
        tuple: les deux vitrines remplies
    """


    H = histo(lstObjets)
    len_histo = len(H)
    possible = True
    i = 0
    vitrine1 = []
    vitrine2 = []
    len_vitrine1 = 0
    len_vitrine2 = 0
    while possible and i < len_histo:
        elmt = i
        # s'il y a plus de deux répétitions
        # on ne peut pas répartir dans les deux
        # vitrines sans éviter un doublon
        if H[i] > 2:
            possible = False
        # si il y a deux répétions on réparti dans
        # chaque vitrine
        elif H[i] == 2:
            vitrine1.append(elmt)
            vitrine2.append(elmt)
            len_vitrine1 += 1
            len_vitrine2 += 1
        elif H[i] == 1:
            # si une des vitrines est plus remplie
            if len_vitrine1 >= len_vitrine2:
                vitrine2.append(elmt)
                len_vitrine2 += 1
            else:
                vitrine1.append(elmt)
                len_vitrine1 += 1
        i += 1

    if not possible:
        res = -1
    else:
        res = (vitrine1, vitrine2)
    return res

# MAIN
def main():
    # avait marché du premier coup mais
    print(agencer_test([1, 2, 2, 3, 4, 5, 5]))

    # fonction intransigeante
    print(agencer(8, [1, 2, 3, 4, 5, 6, 300, 300, 200, 201, 202, 200]))


# --- EXECUTION ---#
if __name__ == "__main__":
    main()
