from BankKonto import BankKonto
from Eier import Eier
class SpareKonto(BankKonto):
    def __init__(self, eier: Eier, kontonummer:str, maks_antall_uttak:int):
        super().__init__(eier, kontonummer)
        self.__maks_antall_uttak = maks_antall_uttak
        self.__antall_uttak = 0
    def ta_ut_penger(self, beløp: int) -> bool:
        if self.__maks_antall_uttak > self.__antall_uttak:
            if super().ta_ut_penger(beløp):
                self.__antall_uttak += 1
                return True
        print("")
        print("Du kan ikke gå over maks antall_uttak")
        return False
    def print_nåværende_beløp(self) -> None:
        print("")
        print(f"Ditt antall uttak er {self.__antall_uttak} og maks antall uttak er {self.__maks_antall_uttak}")

    @property
    def maks_antall_uttak(self):
        return self.__maks_antall_uttak
    @property
    def antall_uttak(self):
        return self.__antall_uttak

def main():
    HHermansen = Eier("Hege", "Hermansen", "12309192")
    spare_konto = SpareKonto(HHermansen,"1020.30.45678", 11)
    print(spare_konto)
    assert spare_konto.__saldo == 0, "Saldo må være satt til 0 ved start"
    spare_konto._sett_inn_penger(10)
    for i in range(11):
        spare_konto.ta_ut_penger(1)

if __name__ == "__main__":
    main()