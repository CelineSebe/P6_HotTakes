from sequence_frequence import frequence

def test_present_une_fois():
    assert frequence([1, 3, 5, 3], 5) == 1   # au milieu
    assert frequence([1, 3, 5, 3], 1) == 1   # au début
    assert frequence([1, 3, 5, 7], 7) == 1   # à la fin

def test_present_plusieurs_fois():
    assert frequence([1, 3, 5, 3], 3) == 2
    assert frequence([4, 4, 4], 4) == 3
    assert frequence('dernier', 'e') == 2

def test_absent():
    assert frequence([1, 3, 5, 3], 7) == 0
    assert frequence('dernier', 'x') == 0
    assert frequence((3, 2, 5, 5, -5), 0) == 0

