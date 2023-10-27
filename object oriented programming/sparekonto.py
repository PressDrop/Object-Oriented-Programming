from main import BankKonto
from person import Person
class SpareKonto(BankKonto):
    def __init__(self, eier: Person, kontonummer:str, maks_antall_uttak:int):
        super().__init__(eier, kontonummer)
        self.maks_antall_uttak = maks_antall_uttak
        self.antall_uttak = 0
    def ta_ut_penger(self, beløp: int) -> bool:
        if self.maks_antall_uttak > self.antall_uttak:
            if super().ta_ut_penger(beløp):
                self.antall_uttak += 1
                return True
        print("")
        print("Du kan ikke gå over maks antall_uttak")
        return False
    def print_nåværende_beløp(self) -> None:
        print("")
        print(f"Ditt antall uttak er {self.antall_uttak} og maks antall uttak er {self.maks_antall_uttak}")

def main():
    HHermansen = Person("Hege", "Hermansen", "12309192")
    spare_konto = SpareKonto(HHermansen,"1020.30.45678", 11)
    print(spare_konto)
    spare_konto.sett_inn_penger(10)
    for i in range(11):
        spare_konto.ta_ut_penger(1)

if __name__ == "__main__":
    main()