def somme_cubes(nombres):
    '''
    retourner la somme des cubes des éléments de nombres.
    '''

    somme = 0
    for x in nombres:
        cube = x ** 3
        somme += cube

    return somme


def main():
    # Définir une liste
    ma_liste = [1, 0, 10, 3]
    print("La liste est :", ma_liste)

    # Calculer la somme des cubes des éléments de la liste
    somme = somme_cubes(ma_liste)

    # Afficher la somme des cubes
    print("Somme des cubes des éléments de cette liste :", somme)


if __name__ == '__main__':
    main()
# MAIN STOP DELETE
