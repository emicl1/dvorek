import random
jmena_slepic = ["Pipinka", "slípka", "pipka", "pipina", "slepička"]
koryto = ["velká zrna", "malá zrna", "zbytky párku", "vařené brambory", "mrkev"]
class Zvirata:
    def __init__(self, jmeno=str, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str):
        self.jmeno = jmeno
        self.druh = druh
        self.velikost = velikost
        self.vek = vek
        self.pocet_nohou = pocet_nohou
        self.nynejsi_misto = nynejsi_misto

    def go_to(self, misto):
        print(f"{self.jmeno} přešlo z {self.nynejsi_misto} do {misto}")
        self.nynejsi_misto = misto

    def eat(self, jidlo):
        print(f"{self.jmeno} snědlo {jidlo}")

class Slepice(Zvirata):
    def __init__(self, jmeno, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str):
        super().__init__(jmeno, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str)

    def speak(self):
        print(f"{self.jmeno}: pipipi")
class Kocka(Zvirata):
    def __init__(self, jmeno=str, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str, puvod=str):
        super().__init__(jmeno=str, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str)
        self.puvod = puvod
    def speak(self):
        print(f"{self.jmeno}: mňau, mňau")

class Vrabec(Zvirata):
    def __init__(self, jmeno=str, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str):
        super().__init__(jmeno=str, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str)
    def speak(self):
        print(f"{self.jmeno}: lalalal")
class Kohout(Zvirata):
    def __init__(self, jmeno=str, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str):
        super().__init__(jmeno=str, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str)
    def speak(self):
        print(f"{self.jmeno}: kykiriký ")
class Pes(Zvirata):
    def __init__(self, jmeno=str, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str):
        super().__init__(jmeno=str, druh=str, velikost=int, vek=int, pocet_nohou=int, nynejsi_misto=str)

    def speak(self):
        print(f"{self.jmeno}: haf haf")


list_slepic = []
for i in range(5):
    list_slepic.append(Slepice(jmena_slepic[i], "slepice", random.randint(20, 30), random.randint(1,5), 2, "U koryta")

