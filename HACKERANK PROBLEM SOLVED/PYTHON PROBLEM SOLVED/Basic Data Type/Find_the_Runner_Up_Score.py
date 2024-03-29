# ce programme recherche dans liste de donne et afficher le seconde moximum

def runner_up_score(number: list) -> int:
    """
    La fonction retourne le second maximum d'une liste de nombre desordonnee
    La fonction ordonne la liste du plus grand a plus petit (invers) avec la fonctin sort(reverse=True)
    """

    number.sort(reverse=True)
    max_number = max(number)
    second_max_number = 0

    for element in number:
        if element < max_number:
            second_max_number = element
            break

    return second_max_number


# recuperation des donnees de l'utilisateur entree en input
userNumber = list(map(int, input().strip().split()))

# appelle de la fonction runner_up_score(), passage en parametre des donnee recupere en input
# affichage automatique des information retournee
print(runner_up_score(userNumber))