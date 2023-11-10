import unittest
import sys

#Make sure to cd to assertiontests
sys.path.append('..')
from BankKonto import BankKonto
from Eier import Eier
#The general strucure for the unittests
class AssertionTests(unittest.TestCase):
    #Note that now every test case happends under the same AssertionTest, which is bad pracisce
    #However let's just say this is testing the functionality of the entire service

    #Testing initail feature of test_bankonto
    def setUp(self) -> None:
        miriam = Eier('Miriam', 'Castillo Amo', 1234123123)
        self.miriam_bankkonto = BankKonto(miriam, 123123123) 
        return super().setUp()
    def test_bankkonto_adding(self):
        # Initial

        self.assertEqual(0, self.miriam_bankkonto.saldo)

        # Preparation

        self.miriam_bankkonto.sett_inn_penger(10)

        # Testing

        self.assertEqual(10, self.miriam_bankkonto.saldo)
    def test_bankkonto_removing(self):
        # Initial 

        #Show that saldo miriam_bankonto gets reset for each test
        self.assertEqual(0, self.miriam_bankkonto.saldo)

        # Perparation 

        self.miriam_bankkonto.sett_inn_penger(100)
        self.miriam_bankkonto.ta_ut_penger(50)
        # Testing

        self.assertEqual(50, self.miriam_bankkonto.saldo)

    def test_bankonto_out_of_balance(self):
        # Initial 

        #No futher inital requiered

        # Preparation

        self.miriam_bankkonto.sett_inn_penger(1)
        self.miriam_bankkonto.ta_ut_penger(11)

        # Testing

        self.assertEqual(1, self.miriam_bankkonto.saldo)
        self.assertFalse(self.miriam_bankkonto.ta_ut_penger(11))

    def test_bankkonto_readonly(self):
        # Initial

        #No more initial

        # Preparation
        self.miriam_bankkonto.__saldo = 2

        # Test

        self.assertEqual(0, self.miriam_bankkonto.saldo)





if __name__ == '__main__':
    unittest.main()