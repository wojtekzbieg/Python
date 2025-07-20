import unittest

from projekt123 import buduj_drzewo, przewiduj, to_terminal


class TestDrzewoDecyzyjne(unittest.TestCase):
    def setUp(self):
        self.dataset = [
            [200, 1, 14, 1, 0],
            [1500, 2, 19, 1, 1],
            [50, 1, 10, 1, 0],
            [10, 3, 3, 0, 0],
            [1400, 1, 23, 1, 0],
            [1000, 2, 20, 0, 1],
            [500, 1, 15, 1, 0],
            [2500, 3, 22, 1, 1]
        ]
        self.drzewo = buduj_drzewo(self.dataset, max_glebokosc=4, min_wielkosc=1)

    def test_autoryzowana_transakcja(self):
        wynik = przewiduj(self.drzewo, [500, 1, 15, 1])
        self.assertEqual(wynik, 0, "Transakcja autoryzowana została błędnie sklasyfikowana.")

    def test_podejrzana_transakcja(self):
        wynik = przewiduj(self.drzewo, [2000, 3, 21, 0])
        self.assertEqual(wynik, 1, "Transakcja podejrzana została błędnie sklasyfikowana.")

    def test_granica_podzialu(self):
        wynik = przewiduj(self.drzewo, [1500, 2, 19, 0])
        self.assertEqual(wynik, 1, "Transakcja na granicy podziału została błędnie sklasyfikowana.")

    def test_puste_dane(self):
        drzewo = buduj_drzewo([], max_glebokosc=4, min_wielkosc=1)
        self.assertIsNone(drzewo, "Funkcja buduj_drzewo powinna zwrócić None dla pustych danych.")


if __name__ == '__main__':
    unittest.main()
