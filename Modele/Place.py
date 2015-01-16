__author__ = 'alexis'

class Place:
    def __init__(self, numero, niveau, long, haut, est_libre):
        self.__numero = numero
        self.__niveau = niveau
        self.__longueur = long
        self.__hauteur = haut
        self.__est_libre = est_libre


    def add_placement(self):
        self.__est_libre = False

    @property
    def numero(self):
        return self.__numero

    @property
    def niveau(self):
        return self.__niveau

    @property
    def longueur(self):
        return self.__longueur

    @property
    def hauteur(self):
        return self.__hauteur
    @property
    def est_libre(self):
        return self.__est_libre
    @property
    def id(self):
        return str(self.__niveau) + "/" + str(self.__numero)


    def __str__(self):
        return "Place : " + self.id