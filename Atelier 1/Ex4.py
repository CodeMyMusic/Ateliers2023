# pour la manipulation de date
from datetime import date

# import de la fonction "est_bissextile" pour
# reconnaître les années bissextiles
from Ex2 import est_bissextile

def main():
    test_acces()

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

    print("Vous allez saisir votre date de naissance")
    #// DEBUT SAISIE
    jour = saisir_entier("le jour")
    mois = saisir_entier("le mois")
    annee = saisir_entier("l'année")
    #// FIN SAISIE

    return date(annee, mois, jour)

def age(date_naissance : date) -> int:
    date_today = date.today()

    age = date_today.year - date_naissance.year

    anniv_celebrated = False
    if (date_today.month < date_naissance.month):
        if (date_today.day < date_naissance.day):
            anniv_celebrated = True 

    if not anniv_celebrated:
        age -= 1

    print(age)

    return age

def est_majeur(date_naissance: date) -> bool:
    majeur = True
    if age(date_naissance) < 18:
        majeur = False
    return majeur

def test_acces():
    """Assure la saisie de la date de naissance et 
    determine en fonction de l'age si l'acces est autorisé

    """
    # saisir la date de naissance
    date_naissance = saisir_date_naissance()
    est_majeur(date_naissance)

#--- EXECUTION ---# 
if __name__ == "__main__":
    main()



        
