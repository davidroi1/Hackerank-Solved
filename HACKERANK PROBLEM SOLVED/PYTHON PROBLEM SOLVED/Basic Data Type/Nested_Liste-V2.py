"""
Ce programme recherche dans une liste les personnes ayant les seconde plus grande mauvaise note de la class
dans l'ordre de alphabetique
"""


def data_recup():
    """
    - La fonction recupere les donnee de l'utilisateur
    - creer une liste impriquer (2D) ayant les nom associé au note
    - appelle de la fonction data_searcher() pour la recherche des noms
    """

    liste = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        liste.append([name, score])

    data_searcher(liste)


def data_searcher(lister: list):
    """
    - La fonction recupere une liste de nom et de note en parametre
    - recherche les noms ayant  la seconde plus grande mauvaise note
    - creer une liste de nom
    - appelle de la fonction data_printer() pour l'affichage d'information
    """

    # initialisation des variable
    lister.sort(key=lambda x: x[1], reverse=False)
    min_score = min(lister, key=lambda x: x[1])
    liste_max = []
    second_max = None

    # recuperation de la seconde plus grande mauvaise note
    for i in range(0, len(lister)):
        if lister[i][1] > min_score[1]:
            second_max = lister[i][1]
            break
    # recuperation des nom ayant la seconde plus grande mauvaise note
    name_liste = [lister[i][0] for i in range(0, len(lister)) if lister[i][1] == second_max]

    data_printer(name_liste)


def data_printer(list_name: list):
    """
    - La fonction recupere une liste de nom en parametre
    - affiche les noms de la liste dans l'ordre alphabetique
    """

    [print(i) for i in sorted(list_name)]


data_recup()
