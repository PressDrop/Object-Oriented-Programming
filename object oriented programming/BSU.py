from BankKonto import BankKonto
from Person import Person
class BSU(BankKonto):
    def __init__(self, eier: Person, kontonummer:str, maksbeløp: float):
        super().__init__(eier, kontonummer)
        self.nåværende_beløp = 0
        self.maksbeløp = maksbeløp
    def ta_ut_penger(self, beløp: int) -> bool:
        if (self.nåværende_beløp+beløp) <= self.maksbeløp and beløp > 0:
            if super().ta_ut_penger(beløp):
                self.nåværende_beløp += beløp
                return True
        print("")
        print(f"Du kan ikke gå over maksbeløpet {self.nåværende_beløp+beløp} som du har satt på kontoen {self.maksbeløp}")
        return False
    def print_nåværende_beløp(self) -> None:
        print("")
        print(f"Ditt nåværende_beløp er {self.nåværende_beløp} og maksbeløp er {self.maksbeløp}")
def main():
    HHermansen = Person("Hege", "Hermansen", "12309192")
if __name__ == '__main__':
    main()