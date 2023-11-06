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
    bsu_konto = BSU(HHermansen,"1020.30.45678", 10000)
    print(bsu_konto)
    assert bsu_konto.saldo == 0, "Saldo må være satt til 0 ved start"
    bsu_konto.sett_inn_penger(10001)
    assert bsu_konto.saldo == 10001, "Saldoen må være det den er blitt satt til å være 0 + 10001"
    bsu_konto.ta_ut_penger(10001)
    assert bsu_konto.saldo == 10001, "Du kan ikke ta ut mer enn penger enn du har satt maksbeløpet til å være"
    bsu_konto.sett_inn_penger(10)
    assert bsu_konto.saldo == 10011
    bsu_konto.ta_ut_penger(10001)
    assert bsu_konto.saldo == 10011, "Du kan fremdeles ikke ta ut mer"
    bsu_konto.ta_ut_penger(10000)
    assert bsu_konto.saldo == 11, "Du skal kunne ta ut maksbeløpet"
if __name__ == '__main__':
    main()