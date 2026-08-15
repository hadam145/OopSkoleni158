# Nový soubor nakladak.py
class Nakladak:

    nosnost = 3000
    def __init__(self):
        self._naklad = 0

    def naloz(self, hmotnost):
        if hmotnost > self.nosnost:
            raise Exception("Nelze nalozit vic nez je nosnost")
        else:
            self._naklad += hmotnost

    def vyloz(self, hmotnost):
        if hmotnost > self.nosnost:
            raise Exception("Nelze vylozit vic nez je naklad")
        self._naklad -= hmotnost

    def vypis(self):
        print(f"Mám naloženo {self._naklad} kg.")
