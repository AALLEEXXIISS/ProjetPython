__author__ = 'alexis'

from Vue.Widget import Widget
from Vue.creerParking import Ui_CreerParking
from Modele.Parking import Parking

class CreerParking:

    """ creer un Parking"""

    def __init__(self, main):
        self.__main = main
        #self._main.activity("Debut Creation Parking", self._main.lvl.INFO)

        self.__widget = Widget(self.__main)
        self.__ui = Ui_CreerParking()
        self.__ui.setupUi(self.__widget)

        # connect
        self.__ui.pB_creer_parking.clicked.connect(self.creer_parking)

        self.showWindow()


    def creer_parking(self):
        nb_places_niveaux = self.__ui.spinBox_nb_places_niveaux.value()
        nb_niveaux = self.__ui.spinBox_nbniveaux.value()
        prix = self.__ui.spinBox_prix.value()
        long_min = self.__ui.spinBox_long_min.value()
        long_max = self.__ui.spinBox_long_max.value()
        haut_min = self.__ui.spinBox_haut_min.value()
        haut_max = self.__ui.spinBox_haut_max.value()

        p = Parking(nb_places_niveaux, nb_niveaux, prix, long_min, long_max, haut_min, haut_max)

        self.__widget.hide()
        print(p)

    def showWindow(self):
        """
        Gestion affichage vue Creation de Parking
        :return:
        """
        self.__widget.show()
        self.__child = None  # supprime l'eventuel widget enfant
        self.__widget.focusWidget()  # reprend le focus sur la fenetre