from Person import Person
class BankKonto:
    def __init__(self, eier: Person, kontonummer: int):
        self.eier = f"{eier.fornavn} {eier.etternavn}"
        self.saldo = 0
        self.kontonummer = kontonummer

        print(f"Nyoprettet konto:")
        print(" "*2, f"{'Eier'.ljust(10)} : {self.eier}") 
        print(" "*2, f"{'Kontonummer'.ljust(10)} : {self.kontonummer})") 
    #Hva som skal printes ut når du printer BankKonto objektet 
    def __str__(self) -> str:
        print("")
        return f"Konto: \n {' '*2} {'Eier'.ljust(10)} : {self.eier}  \n {' '*2} {'Kontonummer'.ljust(10)} : {self.kontonummer}  \n {' '*2} {'Saldo'.ljust(10)} : {self.saldo}"
    def sett_inn_penger(self, beløp:int) -> bool:
        print("")
        if beløp >= 0:
            self.saldo += beløp
            print(f"Du satt inn et beløp på {beløp}, du har nå {self.saldo} kroner på kontoen")
            return True
        print(f"Du kan ikke sette inn et negativt beløp")
        return False
    def ta_ut_penger(self, beløp:int) -> bool:
        print("")
        if beløp >= 0 and beløp <= self.saldo:
            self.saldo -= beløp
            print(f"Du tokk ut {beløp} kroner, du har nå {self.saldo} kroner på kontoen")
            return True
        if beløp > self.saldo:
            print(f"Beløpet du prøvde å sette inn, {beløp}, er større enn pengene du har på kontoen {self.saldo}")
            return False
        print("Du kan ikke ta ut et negativt beløp")
        return False
def main():
    HHermansen = Person("Hege", "Hermansen", "12309192")
    konto = BankKonto(HHermansen,"1020.30.45678")
    assert konto.saldo == 0, "Saldo må være satt til 0 ved start"
    print(konto)
    konto.sett_inn_penger(10)

if __name__ == '__main__':
    main()