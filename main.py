from Lide.clovek import Clovek

lenka = Clovek("Lenka",50)
petr = Clovek("Petr",50)
tomas = Clovek("Tomas",50)
david = Clovek("David",50)
marek = Clovek("Marek",50)
adam = Clovek("Adam",50)
honza = Clovek("Honza",50)


print(Clovek.vrat_pocet_lidi())

lide = [
    lenka,
    petr,
    tomas,
    david,
    marek,
    adam,
    honza
]
print(f"Pocet lidi :{len(lide)}")
