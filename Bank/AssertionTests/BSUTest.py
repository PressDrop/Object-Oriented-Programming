import unittest
import sys


#Make sure to cd to assertiontests
sys.path.append('..')
from BSU import BSU 
from Eier import Eier


#This test will test new features added upon BSU 
#Given that BSU inherits from BankKonto we will assume that the tests that worked on BankKonto works on BSU
class AssertionTests(unittest.TestCase):
    #Same setup as found in the test found for BankKonto except that we now init for BSU
    def setUp(self) -> None:
        miriam = Eier('Miriam', 'Castillo Amo', 1234123123)
        self.miriam_bankkonto = BSU(miriam, 123123123, 1000) 
        return super().setUp()
    #Note that 1000 has been set to be the max amount to be withdrawn for every test

    def test_BSU_exeed_maxwithdraw(self):
        # Initial 

        self.miriam_bankkonto.sett_inn_penger(10000)

        # Preparation 

        self.miriam_bankkonto.ta_ut_penger(2000) 

        # Test 

        self.assertEqual(10000, self.miriam_bankkonto.saldo)  
        #Check that you can withdraw money if it doesnt exceed amount
        self.assertTrue(self.miriam_bankkonto.ta_ut_penger(1)) 
    def test_bsu_maxwithdraw_saved(self):
        #This test will do almost the same as the last, but it will check that if
        #two sums comined exceed the max withdrawl the second will not go through 
        #but the first goes thorugh

        # Initial

        self.miriam_bankkonto.sett_inn_penger(1500)

        # Preparation

        self.miriam_bankkonto.ta_ut_penger(700)
        self.miriam_bankkonto.ta_ut_penger(700)

        # Test
        
        self.assertEqual(800, self.miriam_bankkonto.saldo)





if __name__ == '__main__':
    unittest.main()