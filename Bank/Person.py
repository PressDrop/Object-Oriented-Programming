class Person:
    def __init__(self, fornavn: str, etternavn:str, telefonnummer:int):
        self.__fornavn = fornavn
        self.__etternavn = etternavn
        self.__telefonnummer = telefonnummer
    
    @property
    def fornavn(self):
        return self.__fornavn
    @property
    def etternavn(self):
        return self.__etternavn
    @property
    def telefonnummer(self):
        return self.__telefonnummer