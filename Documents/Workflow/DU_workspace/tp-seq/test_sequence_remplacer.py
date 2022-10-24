from sequence_remplacer import remplacer

def test_vide():
    l = []
    remplacer(l, 3, 0)
    assert l == []

def test_absent():
    l = [5, 3, 8, 2, 3, 1]
    remplacer(l, 0, 7)
    assert l == [5, 3, 8, 2, 3, 1]

def test_milieu():
    l = [5, 3, 8, 2, 3, 1]
    remplacer(l, 3, 0)
    assert l == [5, 0, 8, 2, 0, 1]

def test_debut():
    l = [5, 3, 8, 2, 3, 1]
    remplacer(l, 5, 4)
    assert l == [4, 3, 8, 2, 3, 1]

def test_fin():
    l = [5, 3, 8, 2, 3, 1]
    remplacer(l, 1, -9)
    assert l == [5, 3, 8, 2, 3, -9]

def test_tous():
    l = [7, 7, 7, 7]
    remplacer(l, 7, -1)
    assert l == [-1, -1, -1, -1]

def test_un_element():
    l = [5]
    remplacer(l, 5, 4)
    assert l == [4]

    l = [5]
    remplacer(l, 1, 6)
    assert l == [5]

