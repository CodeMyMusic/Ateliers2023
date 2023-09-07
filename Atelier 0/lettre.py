#// PRIX EN FONCTION DU POIDS DE LA LETTRE //#

LETTRE_VERTE = {
    20: 1.16,
    100: 2.32,
    250: 4,
    500: 6,
    1000: 7.5,
    3000: 10.50,
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

def main():
    print("\n-- ENVOI DE LETTRE --\n")

    #// DEBUT SAISIE //#

    # ajouter options
    # ne pas embeter
    # rajouter une limite

    saisieValide = False
    while saisieValide == False:
        poids = input("Entrez le poids de la lettre : ")
        try:
            poids = int(poids)
        except:
            print("Le poids doit être de type nombre entier")
        else:
            saisieValide = True

    saisieValide = False
    while saisieValide == False:
        type_lettre = input("Entrez le type de la lettre :").upper()
        if type_lettre in possible_types:
            saisieValide = True
        else:
            print("Type de lettre non reconnu. Vérifiez que vous n'avez pas fait de faute de frappe.")

    #// FIN SAISIE //#
            
    prix = trouver_montant_lettre(poids, type_lettre)

    print("Pour une lettre de type {} dont le poids est de {}grammes, le prix est de {}€".format(type_lettre, poids, prix))


# Types de lettres possibles
possible_types = {
    "LETTRE VERTE": LETTRE_VERTE,
    "LETTRE PRIORITAIRE": LETTRE_PRIORITAIRE,
    "ECOPLI": ECOPLI
}

def trouver_montant_lettre(poids: int, dico_type_lettre: str) -> int:
    """Trouver le montant de la lettre en fonction du poids et du type

    Args:
        poids (int): le poids de la lettre
        type (str): le type de lettre

    Returns:
        int: le montant de la lettre
    """

    # récupère le dico associé au type
    dico_type_lettre = possible_types[type_lettre]
    prix = "Prix inconnu"
    trouvePrix = False
    # index dans le dico
    i = 0
    while trouvePrix == False and i < len(dico_type_lettre):
        # la clé c'est le poids
        tranche_poids = list(dico_type_lettre.keys())[i]
        if poids <= tranche_poids:
            tranche_prix = dico_type_lettre[tranche_poids]
            prix = tranche_prix
            trouvePrix = True
        else:
            i+=1

    return prix

if __name__ == "__main__":
    main()