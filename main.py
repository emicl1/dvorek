
class Hrdina:
    def __init__(self, health, name, strengt):
        self.health = health
        self.name = name
        self.strengt = strengt

    def mluv(self, veta):
        print(self.name + ": " +veta)

    def info(self):
        print(f"name: {self.name}")
        print(f"health: {self.health}")
        print(f"strenght: {self.strengt}")

    def fight(self, other):
        if other.health - self.strengt > self.health - other.strengt:
            print(f"{self.name} vs {other.name}")
            print(f"{other.name} won")
        else:
            print(f"{self.name} won")

class Zlyhridna(Hrdina):

    def __init__(self, jmeno):
        super().__init__(jmeno, strengt=300, health=60)

    def fight(self, other):
        print(f"{self.name} won")


matěj = Hrdina(100, "Matěj", 50)
pf = Hrdina(150, "Čmolík", 60)
tu = Zlyhridna("Ratatuj")
tu.info()
matěj.mluv("Pupu")
matěj.info()
matěj.fight(pf)

