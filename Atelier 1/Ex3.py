def main():
    print("Programme de résolution d'équations du second degré.\nL'équation est de type ax²+bx+c où a, b et c sont les coefficients et a != 0")
    verifier_saisie()
    saisieValide = False
    while saisieValide == False:
        a = input("Entrez a")
        try:
            # on essaie de convertir l'input en nombre réel
            a = int(a)
        except:
            # l'input n'est pas un nombre réel
            print("L'annee doit être un nombre entier")
        else:
            saisieValide = True

def verifier_saisie():



if __name__ == "__main__":
    main()