from Ex2 import est_bissextile

def main():
    jour = saisie_entier("jour")
    mois = saisie_entier("mois")
    annee = saisie_entier("année")
    print(date_est_valide(jour, mois, annee))
    main()

def saisie_entier(type_date : str) -> int:
    """Vérifie que la saisie est un entier

    Args:
        type_date (str): le type de date (jour, mois ou année)

    Returns:
        int: le type de date converti en entier
    """
    saisieValide = False
    while saisieValide == False:
        entier = input(f'Entrez le {type_date}:')
        try:
            # on essaie de convertir l'input en nombre réel
            entier = int(entier)
        except:
            print("Veuillez entrer un nombre entier")
        else:
            saisieValide = True
    return entier

def date_est_valide(jour : int, mois: int, annee: int) -> bool:
    """Teste si une date est valide

    Args:
        jour (int): le jour
        mois (int): le mois
        annee (int): l'année

    Returns:
        bool: si la date est valide ou non
    """
    est_valide = False
    # Si le jour n'est pas nul
    if jour > 0:
        # Si le mois est compris entre 1 et 12
        if 0 < mois < 13:
            # Si c'est le mois de février
            if (mois == 2):
                # Si l'année est bissextile
                if est_bissextile(annee):
                    # Non bissextile il y a maximum 29 jours
                    if jour <= 29:
                        est_valide = True
                else:
                    # Non bissextile il y a maximum 28 jours
                    if jour <= 28:
                        est_valide = True
            # Si ce n'est pas le mois de février
            else:
                if (mois % 2 == 1):
                    if jour <= 31:
                        est_valide = True
                else:
                    if jour <= 30:
                        est_valide = True

    return est_valide

if __name__ == "__main__":
    main()



        
