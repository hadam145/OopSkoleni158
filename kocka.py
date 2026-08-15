from zvire import Zvire


class Kocka(Zvire):

    def __init__(self, hmotnost, jmeno):
        super().__init__(hmotnost)
        self.jmeno = jmeno

    def vydej_zvuk(self):
        return "Mnau"

    def __str__(self):
        return "Kočka"