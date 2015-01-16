__author__ = 'alexis'
from PyQt4 import QtGui



class Widget(QtGui.QWidget):
    def __init__(self, main):
        super(Widget, self).__init__()
        self.__main = main

    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirmer Fermeture...",
                                            "Etes vous sur de vouloir abandonner ?\n"
                                            "(Toute modification non enregistrée seras perdu)",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            event.accept()
            self.__main.showWindow()