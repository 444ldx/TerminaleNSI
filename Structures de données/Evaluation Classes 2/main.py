import unittest

# Exercice 1

class Date():
    """Représentation d'une Date"""
    
    MOIS = ['janvier',
            'février',
            'mars',
            'avril',
            'mais',
            'juin',
            'juillet',
            'aout',
            'septembre',
            'octobre',
            'novembre',
            'décembre']
    
    def __init__(self, jour:int, mois:int, annee:int):
        if jour >= 0 and jour <= 31 and mois >= 1 and mois <= 12:
            self.jour = jour
            self.mois = mois
            self.annee = annee
        else:
            raise ValueError("Le format de la date rentrée n'est pas correct.")
        
    def __str__(self):
        return f"{self.jour} {self.MOIS[self.mois-1]} {self.annee}"
    
    def __lt__(self, other):
        if self.annee < other.annee:
            return True
        elif self.mois < other.mois:
            return True
        elif self.jour < other.jour:
            return True
        else: 
            return False
        

# Exercice 2

class Fraction():
    """Représentation d'une Fraction"""
    
    def __init__(self, num:int, denom:int):
        if num > 0 and denom > 0:
            self.num = num
            self.denom = denom
            self.__simplifier()
        else:
            raise ValueError("Les arguments doivent être des entiers naturels.")
        
    def __str__(self):
        return f"{self.num}/{self.denom}" if self.denom != 1 else f"{self.num}"
    
    def __eq__(self, other):
        if self.num == other.num and self.denom == other.denom:
            return True
        return False
    
    def __lt__(self, other):
        return True if self.num/self.denom < other.num/other.denom else False
    
    def __add__(self, other):
        return Fraction(self.num + other.num, self.denom + other.denom)
    
    def __mul__(self, other):
        return Fraction(self.num * other.num, self.denom * other.denom)
    
    def __pgcd(self, a:int, b:int):
        """Plus grand diviseur commun

        Args:
            a (int): Numérateur
            b (int): Dénominateur

        Returns:
            (int): Plus grand diviseur commun
        """
        while b:
            a, b = b, a%b
        return a
    
    def __simplifier(self):
        """Simplifier la fraction"""
        facteur_commun = self.__pgcd(self.num, self.denom)
        self.num /= facteur_commun
        self.denom /= facteur_commun
        self.num, self.denom = int(self.num), int(self.denom)

# Tests

class Tests(unittest.TestCase):
    def test_exo1(self):
        self.assertEqual(Date(3, 6, 1876).__str__(), "3 juin 1876")
        self.assertEqual(Date(7, 12, 1853).__str__(), "7 décembre 1853")
        self.assertTrue(Date(3, 6, 1876) < Date(4, 6, 1876))
        self.assertFalse(Date(9, 12, 1963) < Date(7, 12, 1853))
        
    def test_exo2(self):
        self.assertEqual(Fraction(1, 10).__str__(), "1/10")
        self.assertEqual(Fraction(2, 4).__str__(), "1/2")
        self.assertEqual(Date(7, 12, 1853).__str__(), "7 décembre 1853")
        self.assertTrue(Fraction(4, 8) == Fraction(4, 8))
        self.assertTrue(Fraction(1, 10) < Fraction(2, 4))
        self.assertEqual(Fraction(1, 10) + Fraction(2, 4), Fraction(1, 6))
        self.assertEqual(Fraction(1, 10) * Fraction(2, 4), Fraction(1, 20))

if __name__ == "__main__":
    unittest.main()
