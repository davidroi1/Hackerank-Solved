"""
Ce programme retourne tous les cordonner possibles d'un tableau a 3D x, y, z
afficher les coordonnee dont leur est differente de n etant un nombre saisir par l'utilisateur
"""


def table_coordinate(x, y, z, n):
    """
    La fonction creer les sequence de nombre des different parametre x, y et z
    elle utilisera trois boucle for et la fonction range() pour la reation des sequences individuelle de valeur
    """

    listsummer = [[k, j, i] for k in range(z + 1) for j in range(y + 1) for i in range(x + 1)]

    newlistsummer = [element for element in listsummer if sum(element) != n]

    return newlistsummer


# recuperation des donnee de l'utilisateur en input dont 4 valeur separer par des espaces
userListNumber = list(map(int, input().strip().split()))

# appelle de la fonction, passage de userListNumber pour les trois parametre en utilisant un scather *
# affichage automatique des resultats recuperers
print(table_coordinate(*userListNumber))