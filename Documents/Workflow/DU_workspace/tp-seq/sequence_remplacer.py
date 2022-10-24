def remplacer(sequence, element, nouveau):
    '''
    Remplacer dans la séquence toutes les occurrences de element par nouveau.
    '''

    for indice, x in enumerate(sequence):
        if x == element:
            sequence[indice] = nouveau
    '''
    for i in range(len(sequence)):
        if element == sequence[i]
            sequence[indice] = nouveau
    '''

# MAIN START DELETE


def main():
    # Définir une liste
    ma_liste = [1, 0, 10, 0, 10, 3, 10]
    print("La liste est :", ma_liste)

    # Demander l'élément à remplacer
    ancien = int(input("Élément à remplacer : "))

    # Demander l'élément qui le remplace
    remplacant = int(input("Remplaçant : "))

    # Déterminer la fréquence de l'élément dans la liste
    remplacer(ma_liste, ancien, remplacant)

    # Afficher le liste
    print("La liste est :", ma_liste)


if __name__ == '__main__':
    main()
# MAIN STOP DELETE
