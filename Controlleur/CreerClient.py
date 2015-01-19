__author__ = 'alexis'


from Vue.Widget import Widget
from Vue.creerClient import Ui_Creer_Client
from Modele.Client import Client

class CreerClient:

    def __init__(self, main):
        self.__main = main
        #self._main.activity("Debut Creation Parking", self._main.lvl.INFO)

        self.__widget = Widget(self.__main)
        self.__ui = Ui_Creer_Client()
        self.__ui.setupUi(self.__widget)

        # connect
        self.__ui.pushButton_creer_client.clicked.connect(self.creer_client)

        self.showWindow()


    def creer_client(self):
        nom = self.__ui.lineEdit_nom.text()
        adresse = self.__ui.lineEdit_adresse.text()

        imma = self.__ui.lineEdit_immatriculation.text()
        long = self.__ui.spinBox_longueur.value()
        haut = self.__ui.spinBox_hauteur.value()

        c = Client(nom, adresse)
        c.nouvelle_voiture(imma,haut,long)


    def showWindow(self):
        """
        Gestion affichage vue Creation de Parking
        :return:
        """
        self.__widget.show()
        self.__child = None  # supprime l'eventuel widget enfant
        self.__widget.focusWidget()  # reprend le focus sur la fenetre
