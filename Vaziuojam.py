from turtle import Screen
from zaltys import Zaltys
from zalcio_pietus import Grobis
from zalcio_pilvas import Pilvas
import time

# Ekrano nustatymai
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Plikas Žaltys")
screen.tracer(0)

# Pagrindiniai objektai
zaltys = Zaltys()
grobis = Grobis()
Pilvas = Pilvas()

# Valdymo klavisai
screen.listen()
screen.onkey(zaltys.virsun, "w")
screen.onkey(zaltys.kairen, "a")
screen.onkey(zaltys.zemyn, "s")
screen.onkey(zaltys.desinen, "d")

# Zaidimas
zaidimas = True
while zaidimas:

    screen.update()
    time.sleep(0.1)
    zaltys.judejimas()

    # Grobio pagavimo sąlygos.
    if zaltys.head.distance(grobis) < 20:
        grobis.naujas_grobis()
        zaltys.prieaugis()
        Pilvas.pridek_skaiciu()
        # _________Testavimui___________
        # print(zaltys.greitis)  # testavimui konsoleje

    # Mirtis į sieną sąlygos
    if zaltys.head.xcor() > 290 or zaltys.head.xcor() < -290 or zaltys.head.ycor() > 290 or zaltys.head.ycor() < -290:
        zaidimas = False
        Pilvas.sakes()
        #_________Testavimui___________
        # print("mirtis i siena")
        # print(zaltys.greitis)

    # Mirtis atsitrenkus į save.
    for segmentas in zaltys.segmentai:
        if segmentas == zaltys.head:
            pass
        elif zaltys.head.distance(segmentas) < 5:
            zaidimas = False
            Pilvas.sakes()
            #_________Testavimui___________
            # print("mirtis i save")
            # print(zaltys.greitis)

screen.exitonclick()
