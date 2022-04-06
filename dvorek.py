"""
scénář na dvorku
autor: Alex Olivier Michaud
"""
#importování
import random

#globalní listy
jmena_slepic = ["Pipinka", "slípka", "pipka", "pipina", "slepička"]
koryto = ["velká zrna", "malá zrna", "zbytky párku", "vařené brambory", "mrkev"]
miska = ["mléko"]

#Definování tříd
class Zvirata:
    """
    rodičovská třída
    """
    def __init__(self, jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo):
        """
        definující zkladní proměné
        :param jmeno: str
        :param druh: str
        :param velikost: int
        :param vek: int
        :param pocet_nohou: int
        :param nynejsi_misto: str
        :param oblibene_jidlo: list
        """
        self.jmeno = jmeno
        self.druh = druh
        self.velikost = velikost
        self.vek = vek
        self.pocet_nohou = pocet_nohou
        self.nynejsi_misto = nynejsi_misto
        self.oblibene_jidlo = oblibene_jidlo

    def go_to(self, misto):
        """
        funkce na přemístění objektu
        :param misto: místo kam jde
        :return: print
        """
        print(f"{self.jmeno} přeběhl/o/a z {self.nynejsi_misto} do {misto}")
        self.nynejsi_misto = misto

    def eat(self, jidlo):
        """
        :param jidlo: snězení jídla
        :return: print
        """
        print(f"{self.jmeno} snědl/a/o {jidlo}")

class Slepice(Zvirata):
    def __init__(self, jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo):
        """
        inheritance
        """
        super().__init__(jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo)

    def speak(self):
        """
        funkce na mluvení
        :return: print
        """
        print(f"{self.jmeno}: pipipi")
class Kocka(Zvirata):
    def __init__(self, jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, puvod, oblibene_jidlo):
        """
        inheritance + přidání původu té kočky
        :param puvod: str
        """
        super().__init__(jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo)
        self.puvod = puvod
    def speak(self):
        """
        funkce na mluvení
        :return: print
        """
        print(f"{self.jmeno}: mňau, mňau")

class Vrabec(Zvirata):
    def __init__(self, jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo):
        """
        inheritance
        """
        super().__init__(jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo)
    def speak(self):
        """
        funkce na mluvení
        :return: print
        """
        print(f"{self.jmeno}: lalalal")
class Kohout(Zvirata):
    def __init__(self, jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo):
        """
        inheritance
        """
        super().__init__(jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo)
    def speak(self):
        """
        funkce na mluvení
        :return: print
        """
        print(f"{self.jmeno}: kykiriký ")
class Pes(Zvirata):
    def __init__(self, jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo):
        """
        inheritance
        """
        super().__init__(jmeno, druh, velikost, vek, pocet_nohou, nynejsi_misto, oblibene_jidlo)

    def speak(self):
        """
        funkce na mluvení
        :return: print
        """
        print(f"{self.jmeno}: haf haf")


####Objekty
Pipinka = Slepice(jmena_slepic[0], "slepice", random.randint(20, 30), random.randint(1,5), 2, "stodoli", ["vařené brambory", "mrkev", "velká zrna"])
Slipka = Slepice(jmena_slepic[1], "slepice", random.randint(20, 30), random.randint(1,5), 2, "stodoli", ["vařené brambory", "mrkev", "velká zrna"])
Pipika = Slepice(jmena_slepic[2], "slepice", random.randint(20, 30), random.randint(1,5), 2, "stodoli", ["vařené brambory", "mrkev", "velká zrna"])
Pipina = Slepice(jmena_slepic[3], "slepice", random.randint(20, 30), random.randint(1,5), 2, "stodoli", ["vařené brambory", "mrkev", "velká zrna"])
Slepicka = Slepice(jmena_slepic[4], "slepice", random.randint(20, 30), random.randint(1,5), 2, "U stodoli", ["vařené brambory", "mrkev", "velká zrna"])
Kokrhac = Kohout("Kokrháč", "kohout", random.randint(30, 40), random.randint(4,7), 2, "stodoli", ["vařené brambory", "mrkev", "velká zrna"])
Kocka_domaci = Kocka("Mikeš", "kočka", random.randint(50,75), random.randint(2, 7), 4, "Okapu", "domaci",  ["mléko"])
Sousedovic_kocka = Kocka("Flíček", "kočka", random.randint(50,70), random.randint(2, 7), 4, "Misky", "sousedova", ["mléko"])
Alan = Pes("Alan", "pes", random.randint(70, 120), random.randint(1,9), 4, "terasy", ["zbytky párku"])
Rafaelo = Vrabec("Rafael", "vrabec", random.randint(5, 10), random.randint(1, 2), 2, "komína", ["malá zrna"])


#### Hlavní program
Kokrhac.speak()
print("Jídlo v korytě: ")
for i in koryto:
    print(i)
print("Jídlo v misce: ")
print(miska[0])
Kocka_domaci.go_to("misky")
if Kocka_domaci.velikost > Sousedovic_kocka.velikost:   #určení která kočka budejíst
    Kocka_domaci.eat("mléko")
else:
    Sousedovic_kocka.eat("mléko")
Pipinka.go_to("Korýtka")
Slipka.go_to("Korýtka")
Pipina.go_to("Korýtka")
Slipka.go_to("Korýtka")
Pipika.go_to("Korýtka")
Slepicka.go_to("Korýtka")
Kokrhac.go_to("Korýtka")
for i in Kokrhac.oblibene_jidlo:    #vyjezení jídla z koryta
    if i in koryto:
        jidlo = koryto.remove(i)
        print(f"Kohout a sledpice snědli {jidlo}")
Rafaelo.go_to("Korýtka")
je_dost_blizko = random.choice([True, False])
if je_dost_blizko:      #určení jestli vrabec bude jíst
    jidlo = koryto.remove("malá zrna")
    Rafaelo.eat("malá zrna")
else:
    print("vrabec se nestihl najíst")
Alan.go_to("Korýtka")
Alan.speak()
Pipinka.speak()
Slipka.speak()
Pipina.speak()
Slipka.speak()
Pipika.speak()
Slepicka.speak()
Kokrhac.speak()
Rafaelo.speak()
Sousedovic_kocka.speak()
Kocka_domaci.speak()
Pipinka.go_to("Dvorek")
Slipka.go_to("Dvorek")
Pipina.go_to("Dvorek")
Slipka.go_to("Dvorek")
Pipika.go_to("Dvorek")
Slepicka.go_to("Dvorek")
Kokrhac.go_to("Dvorek")
Rafaelo.go_to("Dvorek")
Sousedovic_kocka.go_to("Dvorek")
Kocka_domaci.go_to("Dvorek")
Alan.eat("zbytky párku")
print("Rafaelo: čimčarará")
print("Pes usl a dvorek utichl")


