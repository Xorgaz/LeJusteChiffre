import test
from test import generer_nombre, verifier_saisie_utilisateur
# Test unitaire 1
def test_saisie_utilisateur_nombre():
    assert verifier_saisie_utilisateur("123") == True

def test_saisie_utilisateur_lettre():
    assert verifier_saisie_utilisateur("abc") == False

# Test unitaire 2
def test_generer_nombre():
    nombre = generer_nombre()
    assert nombre >= 0 and nombre <= 100

test_saisie_utilisateur_nombre
test_saisie_utilisateur_lettre
test_generer_nombre
