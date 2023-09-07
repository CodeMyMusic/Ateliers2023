#// PRIX EN FONCTION DU POIDS DE LA LETTRE //#

LETTRE_VERTE = {
    20: 1.16,
    100: 2.32,
    250: 4,
    500: 6,
    1000: 7.5,
    3000: 10.5,
}

LETTRE_PRIORITAIRE = {
    20: 1.43,
    100: 2.86,
    250: 5.26,
    500: 7.89,
    3000: 11.44,
}

ECOPLI = {
    20: 1.14,
    100: 2.28,
    250: 3.92,
}

#// // // // // #

# Types de lettres possibles
possible_types = {
    "lv": LETTRE_VERTE,
    "lp": LETTRE_PRIORITAIRE,
    "eco": ECOPLI
}

types_input = list(possible_types.keys())

def main():
    print("\n-- ENVOI DE LETTRE --\n")

    #// DEBUT SAISIE //#
    
    # INPUT TYPE
    saisieValide = False
    while saisieValide == False:
        type_lettre = input("Entrez le type de la lettre {} :".format(types_input))
        if type_lettre in types_input:
            saisieValide = True
        else:
            print("Type de lettre non reconnu. Vérifiez que vous n'avez pas fait de faute de frappe.")

    # INPUT POIDS
    saisieValide = False
    while saisieValide == False:
        liste_poids = list(possible_types[type_lettre].keys())
        poids = input("Entrez le poids de la lettre (max {} grammes) : ".format(liste_poids[len(liste_poids)-1]))
        try:
            poids = int(poids)
        except:
            print("Le poids doit être de type nombre entier")
        else:
            if (poids <= liste_poids[len(liste_poids)-1]):
                saisieValide = True
            else:
                print("Vous avez dépassé le poids maximum autorisé")

    #// FIN SAISIE //#
            
    prix = trouver_montant_lettre(poids, type_lettre)

    print("Pour une lettre de type {} dont le poids est de {} grammes, le prix est de {} €".format(type_lettre, poids, prix))


def trouver_montant_lettre(poids: int, type_lettre: str) -> int:
    """Trouver le montant de la lettre en fonction du poids et du type

    Args:
        poids (int): le poids de la lettre
        type (str): le type de lettre

    Returns:
        int: le montant de la lettre
    """

    # récupère  type
    dico_poids_prix = possible_types[type_lettre]
    prix = "Prix inconnu"
    trouvePrix = False
    # index dans le dico
    i = 0
    # tant qu'on a pas trouvé le prix et qu'on a pas dépassé la longeur du dico
    while trouvePrix == False and i < len(dico_poids_prix):
        # la clé c'est le poids
        tranche_poids = list(dico_poids_prix.keys())[i]
        if poids <= tranche_poids:
            tranche_prix = dico_poids_prix[tranche_poids]
            prix = tranche_prix
            trouvePrix = True
        else:
            i+=1

    return prix

if __name__ == "__main__":
    main()