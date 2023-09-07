import math

def main():
    print("Programme de résolution d'équations du second degré.\nL'équation est de type ax²+bx+c où a, b et c sont les coefficients et a != 0")
    # a nombre reel doit etre different de 0 (True)
    a = gerer_saisie_nbr_reel("a", True)
    b = gerer_saisie_nbr_reel("b")
    c = gerer_saisie_nbr_reel("c")
    print(solution_equation(a, b, c))

def gerer_saisie_nbr_reel(nom_nbr: str, is_not_zero = False) -> float:
    """Gère la saisie d'un nombre réel

    Args:
        is_not_zero (bool): Si le nombre réel ne peut 
        pas être égal à zéro

    Returns:
        float: renvoie un nombre réel
    """
    nbr = 0
    saisieValide = False
    while saisieValide == False:
        nbr = input(f'Entrez {nom_nbr} :')
        try:
            # on essaie de convertir l'input en nombre réel
            nbr = int(nbr)
        except:
            # l'input n'est pas un nombre réel
            print("Vous n'avez pas entré un nombre réel")
        else:
            if is_not_zero:
                if nbr != 0:
                    saisieValide = True
                else:
                    print(f'{nom_nbr} doit être différent de 0')
            else:
                saisieValide = True

    return nbr

def discriminant(a: float, b: float, c: float):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_
        c (_type_): _description_

    Returns:
        _type_: _description_
    """
    return b*b - 4*a*c

def racine_unique(a: float, b: float) -> int:
    """Calcule la racine uniqe

    Args:
        a (float): le coef a
        b (float): le coef b

    Returns:
        int: renvoie la racine unique calculée
    """
    return (-b)/(2*a)

def racine_double(a:float, b:float, delta:float, num:int) -> float:
    """Calcule la racine

    Args:
        a (float): le coef a
        b (float): le coef b
        delta (float): le discriminant calculé
        num (int): le numéro de la racine

    Returns:
        foat: la racine calculée
    """
    if num == 1:
        racine = ((-b)+math.sqrt(delta))/(2*a)
    else:
        racine = ((-b)-math.sqrt(delta))/(2*a)
    return racine

def str_equation(a: float, b: float, c: float) -> str:
    """Affiche l'équation

    Args:
        a (float): le coef a
        b (float): le coef b
        c (float): le coef c

    Returns:
        str: l'équation
    """
    return f'{a}x² + {b}x + {c} = 0'

def solution_equation(a: float, b: float, c: float) -> str:
    """Trouve la solution de l'équation et renvoie le message final

    Args:
        a (float): le coef a
        b (float): le coef b
        c (float): le coef c

    Returns:
        str: la solution
    """
    message = "Solution de l'équation {} :\n".format(str_equation(a, b, c))
    message += equation(a, b, c)
    return message

def equation(a: float, b:float, c:float) -> str:
    """Renvoie la solution de l'équation

    Args:
        a (float): le coef a
        b (float): le coef b
        c (float): le coef c

    Returns:
        str: la solution de l'équation
    """
    delta = discriminant(a, b, c)
    solution = ""

    if delta < 0:
        solution = "Aucune solution réelle"
    elif delta == 0:
        solution = "Racine unique : x = " + str(racine_unique(a, b))
    else:
        solution = "Deux racines :\n"
        solution += "x1 = " + str(racine_double(a, b, delta, 1)) + "\n"
        solution += "x2 = " + str(racine_double(a, b, delta, 2))
    
    return solution


if __name__ == "__main__":
    main()