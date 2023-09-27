import os
from random import *
import math

from JeuDuPendu import places_lettre, outputStr, affiche_pendu

# On se met dans le même répertoire que le script python 
# car c'est que là se trouve le fichier à ouvrir
os.chdir(os.getcwd()+"\\Atelier_3")

def choose_difficulty() -> (int, int):
    """Demande à l'utilisateur de choisir une difficulté
    et renvoie une borne représentant la taille min et
    taille max des mots inclus.

    Args:
        tuple: un doublet représentant la taille min et
    taille max des mots inclus.
    """
    print("Ce jeu peut se jouer dans 3 modes de difficulté :")
    print("(0) le mot ne contient pas plus de 6 lettres")
    print("(1) le mot contient 7 ou 8 lettres")
    print("(2) le mot contient plus de 8 lettres")  
    difficulties = {
        0: (0, 6),
        1: (7, 8),
        2: (9, math.inf)
    }

    valide = False
    while not valide:
        nb_difficulty = input("Entrez le niveau de difficulté: ")
        try:
            nb_difficulty = int(nb_difficulty)
        except(ValueError):
            print("Le niveau de difficulté doit être un entier !")
        else:
            # si le niveau de difficulté n'est pas dans la borne [0, 2]
            if nb_difficulty > 2 or nb_difficulty < 0:
                print("Le nombre que vous avez entré n'est pas dans la borne !")
            else:
                valide = True

    return difficulties[nb_difficulty]


def build_list(fileName: str)-> list:
    """Renvoie la liste de mots contenue dans un fichier

    Args:
        fileName (str): le nom du fichier

    Returns:
        list: la liste de mots
    """
    # ouvre le fichier en lecture
    fichier = open(fileName, "r", encoding='utf-8')
    # liste comprenant chaque ligne du fichier
    lst_lines = fichier.readlines()
    liste_mots = []
    for ligne in lst_lines:
        lst_tokens = ligne.split(None)
        # on évalue s'il y a un deuxième élément (on évite de tester
        # la taille de la liste pour gagner du temps)
        try:
            lst_tokens[1]
            # 
            liste_mots.append(" ".join(lst_tokens).lower())
        # s'il n'y pas de deuxième élément, on intercepte l'erreur
        # index out of range
        except(IndexError):
            liste_mots.append(lst_tokens[0].lower())
        
    return liste_mots


def build_dict_find_max_len(lst_mots: list) -> (dict, int):
    """Crée un dictionnaire où les clés représentent le nombre
    de lettres du ou des mots correspondants, les mots correspondants
    sont dans une liste qui est la valeur de la clé

    Args:
        lst_mots (list): _description_

    Returns:
        tuple: un doublet contenant le dictionnaire et 
        le nombre de lettres maximum dans ce dico
    """
    dict_mot = {}
    max_words_len = 0
    # on parcourt la liste de mots
    for i in range(len(lst_mots)):
        mot = lst_mots[i]
        len_mot = len(mot)
        if len_mot > max_words_len:
            max_words_len = len_mot
        try:
            # on teste si la clé existe
            key = dict_mot[len(mot)]
        except(KeyError):
            # sinon, on crée une liste associée à la clé, contenant le mot
            # la clé est donc créée
            dict_mot[len(mot)] = [mot]
        else:
            # si la clé existe on peut lui ajouter le mot dans sa liste
            key.append(mot)
    return dict_mot, max_words_len


def select_word(dico_mots: dict, difficulty: (int, int)) -> str:
    """Choisit un mot au hasard dans le dico selon la difficulté

    Args:
        dico (dict): le dico
        difficulty (doublet): une borne représentant la taille
        des mots, sous forme (min_longueur_mot, max_longueur_mot)

    Returns:
        str: le mot choisi au hasard
    """
    dico_mots, max_words_len = dico_mots

    # par défaut on parcourt dans le sens croissant
    sens = 1

    # on extrait le doublet en min_val et max_val
    min_val, max_val = difficulty

    # on part de la plus petite longueur
    len_mot = min_val

    lst_mots_difficulte = []
    while len_mot <= max_val and len_mot <= max_words_len:
        # on teste s'il y a une valeur associée à la longueur du mot
        try:
            liste_mot_same_len = dico_mots[len_mot]
        # sinon on passe
        except(KeyError):
            pass
        # il y a déjà une valeur associée
        else:
            # la valeur en question est une liste
            for mot in liste_mot_same_len:
                lst_mots_difficulte.append(mot)
        len_mot += 1

    # retourne un mot au hasard dans la liste
    return choice(lst_mots_difficulte)

   
# JEU
def runGame():
    liste_mots = build_list("capitales.txt")

    tri_mots_max_len = build_dict_find_max_len(liste_mots)

    print("Bonjour, aujourd'hui nous allons jouer au pendu :)")

    difficulty = choose_difficulty()
    
    mot_a_trouve = select_word(tri_mots_max_len, difficulty)

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

runGame()







