# Pour la génération de nombres aléatoires
import random

# Réponses classiques du jeu (sans le puit)
game_responses = ['papier', 'pierre', 'ciseaux']

define_winner = {
    "papier": ["pierre", "puit"],
    "ciseaux": "papier",
    "pierre": "ciseaux",
    "puit": ["pierre", "ciseaux"],
}

saisieValide = False
while saisieValide == False:
    jouer_contre_ordinateur = input(
    "Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").lower()
    if jouer_contre_ordinateur == 'o' and jouer_contre_ordinateur == 'n':
        saisieValide = True
    else:
        print("Je n'ai pas compris votre réponse")

# Le joueur veut jouer contre l'ordinateur
if jouer_contre_ordinateur == 'o':
    joueur1 = input("Quel est votre nom ? ")
    print("Bienvenue ", joueur1, " nous allons jouer ensemble \n")
    joueur2 = 'Machine'

# Le joueur veut jouer contre un autre joueur
else:
    joueur1 = input("Quel est votre nom ? ")
    joueur2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenue à vous deux, que le meilleur gagne")

saisieValide = False
while saisieValide == False:
    puit_is_allowed = input("Voulez-vous autoriser le puit ? (O/N) ").lower()
    if puit_is_allowed == 'o' and puit_is_allowed == 'n':
        saisieValide = True
    else:
        print("Je n'ai pas compris votre réponse")

if puit_is_allowed == 'o':
    game_responses.append("puit")

#/ Variables jeu /#

exit_game = False
joueur1_score = 0
joueur2_score = 0
nbr_parties = 0


def get_choix(joueur:str) -> str:
    """Choix du joueur

    Args:
        joueur (str): le joueur

    Returns:
        str: choix du joueur
    """
    saisieValide = False

    while saisieValide == False:
        saisieValide = input("{}, faîtes votre choix parmi {}: ".format(joueur, game_responses)
                ).lower()
        if saisieValide in game_responses:
            saisieValide = True
        else:
            print("Je n'ai pas compris votre réponse")

    return saisieValide

# TEST DU GAGNANT

def teste_gagne(choix1: str, choix2: str) -> bool:
    """Teste si le choix est gagnant en utilisant le dictionnaire define_winner

    Args:
        choix1 (str): choix principal
        choix2 (str): choix secondaire

    Returns:
        bool: le choix principal est-il gagnant face au choix secondaire
    """
    est_gagnant = False
    # Si l'objet 2 est dans le tableau des objets perdants contre l'objet 1
    # cela fonctionne même si "define_winner[obj1]" n'est pas une liste !
    perdants_contre_choix1 = define_winner[choix1]
    if choix2 in perdants_contre_choix1:
        est_gagnant = True

    return est_gagnant


while exit_game == False:
    # On incrémente le nombre de parties
    nbr_parties += 1

    joueur1_choix = get_choix(joueur1)

    # Si le joueur 2 est un ordinateur
    if jouer_contre_ordinateur == 'o':
        # on choisi un index au hasard (utiliser la longueur du tableau)
        joueur2_choix = game_responses[random.randint(0, len(game_responses))]
    # Sinon
    else:
        joueur2_choix = get_choix(joueur2)

    # On affiche les choix de chacun
    print("On récapitule :", joueur1, "a choisi", joueur1_choix,
          "et", joueur2, "a choisi", joueur2_choix, "\n")
    
    # on va éviter de faire des tonnes de vérification et vérifier tout de suite s'ils ont
    # choisi la même la réponse
    if joueur1_choix == joueur2_choix:
        print("Les deux joueurs sont ex-aequo")
    
    else:  
        # On teste si l'objet choisi par le joueur 1 gagne contre l'objet du joueur 2
        if teste_gagne(joueur1_choix, joueur2_choix) == True:
            joueur1_score += 1
            print("le gagnant est", joueur1)

        # comme les deux joueurs ont des réponses différentes (voir au dessus ligne 99)
        # et que l'on perd forcément contre un objet à pierre caillou ciseaux,
        # le joueur 1 perd et le joueur 2 gagne
        else: 
            joueur2_score += 1
            print("le gagnant est", joueur2)                 
        
    print("Les scores à l'issue de cette manche sont donc",
          joueur1, joueur1_score, "et", joueur2, joueur2_score, "\n")


    if nbr_parties < 5:
        exit_game = False
    else:
        exit_game = True

    if nbr_parties< 5:
        # On propose au joueur(s) de rejouer
        continuer= input(
            "Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(joueur1, joueur2))
        # Si la réponse est non valide
        if continuer!= 'o' and continuer!= 'n':
            exit_game = True
            print("Vous ne répondez pas à la question, on continue")
            continuer= input(
                "Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? ").lower()
        if continuer== 'o':
            exit_game = False
        else:
            exit_game = True


print("Merci d'avoir joué ! A bientôt")