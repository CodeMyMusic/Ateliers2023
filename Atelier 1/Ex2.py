def main():
    saisieValide = False
    while saisieValide == False:
        annee = input("Entrez une année pour savoir si elle est bissextile :")
        try:
            # on essaie de convertir l'input en nombre réel
            annee = int(annee)
        except:
            # l'input n'est pas un nombre réel
            print("L'annee doit être un nombre entier")
        else:
            saisieValide = True

    # pour afficher le résultat
    afficher(annee, est_bissextile(annee))

    # tests pertinents
    tests()

def afficher(annee: int, bissextile: bool):
    if bissextile:
        print(annee, "est une année bissextile")
    else:
        print(annee, "n'est pas une année bissextile")

def tests():
    for annee in range(RANGE_TEST[0], RANGE_TEST[1]):
        afficher(annee, est_bissextile(annee))

# années à tester (tranche)
RANGE_TEST = [2000, 2025]

ANNEES_BISSEXTILES = [2004, 2008, 2012, 2016, 2020, 2024]

def est_bissextile(annee : int) -> bool: 
    valid = False 
    # si l'annee est divisible par 4
    if annee % 4 == 0:
        # si l'annee n'est ni divisible par ni divisible par 400
        if annee % 100 != 0 and annee % 400 != 0:
            valid = True
    
    return valid



if __name__ == "__main__":
    main()