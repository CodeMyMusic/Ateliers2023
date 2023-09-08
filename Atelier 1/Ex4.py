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
    """Renvoie l'âge à la date du jour d'après la date de 
    naissance fournie

    Args:
        date_naissance (date): la date de naissance

    Returns:
        int: l'âge
    """
    # date du jour
    date_today = date.today()

    # calcul de l'âge en année (en supposant que
    # l'anniversaire est passé
    age = date_today.year - date_naissance.year

    # on considère l'anniversaire non fêté
    anniv_celebrated = False
    # d'abord on vérifie que le mois de cette année
    # est après ou est le mois de la date de naissance
    if (date_today.month >= date_naissance.month):
        # et on vérifie avec les jours
        if (date_today.day >= date_naissance.day):
            anniv_celebrated = True 

    # donc si l'anniversaire n'a pas été fêté il faut
    # retirer un an à la personne
    if not anniv_celebrated:
        age -= 1

    return age

def est_majeur(date_naissance: date) -> bool:
    """Teste si la personne est majeure en fonction de
    la date du jour et de la date naissance

    Args:
        date_naissance (date): la date de naissance

    Returns:
        bool: majeur ou pas
    """
    majeur = True
    if age(date_naissance) < 18:
        majeur = False
    return majeur

def test_acces():
    """Fonction d'affichage
    Assure la saisie de la date de naissance et 
    determine en fonction de l'age si l'acces est autorisé

    """
    test()
    # saisir la date de naissance
    date_naissance = saisir_date_naissance()
    age = age(date_naissance)
    if est_majeur(date_naissance):
        print(f'Bonjour, vous avez {age} ans, Accès autorisé')
    else:
        print(f'Désolé, vous avez {age}, Accès interdit')

              
def test():
    """Test des fonctions et procédures
    """
    dates_naissances = [
        # random
        date(1997, 5, 2),

        # contexte !! nous sommes le 8 sept 2023

        # meme jour et meme mois qu'hier
        date(2005, 9, 7),
        # meme jour et meme mois qu'aujourd'hui
        date(2005, 9, 8),
        # meme jour et meme mois que demain
        date(2005, 9, 9)
    ]
    for date_naissance in dates_naissances:
        print("{} : {}".format(age(date_naissance), est_majeur(date_naissance)))
    

#--- EXECUTION ---# 
if __name__ == "__main__":
    main()



        
