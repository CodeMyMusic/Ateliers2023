from random import *

def places_lettre(ch: str, mot: str)-> list:
    """Renvoie la ou les places d'une lettre dans un mot

    Args:
        ch (str): la lettre
        mot (str): le mot

    Returns:
        list: la liste des indices qu'occupe la lettre
    """
    liste_places = []
    for i in range(len(mot)):
        if mot[i] == ch:
            liste_places.append(i)
    return liste_places


def outputStr(mot: str, lpos: list)-> str:
    """Renvoie un mot totalement ou partiellement masqué par des tirets,
    selon la liste des indices des caractères à afficher "lpos"

    Args:
        mot (str): le mot
        lpos (list): la liste des indices des caractères à afficher

    Returns:
        str: le mot masqué totalement ou partiellement par des tirets
    """
    masked_word = ['-']*len(mot)
    for indice_a_afficher in lpos:
        masked_word[indice_a_afficher] = mot[indice_a_afficher]
    return "".join(masked_word)


def affiche_pendu(nbErreurs: int):
    """Affiche le pendu selon le nombre d'erreurs

    Args:
        nbErreurs (int): le nombre d'erreurs
    """
    visuel_pendu = [
        "|---] ",
        "| 0 ",
        "| T ",
        "|/ \\",
        "|_____"
    ]
    for i in range(len(visuel_pendu)-nbErreurs, len(visuel_pendu)):
        print(visuel_pendu[i])


# JEU
def runGame():
    liste_mots = ["pastèque", "personne", "environnement", "pélican", "cuistre"]

    # on prend au hasard un mot dans la liste
    mot_a_trouve = choice(liste_mots)

    # cette liste vide représente les lettres trouvées dans le mot
    indices_lettres_trouvees = []

    # compteur lettres trouvées
    nb_lettres_trouvees = 0

    # nb lettres mot à trouver
    nb_lettres_mot_ = len(mot_a_trouve)

    mot_masque = outputStr(mot_a_trouve, indices_lettres_trouvees)

    # compteur erreurs
    nbErreur = 0

    MAX_ERREURS = 5

    print("Bonjour, aujourd'hui nous allons jouer au pendu :)")
    print("Voici le mot à trouver : ", end="")

    # tant que l'utilisateur n'a pas atteint 5 erreurs ni trouvé le mot
    while nbErreur < MAX_ERREURS and nb_lettres_trouvees < nb_lettres_mot_:
        print(mot_masque)
        lettre = input("Entrez une lettre :")
        lettre_indice = places_lettre(lettre, mot_a_trouve)
        if lettre_indice:
            for elmt in lettre_indice:
                indices_lettres_trouvees.append(elmt)
                #on incrémente notre compteur de lettres trouvées
                nb_lettres_trouvees += 1

            mot_masque = outputStr(mot_a_trouve, indices_lettres_trouvees)
            print('Vous avez trouvé la lettre {}'.format(lettre))
        else:
            print('La lettre "{}" n\'est pas présente dans le mot.'.format(lettre))
            nbErreur += 1
        print("\n* * * *")
        affiche_pendu(nbErreur)
        print("* * * *")
        print("")

    if nbErreur == MAX_ERREURS:
        print("Vous avez perdu ! ", end="")
    else:
        print("Félications vous avez gagné ! ", end="")
    
    print("Le mot était:", mot_a_trouve)


# MAIN
def main():
    runGame()


if __name__ == "__main__":
    main()


