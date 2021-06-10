import random
import time
from tkinter import *
from entities import *



def setup():
    global spielfeld, canvasSpielfeld, canvasTextfeld

    #Erstellen eines Canvas, zur Darstellung von Spielfiguren und Leben
    canvasSpielfeld = Canvas(spielfeld, height=500, width=800)
    canvasSpielfeld.configure(bg="black")
    canvasSpielfeld.pack()

    #Erstellen des Canvas, zur Darstellung von Spieltext und Buttons
    canvasTextfeld = Canvas(spielfeld, height=300, width=800)
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



    button1 = Button(spielfeld, text="Quit", bg="black", fg="white",command= lambda: ersteRunde())
    spielfeld.after(delay2 + 1200, lambda: buttonErsteRunde())

def buttonErsteRunde():
    global button1
    canvasTextfeld.create_window(400, 280, window=button1)

def ersteRunde():
    global canvasTextfeld, button1
    canvasTextfeld.delete(introText)
    button1.destroy()




#Erstellen des Tkinter Fensters. Hintergrund wird auf schwarz gesetzt
spielfeld = Tk()
spielfeld.title("Pokemon in gut")
spielfeld.geometry("800x800")
spielfeld.configure(bg="black")


setup()


spielfeld.mainloop()











