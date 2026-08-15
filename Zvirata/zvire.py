class Zvire:
    def __init__(self, hmotnost):
        self._hmotnost = hmotnost

    @property
    def letave(self):
        return self._hmotnost < 9

    def nakrm(self, hmotnost):
        self._hmotnost += hmotnost

    def vydej_zvuk(self):
        return ""

    def __str__(self):
        return "Zvire"

    def vypis(self):
        return (f"Zvire má hmotnost {self._hmotnost} "
                f"a zvire je letave: {self.letave}")
