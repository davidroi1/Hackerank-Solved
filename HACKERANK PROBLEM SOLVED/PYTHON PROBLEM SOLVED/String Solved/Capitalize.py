"""
Ce programme permet de rendre une chaine de carctere en capitalise losqu'elle est lower
"""


def solve(s):
    """
    - La fonction modifie la chaine de caractere, de miniscule en majuscule
    - elle retourne la chaine modife
    """

    list_string = []

    for letter in s.split(" "):
        list_string.append(letter.capitalize())

    return " ".join(list_string)


# recuperation de la chaine de l'utilisateur a modifier
user_string = input()

# recuperation et affichage de la chaine modifie
print(solve(user_string))