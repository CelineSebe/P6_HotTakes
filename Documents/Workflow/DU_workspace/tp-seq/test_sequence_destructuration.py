def test_trous_sequence_destructuration():
    # Remplacer les ... par une seule instruction
    # sans écrire de constantes littérales (1, 2...)

    s = [1, 2, 3, 4]

    ...

    assert a0 == 3 and b0 == 2 and c0 == 1 and d0 == 4

    ...

    assert a1 == 1 and b1 == [2, 3, 4]

    ...

    assert a2 == 4 and b2 == 1 and c2 == [2, 3]

    ...

    assert a3 == 4 and b3 == [1, 2] and c3 == 3

    print('ok')
