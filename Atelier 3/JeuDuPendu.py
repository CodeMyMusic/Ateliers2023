from random import *

def places_lettre(ch: str, mot: str)-> list:
    """Renvoie la ou les places d'une lettre dans un mot

    Args:
        ch (str): la lettre
        mot (str): le mot

    Returns:
        list: la liste des indices qu'occupe la lettre
    """
    len_mot = len(mot)
    places = []
    for i in range(len_mot):
        if mot[i] == ch:
            places.append(i)
    return places

def outputStr(mot: str, lpos: list)-> str:
    """Renvoie le mot, masqué partiellement ou
    totalement selon les indices présents dans lpos 

    Args:
        mot (str): le mot
        lpos (list): la liste des indices non masqués

    Returns:
        str: le mot masqué
    """
    masked_word = ['-']*len(mot)
    for elmt in lpos:
        masked_word[elmt] = mot[elmt]
    return masked_word

def affiche_pendu(nbErreurs):
    visuel_pendu = [
        "|---] ",
        "| 0 ",
        "| T ",
        "|/ \\",
        "|_____"
    ]
    for i in range(nbErreurs):
        print(visuel_pendu[i])

def runGame():
    liste_mots = ["pastèque", "personne", "environnement", "pélican", "cuistre"]

    # on prend au hasard un mot dans la liste
    mot_a_trouve = choice(liste_mots)

    # cette liste vide représente les lettres trouvées dans le mot
    lettres_trouvees = []

    # compteur lettres trouvées
    nb_lettres_trouvees = 0

    # nb lettres mot à trouver
    nb_lettres_mot = len(mot_a_trouve)

    mot_masque = outputStr(mot_a_trouve, lettres_trouvees)

    # compteur erreurs
    nbErreur = 0

    print("Bonjour, aujourd'hui nous allons jouer au pendu :)")
    print("Voici le mot à trouver : ", end="")

    # tant que l'utilisateur n'a pas atteint 5 erreurs ni trouvé le mot
    while nbErreur < 5 and nb_lettres_trouvees < nb_lettres_mot:
        print("".join(mot_masque))
        lettre = input("Entrez une lettre :")
        lettre_indice = places_lettre(lettre, mot_a_trouve)
        if lettre_indice:
            for elmt in lettre_indice:
                lettres_trouvees.append(elmt)
                #on incrémente notre compteur de lettres trouvées
                nb_lettres_trouvees += 1

            mot_masque = outputStr(mot_a_trouve, lettres_trouvees)
            print('Vous avez trouvé la lettre {}'.format(lettre))
        else:
            print('La lettre "{}" n\'est pas présente dans le mot.'.format(lettre))
            nbErreur += 1
        print("\n* * * *")
        affiche_pendu(nbErreur)
        print("* * * *")
        print("")

    if nbErreur == 5:
        print("Vous avez perdu ! ", end="")
    else:
        print("Félications vous avez gagné ! ", end="")
    
    print("Le mot était:", mot_a_trouve)

runGame()


