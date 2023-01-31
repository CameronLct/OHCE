class Ohce:
    def __init__(self, langue):
        self.langue = langue
    def bien_dit(self):
        return self.langue.bien_dit()

    def bonjour(self):
        return self.langue.bonjour()

    def au_revoir(self):
        return self.langue.au_revoir()

    def miroir(self, chaine):
        return chaine[::-1]

    def palindrome(self, palindrome):
        miroir = self.miroir(palindrome)
        return self.bonjour() + miroir + (self.bien_dit() if miroir == palindrome else "") + self.au_revoir()