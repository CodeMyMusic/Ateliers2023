liste_non_triee_relative = [-5, 0, 0, -12, 5, 8, 0, -13, 0, 45, -2, -9, 62, 32, 0, 0]

def separer(lst : list) -> list:
    """Renvoie à partir d'une liste de nombres relatifs 
    une liste où les nombres négatifs sont à gauche, les 0
    au milieu et les nombres positifs à droite

    Args:
        lst (list): _description_

    Returns:
        list: _description_
    """
    new_list = []
    # index du delimiteur des 0
    debut_zero = 0
    for elmt in lst:
        if elmt == 0:
            # on insère là où se trouvent les 0
            # grâce à l'index du premier 0
            new_list.insert(debut_zero, elmt)
        elif elmt > 0:
            # on ajoute le nombre positif à la fin
            # du tableau
            new_list.append(elmt)
        else:
            # on insère au début de liste l'élément
            # positif
            new_list.insert(0, elmt)
            # il faut donc incrémenter l'index du
            # délimiteur des 0
            debut_zero += 1
    
    return new_list

res = separer(liste_non_triee_relative)

# j'ai trouvé du premier coup !
print(res)
