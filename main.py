from nakladak import Nakladak

tatra = Nakladak()

try:
    tatra.naloz(5000)
    tatra.vyloz(6000)
except Exception as e:
    print(e)