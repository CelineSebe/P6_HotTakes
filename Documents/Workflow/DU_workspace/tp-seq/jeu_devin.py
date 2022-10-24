from multiprocessing.resource_sharer import stop
import random


def selectionne_jeu():
    '''Faire choisir un jeu'''

    print("1- L'ordinateur choisit un nombre")
    print("2- Vous choisissez un nombre et l'ordinateur le devine")
    print("0- Quitter le programme")

    choice = int(input("Votre choix :"))

    if choice == 1:
        je_devine()
    elif choice == 2:
        machine_devine()
    elif choice == 0:
        stop()
    else:
        selectionne_jeu


def je_devine():
    '''Faire deviner le nombre choisi par la machine entre 0 et 1000'''

    # Faire choisir nombre à la machine
    nombre = random.randint(1, 999)

    # Choisir n
    print("J'ai choisi un nombre compris entre 1 et 1000.")

    # Comptabiliser le nombre d'essai
    n_essai = 1  # Initialiser la variable n_essai
    n = int(input(f"Proposition {n_essai} :"))

    # Déterminer où en est l'utilisateur tant que n est différent de nombre
    while n != nombre:
        # proposer des indices pour chaque essai
        if n > nombre:
            print("Trop grand")  # retourner indice pour aider l'utilisateur
            n_essai += 1  # incrémenter le n_essai à chaque n != nombre
            n = int(input(f"Proposition {n_essai} :"))
        else:
            print("Trop petit")
            n_essai += 1
            n = int(input(f"Proposition {n_essai} :"))

    print("Bravo ! Vous avez réussi après", n_essai, "essais")
    selectionne_jeu()


def machine_devine():
    ''' Faire deviner un nombre entre 0-1000 à la machine'''

    # Faire demander un nombre à la machine entre 0 et 1000
    a = 0
    b = 1000

    # Comptabiliser le nombre d'essai
    n_essai = 1  # Initialiser la variable n_essai
    response = "n"
    while response != "o":
        response = str(
            input("Avez-vous choisi un nombre compris entre 1 et 999 (o/n)?"))
        if response == "n":
            input("J'attends...")
        elif response == "o":  # Faire faire une recherche par dichotomie
            m = (a + b)/2
            print(f"Proposition {n_essai} :", int(m))
        else:
            response = str(
                input("Avez-vous choisi un nombre compris entre 1 et 999 (o/n)?"))

    for i in range(a, b):
       # Aider la machine à trouver m
       # Fournir des indices après chaque mauvaise réponse
        proposition = str(input("Trop (g)rand, trop (p)etit ou (t)rouvé"))
        if proposition == "g":
            b = m
            n_essai += 1
            m = (a + b)/2
            print(f"Proposition {n_essai} :", int(m))
        elif proposition == "p":
            a = m
            n_essai += 1
            m = (a + b)/2
            print(f"Proposition {n_essai} :", int(m))
        elif proposition == "t":
            # Machine a donné la bonne réponse
            print(f"J'ai trouvé en {n_essai} essais")
            selectionne_jeu()
        else:
            print("g si ma proposition est trop grande")
            print("p si ma proposition est trop petite")
            print("t si j'ai trouvé le nombre")


selectionne_jeu()

stop()
