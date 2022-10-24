def test_exemple_cours():
    # Remplacer les ... par UNE expression ou instruction pour qu'il
    # n'y ait pas d'erreurs à l'exécution signalées par les assert

    s = [10, 3, 4, 7, 3, 5]

    taille = ...        # la taille de s

    assert taille == 6

    premier = ...      # le premier élément de s
    dernier = ...      # le dernier élément de s

    assert premier == 10
    assert dernier == 5

    indice7 = ...      # entier qui correspond à l'indice de 7 dans s

    assert s[indice7] == 7

    ...               # remplacer 4 par 421 dans s

    assert s == [10, 3, 421, 7, 3, 5]

    ...               # supprimer 421 de s

    assert s == [10, 3, 7, 3, 5]

    ...             # ajouter 0 à la fin de s

    assert s == [10, 3, 7, 3, 5, 0]
    print('ok')
