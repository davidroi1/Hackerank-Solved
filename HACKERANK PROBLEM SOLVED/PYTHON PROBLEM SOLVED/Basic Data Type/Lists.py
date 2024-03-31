"""
Ce programme effectue des operation sur une liste de donne en fonction des instruction donnee par l'utilisateur
"""


def matching(instruc: str, val: list):
    """
    - La fonction modifie une liste en fonction des instructions de l'utilisateur
    - Elle modifie automatiquement une liste du programme principal
    """

    match instruc:
        case "insert": empty_list.insert(val[0], val[1])

        case "remove": empty_list.remove(val[0])

        case "append": empty_list.append(val[0])

        case "sort": empty_list.sort()

        case "pop": empty_list.pop()

        case "reverse": empty_list.reverse()

        case "print": print(empty_list)


# condition permettant a ce bout de code d'etre executer entend qu'instruction principale
if __name__ == "__main__":

    empty_list = []

    # recuperation des instruction de l'utilisateur
    # appelle de la fonction avec les parametres: instruction, new_value
    for parcour in range(int(input())):
        instruction, *value = input().split()
        new_value = list(map(int, value))

        matching(instruction, new_value)
