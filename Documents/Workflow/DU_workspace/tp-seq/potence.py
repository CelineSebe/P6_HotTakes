'''Ce module fournit la fonction potence pour afficher un pendu.'''

NB_ETAPES = 11   # Nombre d'étapes pour construire la potence


# La dessin de la potence et du pendu (complet).
#
# Le "r" devant ''' indique que les caractères ne doivent pas être interprétés
# (r pour raw).  Ceci concerne le caractère '\' qui donne un sens au caractère
# suivant : \n retour à la ligne, \t tabulation, \\ anti-slash...
#
# Le nom en majuscules indique que cette variable ne devrait pas être changée.
# Le « _ » en début de nom indique que c'est une variable locale à ce fichier
# qui ne devrait pas être utilisée à l'extérieur.
_POTENCE = r'''
  _______________
    || //     |
    ||//      |
    ||/      / \
    ||       \_/
    ||      __|__
    ||        |
    ||        |
    ||       / \
    ||      /   \
   /||\
  //||\\
 // || \\
======================
'''

# Le masque marque par une lettre (A à Z) certaines parties de la potence.
# Chaque lettre correspond à une étape du tracé : 'A' pour la première, 'B'
# pour la deuxième, etc.
_MASQUE = r'''
  CCCCCCCCCCCCCCC
    BB DD     K
    BBDD      K
    BBD      J J
    BB       JJJ
    BB      HHEII
    BB        E
    BB        E
    BB       F G
    BB      F   G
   AAAA
  AAAAAA
 AA AA AA
AAAAAAAAAAAAAAAAAAAAAA
'''


assert len(_MASQUE) == len(_POTENCE), (len(_POTENCE), len(_MASQUE))
    # vérifier la cohérence à minima entre _POTENCE et _MASQUE

assert NB_ETAPES == len(set(c for c in _MASQUE if 'A' <= c <= 'Z'))
    # vérifier que la valeur de NB_ETAPES est correcte.
    # Remarque : on aurait pu utiliser l'expression de droite pour initialiser
    # NB_ETAPES


def potence(etape: int) -> str:
    '''Retourne la potence à une étape donnée de son tracé.

    :param etape: l'étape souhaitée du tracé de la potence
    :return: la potence à l'étape considérée
    :pre: 1 <= etape <= 11
    '''
    assert 1 <= etape <= 11

    # Déterminer la lettre qui correspond à l'étape (1 -> 'A', etc.)
    lettre: str = chr(ord('A') + etape - 1)  # lettre correspondant à l'étape

    # Construire la potence pour cette étape.
    #    Principe : on ne garde du _POTENCE que les caractères pour
    resultat = ''
    for indice, caractere in enumerate(_MASQUE):
        if 'A' <= caractere <= 'Z':     # un marqueur
            if caractere <= lettre:     #    à montrer
                resultat += _POTENCE[indice]
            else:                       #    à cacher
                resultat += ' '
        else:                           # un autre caractère
            resultat += caractere       #    à conserver
    return resultat


if __name__ == '__main__':
    # Afficher tous les tracés de la potence et du pendu
    for etape in range(1, NB_ETAPES + 1):
        print('\n' * 3)
        print(potence(etape))
        print('\n' * 3)
        input('Appuyer sur ENTRÉE...')
