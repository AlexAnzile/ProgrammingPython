import unittest
from es7 import somma 

class TestSomma(unittest.TasteCase):

    def test_somma(self):
        self.asserEqual(somma(1,1), 2)
        self.asserEqual(somma(1.5,2.5), 4)