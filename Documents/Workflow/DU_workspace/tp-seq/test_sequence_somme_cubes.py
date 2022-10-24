from sequence_somme_cubes import somme_cubes

def test1_classique():
    assert somme_cubes([ 4, -2, 0]) == 56

def test2_vide():
    assert somme_cubes([]) == 0

def test3_tuple():
    assert somme_cubes((1, 2, 3, 4)) == 100

def test4_reel():
    assert somme_cubes([2.0]) == 8.0

def test5_reel_arrondi():
    assert round(somme_cubes([0.2]), 6) == 0.008

