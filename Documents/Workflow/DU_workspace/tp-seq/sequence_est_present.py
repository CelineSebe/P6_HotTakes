
def est_present(sequence, element):
    '''
    Est-ce qu'un élément est présent dans une séquence ?
    '''

    i = 0
    while i < len(sequence) and sequence[i] != element:
        i += 1
    return i < len(sequence)


def main():
    # Définir une liste
    ma_liste = [1, 0, 10, 0, 10, 3, 10, 15]
    print("La liste est :", ma_liste)

    # Demander l'élément
    element = int(input("Élément : "))

    # Déterminer la présence de l'élément dans la liste
    presence = est_present(ma_liste, element)

    print("Est présent ?", "oui" if presence else "non")


if __name__ == '__main__':
    main()
