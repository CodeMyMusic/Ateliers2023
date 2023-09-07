# pour la manipulation de date
from datetime import date

# import de la fonction "est_bissextile" pour
# reconnaître les années bissextiles
from Ex2 import est_bissextile

def main():
    test_acces()
    main()

def saisir_entier(chose : str) -> int:
    """Vérifie que la saisie est un entier

    Args:
        type_date (str): le type de date (jour, mois ou année)

    Returns:
        int: le type de date converti en entier
    """
    saisieValide = False
    while saisieValide == False:
        # saisie
        entier = input(f'Entrez {chose} : ')
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

def saisir_date_naissance() -> date:
    """Demande la date de naissance à l'utilisateur

    Returns:
        date: la date de naissance (jour, mois, année)
    """
    #// DEBUT SAISIE
    jour = saisir_entier("le jour")
    mois = saisir_entier("le mois")
    annee = saisir_entier("l'année")
    #// FIN SAISIE

    return date(annee, mois, jour)

def age(date_naissance : date) -> int:
    print(date.today().day - date_naissance.day) 

def test_acces():
    """Assure la saisie de la date de naissance et 
    determine en fonction de l'age si l'acces est autorisé

    """
    # saisir la date de naissance
    date_naissance = saisir_date_naissance()
    age(date_naissance)

#--- EXECUTION ---# 
if __name__ == "__main__":
    main()



        
