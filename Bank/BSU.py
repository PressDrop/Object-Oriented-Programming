from BankKonto import BankKonto
from Eier import Eier
class BSU(BankKonto):
    def __init__(self, eier: Eier, kontonummer:str, maksbeløp: float):
        super().__init__(eier, kontonummer)
        self.__nåværende_beløp = 0
        self.__maksbeløp = maksbeløp
    def ta_ut_penger(self, beløp: int) -> bool:
        if (self.__nåværende_beløp+beløp) <= self.__maksbeløp and beløp >= 0:
            if super().ta_ut_penger(beløp):
                self.__nåværende_beløp += beløp
                return True
        print("")
        print(f"Du kan ikke gå over maksbeløpet {self.__nåværende_beløp+beløp} som du har satt på kontoen {self.__maksbeløp}")
        return False
    def print_nåværende_beløp(self) -> None:
        print("")
        print(f"Ditt nåværende_beløp er {self.__nåværende_beløp} og maksbeløp er {self.__maksbeløp}")
    
    @property
    def nåværende_beløp(self):
        return self.__nåværende_beløp
    @property
    def maksbeløp(self):
        return self.__maksbeløp
def main():
    HHermansen = Eier("Hege", "Hermansen", "12309192")
if __name__ == '__main__':
    main()