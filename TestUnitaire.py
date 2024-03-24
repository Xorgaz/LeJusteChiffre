import LeJusteChiffre
from LeJusteChiffre import generer_nombre, verifier_saisie_utilisateur

"""Tests unitaires"""
# Test unitaire 1 - test la saisie de l'utilisateur vérifie si nombre
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