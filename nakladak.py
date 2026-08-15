# Nový soubor nakladak.py
class Nakladak:

    nosnost = 3000
    def __init__(self):
        self._naklad = 0

    def naloz(self, hmotnost):
        if hmotnost > self.nosnost:
            print("Nelze nalozit vic nez je nosnost")
        else:
            self._naklad += hmotnost

    def vyloz(self, hmotnost):

        self._naklad -= hmotnost

    def vypis(self):
        print(f"Mám naloženo {self._naklad} kg.")
