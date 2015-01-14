from Modele import Client

__author__ = 'alexis'

import unittest


class ClientTest(unittest.TestCase):
    def test_get_nom(self):
        client_test = Client.Client('nom', 'adresse', False, False)
        self.assertIsInstance(client_test.nom, str)


if __name__ == '__main__':
    unittest.main()
