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

# CODE PLUS PERFORMANT
def full_name_without_functions(str_arg: str) -> str:
    """Renvoie le nom prénom formaté

    Args:
        str_arg (str): nom prenom

    Returns:
        str: nom prenom formaté
    """
    # Tant qu'on ne trouve pas le nom
    nomTrouve = False
    # pour que la première du prénom soit
    # convertie en majuscule
    premiereLettrePrenom = True

    # résultat final
    full_name = ''

    # on parcoure le nom prénom non formaté
    for char in str_arg:
        # s'il y a un espace
        if char == ' ':
            full_name += ' '
            # le nom est trouvé
            nomTrouve = True
        else:
            # si le nom n'est pas trouvé
            if not nomTrouve:
                # on convertir en majuscule
                full_name += to_majuscule(char)
            else:
                # s'éxécute une seule fois pour mettre la
                # première lettre en majuscule
                if premiereLettrePrenom:
                    full_name += to_majuscule(char)
                    premiereLettrePrenom = False
                else:
                    # si c'est une minuscule
                    if 97 <= ord(char) <= 122:
                        # on ajoute juste
                        full_name += char
                    else:
                        # on convertit en minuscule et on ajoute
                        full_name += chr(ord(char) + 32)

    return full_name

def to_majuscule(c : chr)-> chr:
    # on vérifie si ce n'est pas une majuscule
    if ord(c) < 65 or ord(c) > 90:
        # on convertit en majuscule
        c = chr(ord(c) - 32)
    return c

print(full_name_without_functions("véron aUrÈlE"))