# Ce programme retourne une valeur booleen (False) / (True) pour verifié si une annee est elle Bixetille

def is_leap(year: int) -> bool:
    """
        Cette fonction verifie si le year est un Bixetille ou  pas
        retoune: True si, year est une annee Bixetille ou False sinon
    """
    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    
    return False


# recuperation de donnee de l'utilisateur donnee en input
years = int(input())

# appelle de la fonction is_leap(), passage de years en paramettre et affichage automatique de la valeur retournee
print(is_leap(years))