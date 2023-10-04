def is_mail(str_arg: str) -> (int, int):
    """Renvoie un tuple déterminant la validité
    d'un mail str_arg

    Args:

        str_arg (str): le mail
        tuple: le message de validité
    """

    trouveCorps = False
    trouveDomaine = False
    message = (1, 'x')
    len_arg = len(str_arg)
    if str_arg[0] == '.':
        message = (0, 1)
    else:
        valide = True
        i = 0
        while i < len_arg and valide:
            c = str_arg[i]
            if not trouveCorps:
                if not majuscule(c) and not minuscule(c) and c != "-" and c != "_":
                    if i < len_arg-2:
                        next_c = str_arg[i+1]
                    else:
                        next_c = 0
                    if c == '.':
                        if next_c == '.':
                            valide = False
                            message = (0, 1)
                    if c == "@":
                        if i >= 1:
                            if str_arg[i-1] == ".":
                                message = (0, 1)
                                valide = False
                            else:
                                trouveCorps = True
                        else:
                            message = (0, 1)
                            valide = False
            else:
                if c == "@" or c == ".":
                    message = (0, 3)
                
            i += 1
        if not trouveCorps:
            message = (0, 2)

    return message


def majuscule(c: chr) -> chr:
    # si c'est une majuscule
    return 65 <= ord(c) <= 90


def minuscule(c: chr) -> chr:
    # si c'est une minuscule
    return 97 <= ord(c) <= 122


def tester():
    v1 = "bisgambiglia_paul@univ-corse.fr"
    v2 = "bisgambiglia_paulOuniv-corse.fr"
    v3 = "bisgambiglia_paul@univ-corsePOINTfr"
    v4 = "@univ-corse.fr"

    print(v1, is_mail(v1))
    print(v2, is_mail(v2))
    print(v3, is_mail(v3))
    print(v4, is_mail(v4))

def main():
    tester()


if __name__ == "__main__":
    main()
