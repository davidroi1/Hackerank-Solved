# Ce programme retourne une liste de nombre allant de 1 a n inclut saisir par l'utilisateur

def printnumber(number: int):
    # Cette fonction affiche les nombre allant de 1 a number consecultif

    for num in range(1, number + 1):
        print(num, end='')


# recuperation des donnee de l'utilisateur
userNumber = int(input("Enter a number: "))

# appelle de la fonction et passage de userNumber en parametre
printnumber(userNumber)