class Ohce:
    def bien_dit(self):
        return "Bien dit"

    def bonjour(self, ):
        return "Bonjour"

    def au_revoir(self):
        return "Au revoir"

    def miroir(self, chaine):
        return chaine[::-1]

    def palindrome(self, palindrome):
        miroir = self.miroir(palindrome)
        return self.bonjour() + miroir + (self.bien_dit() if miroir == palindrome else "") + self.au_revoir()