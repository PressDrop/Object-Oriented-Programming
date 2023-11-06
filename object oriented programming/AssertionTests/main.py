import unittest
import pytest

from BankKonto import BankKonto
from BSU import BSU
from SpareKonto import SpareKonto
from Person import Person


#The general strucure for the unittests
class AssertionTests(unittest):
    @pytest.fixture(scope='function')
    def init(self):
        miriam = Person('Miriam', 'Castillo Amo', 1234123123)
    def test_bankkonto(self):
        pass
    def test_BSU(self):
        pass
    def test_sparekonto(self):
        pass

if __name__ == '__main__':
    unittest.main()