from turtle import Turtle
STARTAS = [(0, 0), (-20, 0), (-40, 0)] # startines koordinates pradiniams segmentams zalcio sukurimui
VIRSUN = 90
ZEMYN = 270
KAIREN = 180
DESINEN = 0

class Zaltys(Turtle):

    def __init__(self):
        super().__init__()
        self.segmentai = []
        self.zalcio_sukurimas()
        self.head = self.segmentai[0]
        self.greitis = 10

    def zalcio_sukurimas(self):
        for pos in STARTAS:
            self.segmento_nustatymas(pos)

    # Zalcio valdymas
    def virsun(self):
        if self.head.heading() != ZEMYN:
            self.head.setheading(VIRSUN)

    def zemyn(self):
        if self.head.heading() != VIRSUN:
            self.head.setheading(ZEMYN)

    def kairen(self):
        if self.head.heading() != DESINEN:
            self.head.setheading(KAIREN)

    def desinen(self):
        if self.head.heading() != KAIREN:
            self.head.setheading(DESINEN)

    # Zalcio segmentu judejimas ir elgsena
    def judejimas(self):
        for segm in range(len(self.segmentai) - 1, 0, -1): # einam per segmentus, start=pask segm indexas (zalcio ilgis - 1),
            # stop=0, step= -1
            naujas_x = self.segmentai[segm - 1].xcor()  # pries tai buvusio segmento x pos
            naujas_y = self.segmentai[segm - 1].ycor()  # pries tai buvusio segmento y pos
            self.segmentai[segm].goto(naujas_x, naujas_y)  # segmentas keliauja i pries tai buvusio vieta.
        self.head.forward(self.greitis)

    def segmento_nustatymas(self, position):
        naujas_seg = Turtle("circle")
        naujas_seg.color("yellow")
        # naujas_seg.turtlesize(stretch_len=2)
        naujas_seg.penup()
        naujas_seg.goto(position)
        self.segmentai.append(naujas_seg)


    def prieaugis(self):
        self.segmento_nustatymas(self.segmentai[-1].pos())
        # greicio ribos ir didejimo nustatymai
        if self.greitis < 35:
            self.greitis += 1

