import random

def generer_nombre():
    """Génère un nombre aléatoire entre 0 et 100."""
    return random.randint(0, 100)

def verifier_saisie_utilisateur(saisie):
    """Vérifie si l'entrée de l'utilisateur est un nombre."""
    try:
        int(saisie)
        return True
    except ValueError:
        return False

def jeu_du_juste_chiffre():
    """Fonction principale du jeu."""
    nb_aleatoire = generer_nombre()
    print("Bienvenue dans le jeu du Juste Chiffre !")
    print("Devinez un nombre entre 0 et 100.")

    while True:
        essai = input("Entrez votre proposition : ")
        if not verifier_saisie_utilisateur(essai):
            print("Veuillez entrer un nombre valide.")
            continue

        essai = int(essai)
        if essai < nb_aleatoire:
            print("Trop petit ! Essayez encore.")
        elif essai > nb_aleatoire:
            print("Trop grand ! Essayez encore.")
        else:
            print("Félicitations ! Vous avez deviné le nombre correctement !")
            break

# Si ce script est exécuté directement, lancez le jeu
if __name__ == "__main__":
    jeu_du_juste_chiffre()
