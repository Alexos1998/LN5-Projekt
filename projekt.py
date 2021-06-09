import random
from tkinter import *
from entities import *

def auswahl():
    auswahlFeuer = Button(spielfeld, text="Feuer", command = lambda: element("Feuer"),
                            bg= "black",
                            fg= "red",
                            font= (20),
                            highlightthickness= 1,
                            bd= 0)
    auswahlErde = Button(spielfeld, text="Erde", command = lambda: element("Erde"),
                            bg= "Brown",
                            fg= "red",
                            font= (20),
                            highlightthickness= 1,
                            bd= 0)
    auswahlBlitz = Button(spielfeld, text="Blitz", command = lambda: element("Blitz"),
                            bg= "Yellow",
                            fg= "red",
                            font= (20),
                            highlightthickness= 1,
                            bd= 0)

    auswahlFeuer.grid(row=14, column=1, padx= 100)
    auswahlErde.grid(row=14, column=2)
    auswahlBlitz.grid(row=15, column=1)


def element(element):
    global Fighter1
    Fighter1 = Fighter(element)


def dmgCalc():

    print(f"Der Boss hat {Boss1.leben} Leben, hat einen Base-Schaden von {Boss1.baseAttack} und ist vom Typ {Boss1.type}\n")

    print(f"Das normale Monster hat {Normal1.leben} Leben, hat einen Base-Schaden von {Normal1.baseAttack} und ist vom typ {Normal1.type}")

spielfeld = Tk()
spielfeld.geometry("800x800")
spielfeld.title("Pokemon in gut")
spielfeld.configure(bg="black")

#auswahl()
canvastest = Canvas(spielfeld)
canvastest.configure(bg= "black",)
canvastest.grid(row= 10, column= 5)
canvasText = canvastest.create_text(10,10, text="", anchor= NW, fill = 'white')

intro = "Du musst bis morgen ein Projekt abgeben "

for x in range(len(intro)):
    text = intro[:x]
    textUpdate = lambda text=text: canvastest.itemconfigure(canvasText, text=text)
    canvastest.after(40*x, textUpdate)

spielfeld.mainloop()




