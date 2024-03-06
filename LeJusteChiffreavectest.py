import pytest
from random import randint

def testunitaire_LeJusteChiffre():
  """
  Teste le programme "Le juste chiffre".
  """
  # Nombre aléatoire entre 0 et 100
  nbaleatoire = randint(0, 100)
  nbcoups = 0
  print("le nombre alea est ", nbaleatoire)
  # Boucle tant que le joueur n'a pas trouve le nombre
  while True:
    # Saisie du nombre proposé par le joueur
    try:
      nbpropose = int(input("Proposez un nombre : "))
      # si ce n'est pas un nombre alors message d'erreur et proposition de proposer un nouveau nombre
    except ValueError:
      print("La saisie doit être un nombre.")
      continue

    # Calcul du nombre de coups fait par l'utilisateur
    nbcoups += 1

    # Comparaison du nombre proposé et du nombre à deviner
    if nbpropose == nbaleatoire:
      assert nbcoups <= 10, f"Le nombre de coups est de {nbcoups}, il devrait être inférieur ou égal à 10."
      print("Bravo vous gagné !")
      break
    elif nbpropose < nbaleatoire:
      print("C'est plus grand !")
    else:
      print("C'est plus petit !")

# Lancement du test
testunitaire_LeJusteChiffre()
