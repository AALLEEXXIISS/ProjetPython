from Modele.Place import Place

__author__ = 'alexis'
import random


class Parking:

    def __init__(self,nb_places_niveau,nb_niveaux,prix,long_min,long_max,haut_min,haut_max):

        self.__nb_places_niveau = nb_places_niveau
        self.__nb_niveaux = nb_niveaux
        self.__prix = prix
        self.__nb_places_libres = self.__nb_niveaux * self.__nb_places_niveau
        self.__places = {}

        for niv in range(0, nb_niveaux,1):
            list_places = []
            for num in range(0, nb_places_niveau,1):
                long = random.randint(long_min,long_max)
                haut = random.randint(haut_min,haut_max)
                list_places.append(Place(num,niv,long,haut, True))
            self.__places[niv] = list_places



    def __str__(self):
        result = "Parking : "
        for n in range(0,self.__nb_niveaux,1):
            result += "niveau : "+ str(n)+" / "
            for p in range(0, self.__nb_places_niveau):
                liste_place = self.__places[n]
                num = liste_place[p].numero
                result += "Place num : " + str(num) + ", " + str(liste_place[p].longueur)+ ", "+ str(liste_place[p].hauteur) + " / "
            result += "/n"

        return result

    @property
    def nb_place_libres(self):
        result = 0
        for niv in range(0, self.__nb_niveaux, 1):
            for num in range(0, self.__nb_places_niveau,1):
                if self.__places[niv][num].est_libre == True :
                    result += 1

        return result

    def rechercher_place(self,voiture):
        for niv in range(0, self.__nb_niveaux, 1):
            for num in range(0, self.__nb_places_niveau,1):
                if voiture.hauteur <= self.__places[niv][num].hauteur and voiture.longueur <= self.__places[niv][num].longueur and self.__places[niv][num].est_libre == True :

                    return self.__places[niv][num]
        return -1


    def nb_places_libres_niveau(self,niveau):
        pass

    def add_abonnement(self, abonnement):
        pass