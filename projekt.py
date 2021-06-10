import random
import time
from tkinter import *
from entities import *



def setup():
    global spielfeld
    global canvasSpielfeld
    global canvasTextfeld

    #Erstellen eines Canvas, zur Darstellung von Spielfiguren und Leben
    canvasSpielfeld = Canvas(spielfeld, height=500, width=800)
    canvasSpielfeld.configure(bg="black")
    canvasSpielfeld.pack()

    #Erstellen des Canvas, zur Darstellung von Spieltext und Buttons
    canvasTextfeld = Canvas(spielfeld, height=500, width=800)
    canvasTextfeld.configure(bg="black")
    canvasTextfeld.pack()

    intro()

def intro():
    global introText, canvasTextfeld,button1
    intro1= "Du musst bis morgen ein Projekt abgeben!! "
    intro2= "Du hast nur noch 10 Stunden Zeit! "
    introText = canvasTextfeld.create_text(10,5, width=650, anchor=NW, text="", fill='white', font=("calibri", 45, "italic"))

    for x in range(len(intro1)):
        delay = 40*x
        text = intro1[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(introText, text=text)
        canvasTextfeld.after(delay, textUpdate)


    for x in range(len(intro2)):
        delay2 = delay + 40*x
        text = intro2[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(introText, text=text)
        canvasTextfeld.after(delay2 + 1000, textUpdate)

    button = Button(spielfeld, text="test", bg="black", command=lambda: ersteRunde())
    #canvasTextfeld.after(10000, button.place())
    button1 = Button(spielfeld, text="Quit", bg="black", fg="white", command= lambda: ersteRunde())
    canvasTextfeld.create_window(400,280,anchor="center", window=button1)


def ersteRunde():
    global canvasTextfeld
    canvasTextfeld.delete(introText)
    button1.destroy()




#Erstellen des Tkinter Fensters. Hintergrund wird auf schwarz gesetzt
spielfeld = Tk()
spielfeld.title("Pokemon in gut")
spielfeld.geometry("800x800")
spielfeld.configure(bg="black")


setup()


spielfeld.mainloop()











