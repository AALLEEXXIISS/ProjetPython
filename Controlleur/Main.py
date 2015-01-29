__author__ = 'alexis'

import sys
from PyQt4 import QtGui, QtCore
from Modele.Parking import Parking
from Controlleur.Acces import Acces
from Modele.Client import Client
from Modele.Voiture import Voiture
from Vue.main import Ui_MainWindow
from Vue.MainWindow import MainWindow
from Controlleur.CreerParking import CreerParking
from Controlleur.CreerClient import CreerClient




class Main():
    def __init__(self):

        #TODO Récupérer parking base de données
        self.__parking = Parking(10,10,100,1,3,1,3)

        app = QtGui.QApplication(sys.argv)
        self.__view = MainWindow()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self.__view)

        #connect
        self.__ui.pB_creer_parking.clicked.connect(self.afficher_garer_reprendre)
        self.__ui.pB_creer_client.clicked.connect(self.ouvrir_bornes)
        #self.__ui.actionOuvrir_Bornes.clicked.connect(self.afficher_garer_reprendre)




        self.afficher()
        sys.exit(app.exec_())
    def afficher_garer_reprendre(self):
        self.__view.hide()
        self.__widgetCourant = Acces(self, self.__parking)


    def creer_parking(self):
        self.__view.hide()
        self.__widgetCourant = CreerParking(self)

    def ouvrir_bornes(self):
        self.__view.hide()
        self.__acces = Acces(self, self.__parking)
        self.__widgetCourant = self.__acces
        self.__acces.lancer_procedure_entree()

    def afficher(self):
        self.__view.show()
        self.__widgetCourant = None  # supprime eventuel widget
        self.__view.focusWidget()  # reprend le focus sur la fenetre principal


if __name__ == '__main__':
    main = Main()