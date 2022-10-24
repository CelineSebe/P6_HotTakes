def frequence(sequence, element):
    '''
    Retourner la fréquence (le nombre d'occurrences) de element dans sequence.
    '''
    nombre = 0
    for x in sequence:
        if x == element:
            nombre += 1
    return nombre

# MAIN START DELETE


def main():
    # Définir une liste
    ma_liste = [1, 0, 10, 0, 10, 3, 10]
    print("La liste est :", ma_liste)

    # Demander l'élément
    element = int(input("Élément : "))

    # Déterminer la fréquence de l'élément dans la liste
    frequence_element = frequence(ma_liste, element)

    print("Sa fréquence :", frequence_element)


if __name__ == '__main__':
    main()
# MAIN STOP DELETE
