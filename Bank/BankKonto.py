from Person import Person
class BankKonto:
    def __init__(self, eier: Person, kontonummer: int):
        self.__eier = f"{eier.fornavn} {eier.etternavn}"
        self.__saldo = 0
        self.__kontonummer = kontonummer

        print(f"Nyoprettet konto:")
        print(" "*2, f"{'Eier'.ljust(10)} : {self.__eier}") 
        print(" "*2, f"{'Kontonummer'.ljust(10)} : {self.__kontonummer})") 
    #Hva som skal printes ut når du printer BankKonto objektet 
    def __str__(self) -> str:
        print("")
        return f"Konto: \n {' '*2} {'Eier'.ljust(10)} : {self.__eier}  \n {' '*2} {'Kontonummer'.ljust(10)} : {self.__kontonummer}  \n {' '*2} {'Saldo'.ljust(10)} : {self.__saldo}"
    def sett_inn_penger(self, beløp:int) -> bool:
        print("")
        if beløp >= 0:
            self.__saldo += beløp
            print(f"Du satt inn et beløp på {beløp}, du har nå {self.__saldo} kroner på kontoen")
            return True
        print(f"Du kan ikke sette inn et negativt beløp")
        return False
    def ta_ut_penger(self, beløp:int) -> bool:
        print("")
        if beløp >= 0 and beløp <= self.__saldo:
            self.__saldo -= beløp
            print(f"Du tokk ut {beløp} kroner, du har nå {self.__saldo} kroner på kontoen")
            return True
        if beløp > self.__saldo:
            print(f"Beløpet du prøvde å sette inn, {beløp}, er større enn pengene du har på kontoen {self.__saldo}")
            return False
        print("Du kan ikke ta ut et negativt beløp")
        return False

    @property
    def saldo(self):
        return self.__saldo
def main():
    HHermansen = Person("Hege", "Hermansen", "12309192")
    konto = BankKonto(HHermansen,"1020.30.45678")
    konto.sett_inn_penger(10)
    print(konto.saldo)

if __name__ == '__main__':
    main()