# Importation / Ajout du module random
import random

"""
Le juste chiffre.
"""

# Nombre généré aléatoirement entre 0 et 100
nbaleatoire = random.randint(0, 100)

# Initialisation du nombre de coups
nbcoups = 0

""" 
Boucle tant que le joueur n'a pas trouvé le nombre
"""
while True:
  # Demande au joueur de deviner le nombre
  nbpropose = int(input("Proposez un nombre : "))

  # Nombre de coups utiliser par le joueur
  nbcoups += 1

  """
  Comparaison du nombre proposé et du nombre à deviner
  """
  if nbpropose == nbaleatoire:
    print("Bravo ! Vous avez trouvé le nombre en", nbcoups, "coups.")
    break
  elif nbpropose < nbaleatoire:
    print("C'est plus grand !")
  else:
    print("C'est plus petit !")
