import os

# fonction de capitalisation des chaine de caractere.
def stringCapitalize(string):
    liste = []
    
    # boucle for pour separer les sequence en deux chaine distincte
    for i in list(string.split()):
        liste.append(i.capitalize())
        
    # fusionnement des chaine du tableau avec join()
    newString = " ".join(liste)
    
    # retour de la nouvelle chaine modifier
    return newString
    
    
# recuperation des donnee de l'utilisateur
userName = input("What is your name please? : ")

# appelle et recuperation des donner apres modification
newName = stringCapitalize(userName)
print(newName)
