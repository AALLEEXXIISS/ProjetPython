__author__ = 'alexis'

from Modele.Parking import Parking
from Controlleur.Acces import Acces
from Modele.Client import Client
from Modele.Voiture import Voiture

class Main:

    parking = Parking(10, 10, 100, 1, 4, 1, 3)
    acces = Acces(parking)
    client1 = Client("Perec","rue du port", False, False)
    client1.nouvelle_voiture(456789, 3, 2)
    place = client1.entrer_parking(acces)
    print(place)



