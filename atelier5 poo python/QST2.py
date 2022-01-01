class Rectangle:
        def _init_(self, longueur=30, largeur=15):
                self.lon = longueur
                self.lar = largeur
                self.nom = "rectangle"

        def surface(self):
                return self.lon*self.lar

        def _str_(self):
                return ("\nLe {0} de côtes {1} et {2} a une surface de {3}"
                         .format(self.nom, self.lon, self.lar,self.surface()))

class Carre(Rectangle):
        def _init_(self, cote=10):
                Rectangle._init_(self, cote, cote)
                self.nom = "carre"

if _name_ == '_main_':
        r = Rectangle(12, 8)
        print(r)
        c = Carre()
        print(c)
