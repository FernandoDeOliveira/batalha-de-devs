from unittest import TestCase

from code_war.grid_index import grid_index


class Test(TestCase):
    def test_grid_index(self):
        results1 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(results1, 'myexample')

        results2 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 5, 6])
        self.assertEqual(results2, 'mam')

        results3 = grid_index([['m', 'y', 'e'], ['x', 'a', 'm'], ['p', 'l', 'e']], [1, 3, 7, 8])
        self.assertEqual(results3, 'mepl')

        results4 = grid_index(
            [['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'], ['e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']],
            [5, 7, 9, 3, 6, 6, 8, 8, 16, 13])
        self.assertEqual(results4, 'ooelccddrr')