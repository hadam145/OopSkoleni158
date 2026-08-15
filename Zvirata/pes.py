from zvire import Zvire


class Pes(Zvire):

    def __init__(self, hmotnost, obojek):
        super().__init__(hmotnost)
        self.obojek = obojek

    def vydej_zvuk(self):
        return "HAF HAF"

    def __str__(self):
        return "Pes"