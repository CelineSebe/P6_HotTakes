from sequence_est_present import est_present

def test_present():
    assert est_present([1, 3, 5, 0], 5)   # au milieu
    assert est_present([1, 3, 5, 0], 0)   # à la fin
    assert est_present([1, 3, 5, 0], 1)   # au début
    assert est_present([3, 1, 3, 5, 3, 0, 3], 3)  # plusieurs fois
    assert est_present('dernier', 'r')
    assert est_present((1, 2, 3, 4), 2)
    assert est_present(range(10), 9)

def test_absent():
    assert not est_present([1, 3, 5, 0], 4)
    assert not est_present('dernier', 'x')
    assert not est_present((1, 2, 3, 4), 5)
    assert not est_present(range(10), 10)
