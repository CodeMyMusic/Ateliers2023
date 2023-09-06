# Pour la génération de nombres aléatoires
import random

# Réponses au jeu
game_responses = ['papier', 'pierre', 'ciseaux']


define_winner = {
    "papier": ["pierre", "puit"],
    "ciseaux": "papier",
    "pierre": "ciseaux",
    "puit": ["pierre", "ciseaux"],
}

# Question
cpo = input(
    "Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").lower()

# Tant que la réponse n'est pas comprise
while cpo != 'o' and cpo != 'n':
    print("Je n'ai pas compris votre réponse")
    cpo = input(
        "Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").lower()

# Si le joueur veut jouer contre l'ordinateur
if cpo == 'o':
    joueur1 = input("Quel est votre nom ? ")
    print("Bienvenue ", joueur1, " nous allons jouer ensemble \n")
    joueur2 = 'Machine'

# Si le joueur veut jouer contre un autre joueur
else:
    joueur1 = input("Quel est votre nom ? ")
    print("Bienvenue ", joueur1, " nous allons jouer ensemble")
    joueur2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenue ", joueur2, " nous allons jouer ensemble \n")

puit_is_allowed = input("Voulez-vous autoriser le puit ? (O/N) ").lower()

# Tant que la réponse n'est pas comprise
while puit_is_allowed != 'o' and puit_is_allowed != 'n':
    print("Je n'ai pas compris votre réponse")
    puit_is_allowed = input("Voulez-vous autoriser le puit ? (O/N) ").lower()

if puit_is_allowed == 'o':
    game_responses.append("puit")

# Pour l'affichage des choix
choix = "("
for i in game_responses:
    choix = choix + i + ","
choix += ")"

exit_game = False
joueur1_score = 0
joueur2_score = 0
nbr_parties = 0


def get_game_answer(joueur):
    response = input(
        "{nom} faîtes votre choix parmi {choix}: ".format(
            nom=joueur, choix=choix)
    ).lower()
    while response not in game_responses:
        print("Je n'ai pas compris votre réponse")
        response = input("Faîtes votre choix parmi", choix, ": "
                         ).lower()

    return response


while exit_game == False:
    nbr_parties += 1
    joueur1_answer = get_game_answer(joueur1)

    # Si le joueur 2 est un ordinateur
    if cpo == 'o':
        joueur2_answer = ['papier', 'pierre', 'ciseaux'][random.randint(0, 2)]

    else:
        joueur2_answer = get_game_answer(joueur2)

    # On affiche les choix de chacun
    print("On récapitule :", joueur1, "a choisi", joueur1_answer,
          "et", joueur2, "a choisi", joueur2_answer, "\n")

    # Dans le dictionnaire "define_winner", on regarde quelle clé est associée à la réponse du joueur
    # la réponse du joueur appartient à la liste de valeurs du dico
    joueur1_perd_contre = list(define_winner.keys())[list(
        define_winner.values()).index(joueur1_answer)]

    # Dans le dictionnaire "define_winner", on regarde quelle valeur est associée à la réponse du joueur
    # la réponse du joueur appartient à la liste de clés du dico
    joueur1_gagne_contre = define_winner[joueur1_answer]

    # Si le joueur1 perd contre le choix du joueur2
    if joueur1_perd_contre == joueur2_answer:
        joueur2_score += 1
        print("le gagnant est", joueur2)
    # Si le joueur2 gagne contre le choix du joueur2
    elif joueur1_gagne_contre == joueur2_answer:
        joueur1_score += 1
        print("le gagnant est", joueur1)
    # Sinon cela veut dire que les joueurs sont ex_aequo
    else:
        print("Les deux joueurs sont ex_aequo")

    print("Les scores à l'issue de cette manche sont donc",
          joueur1, joueur1_score, "et", joueur2, joueur2_score, "\n")


    if nbr_parties < 5:
        exit_game = False
    else:
        exit_game = True

    if nbr_parties< 5:
        # On propose au joueur(s) de rejouer
        go = input(
            "Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(joueur1, joueur2))
        # Si la réponse est non valide
        if go != 'o' and go != 'n':
            exit_game = True
            print("Vous ne répondez pas à la question, on continue")
            go = input(
                "Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").lower()
        if go == 'o':
            exit_game = False
        else:
            exit_game = True


print("Merci d'avoir joué ! A bientôt")
