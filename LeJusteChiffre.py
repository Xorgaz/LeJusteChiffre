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

"""Tests unitaires"""
# Test unitaire 1 - test la saisie de l'utilisateur vérifie si nombre.
def test_saisie_utilisateur_nombre():
    assert verifier_saisie_utilisateur("123") == True

# Test unitaire 2 - test la saisie de l'utilisateur vérifie si il entre des lettres
def test_saisie_utilisateur_lettre():
    assert verifier_saisie_utilisateur("abc") == False 

# Test unitaire 1 - test si le nombre générer se trouve bien entre 0 et 100
def test_generer_nombre():
    nombre = generer_nombre()
    assert nombre >= 0 and nombre <= 100

test_saisie_utilisateur_nombre
test_saisie_utilisateur_lettre
test_generer_nombre

#Lance le jeu
jeu_du_juste_chiffre()

