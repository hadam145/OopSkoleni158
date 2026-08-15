
from clovek import Clovek

#Dědíme z třídy Clovek
class Programator(Clovek):

    def vrat_povolani(self):
        return "Programátor"

    #Konstruktor prográmátora má navíc jazyk
    def __init__(self, jmeno, vek, jazyk):
        super().__init__(jmeno, vek)
        self.jazyk = jazyk

    #Metoda vrat_pozdrav patří prográmátorovi
    # a volá buď tu metodu vrat_pozdrav z
    #prográmátora nebo z Cloveka
    #Využíváme polymorfismu
    def vrat_pozdrav(self, pozdrav = None):
        if pozdrav is None:
            return (f"Jsem programátor a programuju "
                    f"v {self.jazyk}")
        else:
            return super().vrat_pozdrav(pozdrav)

    #Přepsání magické metody __str__()
    def __str__(self):
        return (super().__str__() +
        f"{__class__.__name__} " +
                f"Programuju v {self.jazyk}")


