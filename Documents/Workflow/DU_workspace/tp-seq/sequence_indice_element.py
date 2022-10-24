def indice_element(sequence, element):
    '''
    Retourner l'indice de la première occurrence de element dans sequence.
    '''
    for i, x in enumerate(sequence):
        if element == x:
            return i

# MAIN START DELETE


def main():
    # Définir une liste
    ma_liste = [1, 0, 10, 0, 10, 3, 10, 15]
    print("La liste est :", ma_liste)

    # Demander l'élément
    element = int(input("Élément : "))

    # Déterminer l'indice de l'élément dans la liste
    indice = indice_element(ma_liste, element)

    print("Son indice :", indice)


if __name__ == '__main__':
    main()
# MAIN STOP DELETE
