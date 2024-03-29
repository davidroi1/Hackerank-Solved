# Ce programme permet d'afficher des expression,  en fonction des condition specifiées

def string_expression(n: int):
    """
        fonction prenant en paramenttre un nombre entier: n
        la fonction retourne une chaine de caractere: Weird, Not Weird
    """

    if (n % 2 != 0) or ((n % 2 == 0) and (n in range(6, 21))):
        print("Weird")

    else:
        print("Not Weird")


# recuperation de donnee de l'utilisateur du programme
number = int(input("Enter a number: "))

# appelle de la fonction et passage de number en parametre n
string_expression(number)