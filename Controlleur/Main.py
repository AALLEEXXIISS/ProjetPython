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

        app = QtGui.QApplication(sys.argv)
        self.__view = MainWindow()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self.__view)

        #connect
        self.__ui.pB_creer_parking.clicked.connect(self.creer_parking)
        self.__ui.pB_creer_client.clicked.connect(self.creer_client)


        self.afficher()
        sys.exit(app.exec_())

    def creer_parking(self):
        self.__view.hide()
        self.__widgetCourant = CreerParking(self)

    def creer_client(self):
        self.__view.hide()
        self.__widgetCourant = CreerClient(self)

    def afficher(self):
        self.__view.show()
        self.__widgetCourant = None  # supprime eventuel widget
        self.__view.focusWidget()  # reprend le focus sur la fenetre principal


if __name__ == '__main__':
    main = Main()