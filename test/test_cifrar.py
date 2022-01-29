import os
import sys
import unittest


sys.path.append(os.getcwd())

from src.cifrar import Cifrador

class Tests(unittest.TestCase):

    def setUp(self):
        """ Crea una cifrador y le da un documento a descifrar"""
        self.c = Cifrador('probando123', 8, 4)


    def test_constructor(self):
        self.assertIsInstance(self.c, Cifrador)
        self.assertRaises(Exception, Cifrador, 'proba', 5, 7)


    def test_cifrar(self):
        criptograma, evaluaciones = self.c.cifrar()
        self.assertIsInstance(criptograma, bytes)
        self.assertEqual(len(evaluaciones), 8)
        for eval in evaluaciones:
            self.assertIsInstance(eval[1], int)

    def test_horner(self):
        self.assertEqual(self.c._horner(1, [6,2,3,2]), 13)
        self.assertEqual(self.c._horner(3, [6,2,3,2]), 93)

if __name__ == '__main__':
    unittest.main()
