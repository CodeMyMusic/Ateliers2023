#// PRIX EN FONCTION DU POIDS DE LA LETTRE //#

LETTRE_VERTE = {
    20: 1.16,
    100: 2.32,
    250: 4,
    500: 6,
    1000: 7.5,
    3000: 10.50,
    "Sticker suivi": 0.50
}

LETTRE_PRIORITAIRE = {
    20: 1.43,
    100: 2.86,
    250: 5.26,
    500: 7.89,
    3000: 11.44,
    "Sticker suivi": 0.50
}

ECOPLI = {
    20: 1.14,
    100: 2.28,
    250: 3.92,
    "Sticker suivi": 0.50
}

#// // // // // #

def trouver_montant_lettre(poids: int, type: str) -> int:
    """Trouver le montant de la lettre en fonction du poids et du type

    Args:
        poids (int): le poids de la lettre
        type (str): le type de lettre

    Returns:
        int: le montant de la lettre
    """
    prix = 0
    if type == "LETTRE VERTE":
        for (key, value) in LETTRE_VERTE:
            if poids <= key:
                prix = value

    return prix


prix = trouver_montant_lettre(19, "LETTRE VERTE")

print(prix)
