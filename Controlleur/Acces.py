__author__ = 'alexis'

from Controlleur.Camera import Camera
from Vue.PanneauAffichage import PanneauAffichage
from Vue.Borne import Borne
from Controlleur.Teleporteur import Teleporteur
from Modele.Voiture import Voiture
from Modele.Parking import Parking

class Acces:
    def __init__(self,parking):
        self.__ma_camera = Camera()
        self.__mon_panneau = PanneauAffichage()
        self.__borne = Borne()
        self.__mon_teleporteur = Teleporteur()
        self.__mon_parking = parking

    def actionner_camera(self, client):
        haut = self.__ma_camera.capturer_hauteur(client.voiture)
        long = self.__ma_camera.capturer_longueur(client.voiture)
        imma = self.__ma_camera.capturer_immatriculation(client.voiture)
        return Voiture(imma, long, haut)

    def actionner_panneau(self):


    def lancer_procedure_entree(self,client):
        #Action Borne, série de questions
        #
        voiture = self.actionner_camera(client)
        place = self.__mon_parking.rechercher_place(voiture)
        #délivraison ticket avec num place
        placement = self.__mon_teleporteur.teleporter_voiture(voiture, place)
        #Action vue Panneau d'affichage
        return place