import random
import pytest


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
    nbalea = generer_nombre()
    print(nbalea)
    print("Bienvenue dans le jeu du Juste Chiffre!")
    while True:
        essai = input("Devinez le nombre entre 0 et 100: ")
        if not verifier_saisie_utilisateur(essai):
            print("Veuillez entrer un nombre valide.")
            continue 
        essai = int(essai)
        if essai < nbalea:
            print("Trop petit!")
        elif essai > nbalea:
            print("Trop grand!")
        else:
            print("Félicitations! Vous avez deviné le nombre correctement!")
            break

# Test unitaire 1
def test_verifier_entree_utilisateur():
    assert verifier_saisie_utilisateur("123") == True
    assert verifier_saisie_utilisateur("abc") == False

# Test unitaire 2
def test_generer_nombre():
    nombre = generer_nombre()
    assert nombre >= 0 and nombre <= 100

jeu_du_juste_chiffre()