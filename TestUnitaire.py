import pytest
from LeJusteChiffre import generer_nombre, verifier_saisie_utilisateur

# Test unitaire pour vérifier si l'entrée de l'utilisateur est un nombre valide
def test_verifier_saisie_utilisateur():
    assert verifier_saisie_utilisateur("123") == True
    assert verifier_saisie_utilisateur("abc") == False
    assert verifier_saisie_utilisateur("12.5") == False

# Test unitaire 2 - test la saisie de l'utilisateur vérifie si il entre des lettres
def test_saisie_utilisateur_lettre():
    assert verifier_saisie_utilisateur("abc") == False 

# Test unitaire 1 - test si le nombre générer se trouve bien entre 0 et 100.
def test_generer_nombre():
    nombre = generer_nombre()
    assert nombre >= 0 and nombre <= 100
