"""
Ce programme recherche dans une liste de nom et de note de peronne et afficher la liste de toute les personne
ayant la plus faible note ordonner en fonction des caractere alphabetique
"""


def sort_dictionnary():
    """
    -La fonction recupere une liste de donnee clé, valeur et creer un dictionnaire pour stocker les information
    -appelle la fonction search_dictionnary avec le dictionnary creer en parametre de la fonciton
    """
    dictionnary = {}

    for _ in range(int(input())):
        name = input()
        score = float(input())
        dictionnary[name] = score

    search_dictionnary(dictionnary)


def search_dictionnary(dictionnarys: dict):
    """
    La fonction recupere un dicitonnaire de sort_dictionnary et recherche dans cette liste les plus faible note
    La fonction stock les nom ayant ces note faible et appelle la fonction search_list_name() avec la liste
    """

    new_dictionnary_sorted = dict(sorted(dictionnarys.items(), key=lambda a: a[1]))
    second_max_value = None
    list_second_max_value = []
    
    # recuperation de la seconde valeur la plus petit
    for value in new_dictionnary_sorted.values():
        if value > min(dictionnarys.values()):
            second_max_value = value
            break
            
    # recuperation des clé ayant la meme valeur que le nombre recuperer
    list_second_max_value = [key for key, value in new_dictionnary_sorted.items() if value == second_max_value]
    
    # appelle de la fonction sort_list_name() et passage de lis_second_max_value en parametre pour affichage du resultat
    sort_list_name(list_second_max_value)


def sort_list_name(list_name: list):
    """
    La fonction recupere une liste de la fonction search_dictionnary et range la les nom en fonction des caratere
    alphabetique et afficher le resultat
    """

    for element in sorted(list_name):
        print(element)


# appelle de la fonction sort_dictionnary() pour debuter le programme
sort_dictionnary()
