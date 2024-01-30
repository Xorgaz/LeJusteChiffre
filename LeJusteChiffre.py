# Le Juste Chiffre
# Le but du jeu est de trouver le chiffre généré aléatoirement.

import re

def translate(text):
    """Translate the given text to Parseltongue.

    :param str text: The text to translate.

    :returns: the translated text.
    :rtype: str
    """
    return re.sub(r"[\w\d]", "s", text)