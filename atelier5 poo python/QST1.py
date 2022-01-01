class Vecteur2D():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def printVector(self):
        print('Les coordonnées de ce vecteur est: ({0},{1})'.format(self.x,self.y))

    def __add__(self,other):
        resultat = Vecteur2D(self.x+other.x,self.y+other.y)
        return resultat


v1 = Vecteur2D(12,34)
v2 = Vecteur2D(23,-6)

v1.printVector()
v2.printVector()

somme = v1 + v2
print('the sum of v1 and v2 is:')
somme.printVector()