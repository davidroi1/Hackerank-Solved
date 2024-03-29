# Ce programme retourne la puissance 2 de tous les nombre compris entre 0 et inferieur a un nombre n donnee en imput

def loopfunction(nbloop: int):
    # Cette fonction affiche la puissance 2 de tous les nombre compris entre 0 infereurs nbloop
    # la fonction range(nblooop): creer une sequence ou liste de nombre allant de 0 a nbloop exclut

    for i in range(nbloop):
        print(i ** 2)


# recuperation des donnee de l'utilisateur en input
nb = int(input("Enter a number: "))

# appelle de la fonction loopfunction() et passage de nb en paramettre
loopfunction(nb)