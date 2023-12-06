from turtle import Turtle
vieta = "center"
sriftas = ("Courier", 24, "normal")

class Pilvas(Turtle):

    def __init__(self):
        super().__init__()
        self.suvalgyta = 0
        with open(r".\rekordas.txt") as rekordas:
            self.rekordas = int(rekordas.read())
        self.color("red")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.tasku_vaizdas()

    # tasku vaizdavimas
    def tasku_vaizdas(self):
        self.write(f"Suvalgyta: {self.suvalgyta}", align=vieta, font=sriftas)

    # tasku skaiciavimas
    def pridek_skaiciu(self):
        self.suvalgyta += 1
        self.clear()
        self.tasku_vaizdas()

    # zaidimo pabaiga
    def sakes(self):
        self.goto(0, 0)
        # Rekordo irasymas.
        if self.suvalgyta > self.rekordas:
            self.rekordas = self.suvalgyta
            with open("rekordas.txt", mode="w") as rekordas:
                rekordas.write(f"{self.rekordas}")
            with open("rekordas.txt") as rekordas:
                self.rekordas = int(rekordas.read())
            self.write(f"Šakės!\nJums priklauso\nnaujas rekordas:{self.rekordas}", align=vieta, font=sriftas)
        elif self.suvalgyta == self.rekordas:
            with open("rekordas.txt") as rekordas:
                self.rekordas = int(rekordas.read())
            self.write(f"Šakės!\nPakartojote rekordą:{self.rekordas}", align=vieta, font=sriftas)
        else:
            self.write(f"Šakės!\nRekordas yra:{self.rekordas}", align=vieta, font=sriftas)
        self.suvalgyta = 0



