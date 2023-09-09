# !!!!!!!!
# !!!!!!!! CE QU'IL NE FAUT PAS FAIRE EST DANS CETTE VERSION DE L'EXO !!!!!!!!!!!!
# !!!!!!!!

#/// CONSTANTES ///#

# tranches ou bornes imc associées aux descriptions
INTERPRETATION_IMC_DIC = {
    # une valeur = une borne
    "Dénutrition ou famine": 16.5,
    # deux valeurs = une tranche
    "Maigreur":[16.5, 18.5],
    "Corpulence normale": [18.5, 25],
    "Surpoids": [25, 30],
    "Obsésité modérée": [30, 35],
    "Obsésité sévère": [35, 40],
    "Obésité morbide": 40
}

#////////////#

def main():
    saisieValide = False
    while not saisieValide:
        imc = input("Entrez l'indice de masse corporelle (IMC): ")
        try:
            # on essaie de convertir l'input en nombre réel
            imc = float(imc)
        except:
            # l'input n'est pas un nombre réel
            print("L'IMC doit être de type nombre réel")
        else:
            saisieValide = True

    # on appelle la fonction interpretant l'imc
    description = interpretation_imc(imc)
    print("Catégorie : ", description)
    # pour que l'on puisse essayer aussi longtemps qu'on le souhaite
    main()

def interpretation_imc(imc : int) -> str:
    """Renvoie une description selon l'imc entré

    Args:
        imc (int): l'imc de la personne

    Returns:
        str: l'interpretation de l'imc
    """
    description = ""

    # on met sous forme de liste les tranches/bornes imc
    tranche_imc = list(INTERPRETATION_IMC_DIC.values())
    # tout ce qui est en dessous de cette borne est la 1ere catégorie
    # le seuil min est le premier elmt du dico INTERPRETATION_IMC_DIC
    seuil_min = tranche_imc[0]
    # tout ce qui est au dessus de cette borne est la derniere catégorie
    # le seuil max est le dernier elmt du dico INTERPRETATION_IMC_DIC
    seuil_max = tranche_imc[len(INTERPRETATION_IMC_DIC)-1]

    # on met sous forme de liste les descriptions des catégories
    tranche_description = list(INTERPRETATION_IMC_DIC.keys())

    if imc < seuil_min:
        description = tranche_description[0]
    elif imc > seuil_max:
        description = tranche_description[len(INTERPRETATION_IMC_DIC)-1]
    else:
        # (1) pas de seuil min ni de seuil max donc on retire l'elmt 0
        # et le dernier elmt de la liste
        tranche_imc = tranche_imc[1:-1]
        # bis (1)
        tranche_description = tranche_description[1:-1]

        trouveDescription = False
        # compteur de boucle
        i = 0
        # tant qu'on a pas trouve la description et qu'on a pas dépassé
        # la taille de la liste
        while not trouveDescription and i < len(tranche_imc):
            # la première valeur dans la liste [16.5, 18.5] est le seuil min
            seuil_min = tranche_imc[i][0]
            # la seconde valeur dans la liste [16.5, 18.5] est le seuil max
            seuil_max = tranche_imc[i][1]
            # si l'imc est compris dans ces bornes
            if seuil_min <= imc <= seuil_max:
                # la description correspond au même index pour la liste des
                # tranches imc
                description = tranche_description[i]
                trouveDescription = True
            else:
                i+=1

    return description


if __name__ == "__main__":
    main()