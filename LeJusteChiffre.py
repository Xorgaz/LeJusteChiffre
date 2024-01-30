# Le Juste Chiffre
# Le but du jeu est de trouver le chiffre généré aléatoirement.

import random

def generer_nombre():
    """
    Retourne un nombre aléatoire entre 0 et 100.
    """
    return random.randint(0, 100)

def jouer():
    """
    Gère le jeu LeJusteChiffre.
    """
    # Générer un nombre aléatoire.
    nombre_secret = generer_nombre()

    # Demander à l'utilisateur de deviner le nombre.
    nombre_propose = input("Devinez le nombre : ")

    # Comparer le nombre proposé au nombre secret.
    while nombre_propose != nombre_secret:
        if nombre_propose < nombre_secret:
            print("Le nombre est plus grand.")
        elif nombre_propose > nombre_secret:
            print("Le nombre est plus petit.")
        nombre_propose = input("Devinez à nouveau : ")

    # Féliciter l'utilisateur s'il a trouvé le bon nombre.
    print("Bravo ! Vous avez trouvé le nombre secret.")

if __name__ == "__main__":
    jouer()
