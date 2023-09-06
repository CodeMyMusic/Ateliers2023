# Pour la génération de nombres aléatoires
import random

# Réponses ouvertes possibles
possible_open_resonses = ['o','n']

# Toutes les réponses
all_game_resonses = ['papier', 'caillou', 'ciseaux', 'puit']

# Réponses classiques
classic_game_responses = ['papier', 'caillou', 'ciseaux']

# Question
cpo = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").lower()

# Tant que la réponse n'est pas comprise
while cpo not in possible_open_resonses:
    print("Je n'ai pas compris votre réponse")
    cpo = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").lower()

# Si le joueur veut jouer contre l'ordinateur
if cpo == 'o':
    joueur1 = input("Quel est votre nom ? ")
    print("Bienvenue ", joueur1, " nous allons jouer ensemble \n")
    joueur2 = 'Machine'

# Si le joueur veut jouer contre un autre joueur
else:
    joueur1 = input("Quel est votre nom ? ")
    print("Bienvenu ", joueur1, " nous allons jouer ensemble")
    joueur2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu ", joueur2, " nous allons jouer ensemble \n")

c = True
p2 = 0
s1 = 0
np = 0

def get_game_answer(joueur):
    response = input(
        "{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=joueur)
        ).lower()
    while response not in classic_game_responses:
        print("Joueur ", joueur)
        response = input("Faîtes votre choix parmi (pierre, papier, ciseaux): "
            ).lower()
                
    return response

while c == True:
    np += 1
    joueur1_answer = get_game_answer(joueur1)

    # Si le joueur 2 est un ordinateur
    if cpo == 'o':
        joueur2_answer = ['papier', 'pierre', 'ciseaux'][random.randint(0, 2)]

    else:
        joueur2_answer = get_game_answer(joueur2)

    # On affiche les choix de chacun
    print("Si on récapitule :", joueur1, joueur1_answer, "et", joueur2, joueur2_answer, "\n")

    # On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if c1 == 'papier' and e2 == 'papier':
        w12 = "aucun de vous, vous être ex æquo"
        s1 = s1 + 0
        p2 = p2 + 0
        print("le gagnant est", w12)
        print("Les scores à l'issue de cette manche sont donc",
              joueur1, s1, "et", joueur2, p2, "\n")

    if c1 == 'pierre' and e2 == 'papier':
        w12 = joueur2
        s1 = s1 + 0
        p2 = p2 + 1
        print("le gagnant est", w12)
        print("Les scores à l'issue de cette manche sont donc",
              joueur1, s1, "et", joueur2, p2, "\n")

    if c1 == 'pierre' and e2 == 'pierre':
        w12 = "aucun de vous, vous être ex æquo"
        s1 = s1 + 0
        p2 = p2 + 0
        print("le gagnant est", w12)
        print("Les scores à l'issue de cette manche sont donc",
              joueur1, s1, "et", joueur2, p2, "\n")

    if c1 == 'pierre' and e2 == 'ciseaux':
        w12 = joueur1
        s1 = s1 + 1
        p2 = p2 + 0
        print("le gagnant est", w12)
        print("Les scores à l'issue de cette manche sont donc",
              joueur1, s1, "et", joueur2, p2, "\n")

    if c1 == 'papier' and e2 == 'ciseaux':
        w12 = joueur2
        s1 = s1 + 0
        p2 = p2 + 1
        print("le gagnant est", w12)
        print("Les scores à l'issue de cette manche sont donc",
              joueur1, s1, "et", joueur2, p2, "\n")

    if c1 == 'papier' and e2 == 'pierre':
        w12 = joueur1
        s1 = s1 + 1
        p2 = p2 + 0
        print("le gagnant est", w12)
        print("Les scores à l'issue de cette manche sont donc",
              joueur1, s1, "et", joueur2, p2, "\n")

    if c1 == 'ciseaux' and e2 == 'pierre':
        w12 = joueur2
        s1 = s1 + 0
        p2 = p2 + 1
        print("le gagnant est", w12)
        print("Les scores à l'issue de cette manche sont donc",
              joueur1, s1, "et", joueur2, p2, "\n")

    if c1 == 'ciseaux' and e2 == 'ciseaux':
        w12 = "aucun de vous, vous être ex æquo"
        s1 = s1 + 0
        p2 = p2 + 0
        print("le gagnant est", w12)
        print("Les scores à l'issue de cette manche sont donc",
              joueur1, s1, "et", joueur2, p2, "\n")

    if c1 == 'ciseaux' and e2 == 'papier':
        w12 = joueur1
        s1 = s1 + 1
        p2 = p2 + 0
        print("le gagnant est", w12)
        print("Les scores à l'issue de cette manche sont donc",
              joueur1, s1, "et", joueur2, p2, "\n")

    if np == 1 or np == 2 or np == 3 or np == 4:
        c = True
    if np == 5:
        c = False

    if np == 1 or np == 2 or np == 3 or np == 4:
        # On propose de c ou de s'arrêter
        go = input(
            "Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(joueur1, joueur2))
        # Tant que la réponse n'est pas comprise
        if go not in possible_open_resonses:
            c = True
            print("Vous ne répondez pas à la question, on continue")
            go = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").lower()
        if go == 'o':
            c = True
        else:
            c = False


if c == False:
    print("Merci d'avoir joué ! A bientôt")
