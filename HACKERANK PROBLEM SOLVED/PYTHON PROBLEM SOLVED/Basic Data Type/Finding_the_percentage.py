"""
Ce programme calcule la moyenne chaque eleve et la fiche sous forme de decimal ayant deux chiffre apres la virgule
"""


def arivage_recup():
    """
    - La fonction recupere les nom et les note des personne
    - creer un dictionnaire ayant pour clé: nom et la valeur: note
    - appelle la fonction arivage_operateur() et passe le dictionnaire en parametre
    """

    dictionnary = {}

    for i in range(int(input())):
        key, *value = input().strip().split()
        dictionnary[key] = list(map(float, value))

    return dictionnary


def arivage_operator(arivage_dic: dict):
    """
    - La fonction recupere un dictionnaire en parametre
    - calcule la moyenne de chaque clé valeur: sum / len()
    - appelle la fonction arivage_printer() pour afficher les donnee
    """

    arivage_new_dic = {}

    for key, value in arivage_dic.items():
        arivage_new_dic[key] = f"{sum(value) / len(value):.2f}"

    return arivage_new_dic


def arivage_printer(arivage_print: dict, query_: str):
    """
    - La fonction recupere une valeur entier en parametre
    - afficher en sortit les donnees recus
    """

    print(arivage_print[query_])


if __name__ == "__main__":

    dictionnay_score = arivage_recup()
    dictionnary_arivage_score = arivage_operator(dictionnay_score)

    # recuperation de la requette de l'utilisateur
    query_arivage = input()

    # appelle de la fontion arivage_printer() avec les paramettre pour recherche le nom et afficher la moyenne demander
    arivage_printer(dictionnary_arivage_score, query_arivage)

