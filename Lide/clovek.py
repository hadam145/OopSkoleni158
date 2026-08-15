# from abc import ABC, abstractmethod


#Třída Clovek podle které se tvoří objekty
class Clovek():

    _pocet_lidi = 0

    @staticmethod
    def pridej_cloveka():
        Clovek._pocet_lidi += 1

    @staticmethod
    def vrat_pocet_lidi():
        return Clovek._pocet_lidi

    # @abstractmethod
    # def vrat_povolani(self):
    #     pass

    #Konstruktor, přijíma paramtery jmeno a vek
    #A nastavuje atributy jmeno a vek
    def __init__(self, jmeno, vek):
        self.__jmeno = jmeno
        self.__vek = vek
        Clovek.pridej_cloveka()

    @property
    def jmeno(self):
        return self.__jmeno

    @property
    def vek(self):
        return self.__vek

    @vek.setter
    def vek(self, novy_vek):
        self.__vek = novy_vek

    # def get_vek(self):
    #     return self.__vek

    # def set_vek(self, vek):
    #     if not (vek < 0):
    #         self.__vek = vek

    #Metoda, která patří k třídě Clovek
    def vrat_pozdrav(self, pozdrav = "AHOJ"):
        return (f"{pozdrav}, jsem {self.jmeno}, "
              f"mám {self.__vek} let.")

    #Přepsání magické metody __str__()
    def __str__(self):
        return (f"Třída {__class__.__name__}"
                f"Jsem {self.jmeno}, "
                f"mám {self.vek} let.")
