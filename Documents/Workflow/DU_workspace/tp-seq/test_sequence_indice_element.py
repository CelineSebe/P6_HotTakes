from sequence_indice_element import *


def test_present_une_fois():
    assert indice_element([1, 3, 5, 3], 1) == 0     # au début
    assert indice_element([1, 3, 5, 3], 5) == 2     # au milieu
    assert indice_element([1, 3, 5, 0], 0) == 3     # à la fin


def test_present_pusieurs_fois():
    assert indice_element([1, 3, 5, 3], 3) == 1         # milieu + fin
    assert indice_element([1, 9, 3, 3, 5], 3) == 2      # milieu
    assert indice_element([5, 5, 5], 5) == 0            # debut fin
    assert indice_element([1, 3, 5, 1, 3, 1], 1) == 0   # partout
    assert indice_element('dernier', 'e') == 1           # milieu


def test_absent():
    assert indice_element([1, 3, 5, 3], 7) == None  # absent
    assert indice_element([3, 2, 5, 5, -5], 0) == None  # absent
    assert indice_element([1, 3, 5, 3, 7], 6) == None   # absent
    assert indice_element('dernier', 'x') == None    # absent
