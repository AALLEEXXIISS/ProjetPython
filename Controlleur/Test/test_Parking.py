from Modele.Parking import Parking
from Modele.Voiture import Voiture
from Modele.Place import Place
__author__ = 'alexis'

import unittest


class ParkingTest(unittest.TestCase):

    def test_instanciation(self):
        p = Parking(10,10,150,2,4,2,3)
        self.assertEqual(100,p.nb_place_libres)

    def test_rechercher_place(self):
        v = Voiture(456789, 3, 2)
        p = Parking(10,10,150,1,3,1,2)
        print(p.nb_place_libres)
        test = p.rechercher_place(v)
        print(test)
        self.assertIsInstance(test,Place)


if __name__ == '__main__':
    unittest.main()
-