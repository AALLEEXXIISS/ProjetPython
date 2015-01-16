__author__ = 'alexis'
from Modele.Place import Place
from Modele.Placement import Placement
from datetime import datetime

class Teleporteur:
    def __int__(self):
        pass
    def teleporter_voiture(self,voiture,place):
        placement = Placement(datetime.now(),voiture, place)
        place.add_placement()
        return placement
    def teleporter_voiture_super_abonne(self,voiture):
        pass
