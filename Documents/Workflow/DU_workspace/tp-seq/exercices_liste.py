''' Exercices sur les listes. '''

'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

def milieu(liste: list) -> list:
    '''Retourner la liste sans le premier ni le dernier élément.'''
    pass


def test_milieu():
    assert [3, 4] == milieu([2, 3, 4, 5])
    assert list(range(1, 9)) == milieu(list(range(10)))


'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

def liste_indices_pairs(liste):
    '''Retourner la liste des éléments d'indices pairs de la liste.'''
    pass

def liste_indices_impairs(liste):
    '''Retourner la liste des éléments d'indices impairs de la liste.'''
    pass


def test_liste_indices_pairs():
    assert [-5, 1, 0] == liste_indices_pairs([-5, 2, 1, 18, 0])
    assert list(range(0, 10, 2)) == liste_indices_pairs(list(range(10)))

def test_liste_indices_impairs():
    assert [2, 18] == liste_indices_impairs([-5, 2, 1, 18, 0])
    assert list(range(1, 10, 2)) == liste_indices_impairs(list(range(10)))

