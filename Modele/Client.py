__author__ = 'alexis'

from Modele.Voiture import Voiture


class Client:
    def __init__(self, nom, adresse, est_abonne = None, est_super_abonne = None):
        self.__nom = nom
        self.__adresse = adresse
        self.__est_abonne = est_abonne
        self.__est_super_abonne = est_super_abonne


    @property
    def nom(self): return self.__nom

    @property
    def adresse(self): return self.__adresse

    @property
    def est_abonne(self): return self.__estAbonne

    @property
    def est_super_abonne(self): return self.__estSuperAbonne

    @property
    def nb_frequentation(self): return self.__nbFrequentation

    @property
    def voiture(self): return self.__ma_voiture

    def s_abonner(self, Abonnement):
        pass

    def nouvelle_voiture(self,imma, haut, long):
        self.__ma_voiture = Voiture(imma, long, haut)

    def se_desabonner(self):
        pass

    def demander_maintenance(self):
        pass

    def demander_livraison(self, date, heure, adresse_livraison):
        pass

    def demander_entretient(self):
        pass

    def entrer_parking(self, acces):
        place = acces.lancer_procedure_entree(self)
        return place
