class Voiture:

    def __init__(self, immatriculation, longueur, hauteur):
        self.__immatriculation = immatriculation
        self.__longeur = longueur
        self.__hauteur = hauteur
        self.__est_dans_parking = False


    def add_placement(self):
        pass


    @property
    def hauteur(self):
        return self.__hauteur
    @property
    def longueur(self):
        return self.__longeur
    @property
    def immatriculation(self):
        return self.__immatriculation
    @property
    def est_dans_parking(self):
        return self.__est_dans_parking == True