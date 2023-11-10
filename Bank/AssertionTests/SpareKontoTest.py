import unittest
import sys


#Make sure to cd to assertiontests
sys.path.append('..')
from SpareKonto import SpareKonto 
from Eier import Eier


#This test will test new features added upon BSU 
#Given that BSU inherits from BankKonto we will assume that the tests that worked on BankKonto works on BSU
class AssertionTests(unittest.TestCase):
    #Not that there is no real reason for setup given that there is only one test case
    def test_sparekonto_exceed_maxwithdrawls(self):
        # Initial
        miriam = Eier('Miriam', 'Castillo Amo', 1234123123)
        self.miriam_bankkonto = SpareKonto(miriam, 123123123, 10) 

        self.miriam_bankkonto.sett_inn_penger(1000)
        
        # Preperation
        #This should cap after 10 because the max withdrawls is set to be 10
        for i in range(100):
            self.miriam_bankkonto.ta_ut_penger(1)

        #Test

        self.assertEqual(990, self.miriam_bankkonto.saldo)
        self.assertFalse(self.miriam_bankkonto.ta_ut_penger(1))


if __name__ == '__main__':
    unittest.main()