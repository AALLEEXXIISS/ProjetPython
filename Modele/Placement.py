__author__ = 'alexis'
class Placement:
    def __init__(self, date_debut, voiture, place):
        self.__date_debut = date_debut
        self.__date_fin = None
        self.__voiture = voiture
        self.__place = place

    def partir_place(self):
        pass


    @property
    def place(self):
        return self.__place
    @property
    def voiture(self):
        return  self.__voiture