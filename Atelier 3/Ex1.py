def full_name(str_arg: str) -> str:
    """Renvoie le nom prénom formaté

    Args:
        str_arg (str): nom prenom

    Returns:
        str: nom prenom formaté
    """
    str_arg = str_arg.split(' ')

    nom = str_arg[0].upper()
    prenom = str_arg[1].capitalize()

    return ' '.join([nom, prenom])

def full_name_without_functions(str_arg: str) -> str:
    """Renvoie le nom prénom formaté

    Args:
        str_arg (str): nom prenom

    Returns:
        str: nom prenom formaté
    """
    nomTrouve = False
    premiereLettrePrenom = True

    # résultat final
    str_res = ''

    for c in str_arg:
        # délimiteur nom / prénom
        if c == ' ':
            str_res += ' '
            nomTrouve = True
        else:
            if not nomTrouve:
                str_res += majuscule(c)
            else:
                if premiereLettrePrenom:
                    str_res += majuscule(c)
                    premiereLettrePrenom = False
                else:
                    # si c'est une minuscule
                    if 97 <= ord(c) <= 122:
                        str_res += c
                    else:
                        # conversion en minuscule
                        str_res += chr(ord(c) + 32)

    return str_res

def majuscule(c : chr)-> chr:
    # si ce n'est pas une majuscule
    if ord(c) < 65 or ord(c) > 90:
        # on convertit en majuscule
        c = chr(ord(c) - 32)
    return c
    

print(full_name_without_functions("véron aUrÈlE"))