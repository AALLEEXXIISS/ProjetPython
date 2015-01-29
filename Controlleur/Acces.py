__author__ = 'alexis'

from Vue.choixClient import Ui_Dialog_choix_client
from Vue.borne import Ui_Borne
from Vue.Widget import Widget
from Controlleur.Camera import Camera
from Vue.PanneauAffichage import PanneauAffichage
from Vue.Borne import Borne
from Controlleur.Teleporteur import Teleporteur
from Modele.Voiture import Voiture
from Modele.Parking import Parking
import random

class Acces:
    def __init__(self, main, parking):
        self.__main = main
        self.__ma_camera = Camera()
        self.__mon_panneau = PanneauAffichage()
        self.__mon_teleporteur = Teleporteur()
        self.__mon_parking = parking

        self.__widget = Widget(self.__main)
        self.__ui = Ui_Dialog_choix_client()
        self.__ui.setupUi(self.__widget)
        self.__widget.show()

        #connect
        self.__ui.pushButton_garer.clicked.connect(self.lancer_procedure_entree)




    def actionner_camera(self):
        haut = random.randint(1,3)
        long = random.randint(1,3)
        imma = random.randint(1,9999999999)
        return Voiture(imma, long, haut)

    def actionner_panneau(self):
        pass

    def lancer_procedure_entree(self):
        #Todo refaire méthode actionner camera sans parametre client.
        #Action Borne, série de questions

        voiture = self.actionner_camera()
        place = self.__mon_parking.rechercher_place(voiture)

        #Affiche la borne
        self.afficherBornes()
        #délivraison ticket avec num place
        placement = self.__mon_teleporteur.teleporter_voiture(voiture, place)
        #Action vue Panneau d'affichage
        #return place
        pass
    def inserer_carte_abonnement(self):
        self.__borne1.plainTextEdit.setPlainText("Insérer votre carte d'abonner")
        self.__borne1.pushButton_inserer_CA.setEnabled(True)

        #connect
        self.__borne1.pushButton_inserer_CA.clicked.connect(self.choix_services)


    def choix_services(self):
        self.__borne1.pushButton_inserer_CA.setEnabled(False)
        self.__borne1.plainTextEdit.setPlainText("Choisissez les services souhaités.")
        self.__borne1.groupBox.setEnabled(True)

        #connect
        self.__borne1.pushButton_valider_services.clicked.connect(self.valider_service)

    def valider_service(self):
        if self.__borne1.checkBox_livraison.isChecked():
            self.__borne1.plainTextEdit.setPlainText("Veuillez saisir votre adresse de livraison.")

    def afficherBornes(self):


        self.__widget1 = Widget(self.__main)
        self.__borne1 = Ui_Borne()
        self.__borne1.setupUi(self.__widget1)
        self.__widget1.show()
        self.__child = None  # supprime l'eventuel widget enfant
        self.__widget1.focusWidget()  # reprend le focus sur la fenetre

        #connect

        #self.__borne1.pushButton_abonne_non.clicked.connect(self.)
        self.__borne1.pushButton_abonne_oui.clicked.connect(self.inserer_carte_abonnement)

        # self.__widget2 = Widget(self.__main)
        # self.__borne2 = Ui_Borne()
        # self.__borne2.setupUi(self.__widget2)
        # self.__widget2.show()
        # self.__child = None  # supprime l'eventuel widget enfant
        # self.__widget2.focusWidget()  # reprend le focus sur la fenetre