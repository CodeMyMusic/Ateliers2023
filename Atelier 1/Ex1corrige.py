import math

#/// CONSTANTES ///#

# interpretation de l'imc en plsusieurs tranches
INTERPRETATION_IMC_DIC = {
    #tranche de valeurs

    (0, 16.5) : "Dénutrition ou famine",
    (16.5, 18.5) : "Maigreur",
    (18.5, 25) : "Corpulence normale",
    (25, 30) : "Surpoids",
    (30, 35) : "Obsésité modérée",
    (35, 40) : "Obsésité sévère",
    (40, math.inf) : "Obésité morbide"
}

#////////////#

def main():
    saisieValide = False
    while saisieValide == False:
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

def interpretation_imc(imc : float) -> str:
    """Renvoie une description selon l'imc saisi

    Args:
        imc (int): l'imc de la personne

    Returns:
        str: l'interpretation de l'imc
    """
    tranche_imc = list(INTERPRETATION_IMC_DIC.keys())
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
            # on récupère la description
            description = INTERPRETATION_IMC_DIC[tranche_imc[i]]
            trouveDescription = True
        else:
            i+=1

    return description


if __name__ == "__main__":
    main()