import random
import time
from tkinter import *
from entities import *

def setup():
    global spielfeld, canvasSpielfeld, canvasTextfeld, img

    canvasSpielfeld = Canvas(spielfeld, height=500, width=800)
    canvasSpielfeld.configure(bg="white")
    canvasSpielfeld.pack()

    #Erstellen des Canvas, zur Darstellung von Spieltext und Buttons
    canvasTextfeld = Canvas(spielfeld, height=300, width=800)
    canvasTextfeld.configure(bg="white")
    canvasTextfeld.pack()

def intro():
    global introText, canvasTextfeld
    intro1= "Du musst bis morgen ein Projekt abgeben!! "
    intro2= "Du hast nur noch 10 Stunden Zeit! "
    introText = canvasTextfeld.create_text(10,5, width=750, anchor=NW, text="", font=("Press Start 2P", 35))

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


    spielfeld.after(delay2 + 1200, lambda: buttonErsteRunde())

def buttonErsteRunde():
    global button1
    button1 = Button(spielfeld, text="Auf geht's", highlightthickness=0, bd=0, bg="white",fg="#333", command=lambda: ersteRunde())
    canvasTextfeld.create_window(400, 280, window=button1)
    spielfeld.bind("<KeyPress-Return>", lambda b: ersteRunde())

def figuren():
    global canvasSpielfeld, spielerFigur, figurAnzeige
    spielerFigur = PhotoImage(file="Assets/Gruppe.png")
    figurAnzeige = canvasSpielfeld.create_image(20, 220, anchor=NW, image=spielerFigur, tags="figure")


def ersteRunde():
    global canvasTextfeld, button1, delayFrage, menuselection
    canvasTextfeld.delete(introText)
    button1.destroy()
    #canvasSpielfeld.delete("figure")
    frage()
    spielfeld.after(delayFrage, lambda: menu())
    menuNavigation()

def menuNavigation():

    spielfeld.bind("<KeyPress-Down>", lambda b:test(b))
    spielfeld.bind("<KeyPress-Up>", lambda b: test(b))
    spielfeld.bind("<KeyPress-Right>", lambda b: test(b))
    spielfeld.bind("<KeyPress-Left>", lambda b: test(b))
    spielfeld.bind("<KeyPress-Return>", lambda b: print("geht"))

def menu():
    global menuButton1, menuButton2, menuButton3, canvasTextfeld, spielfeld, menuselection

    menuButton1 = Button(spielfeld, text="Power Nap", bg="white",
                         highlightthickness=0, bd=0, fg="#333",
                         font=("Press Start 2P", 25),
                         command=lambda: print("Funktioniert super"))
    canvasTextfeld.create_window(100, 100, window=menuButton1, anchor=W)

    menuButton2 = Button(spielfeld, text="Energy Booster", bg="white",
                         highlightthickness=0, bd=0, fg="#333",
                         font=("Press Start 2P", 20),
                         command=lambda: print("Funktioniert super"))
    canvasTextfeld.create_window(100, 170, window=menuButton2, anchor=W)

    menuButton3 = Button(spielfeld, text="Kaffe Booster", bg="white",
                         highlightthickness=0, bd=0, fg="#333",
                         font=("Press Start 2P", 20),
                         command=lambda: print("Funktioniert super"))
    canvasTextfeld.create_window(100, 240, window=menuButton3, anchor=W)


def test(keystroke):
    global menuButton1, menuButton2, menuButton3, menuselection
    if keystroke.keysym == "Down":
        if menuselection < 2:
            menuselection += 1
    elif keystroke.keysym == "Up":
        if menuselection > 0:
            menuselection -= 1

    if menuselection < 1:
        menuButton1.configure(font=("Press Start 2P",25))
        menuButton2.configure(font=("Press Start 2P",20))
        menuButton3.configure(font=("Press Start 2P",20))
    elif menuselection == 1:
        menuButton2.configure(font=("Press Start 2P",25))
        menuButton1.configure(font=("Press Start 2P",20))
        menuButton3.configure(font=("Press Start 2P",20))
    elif menuselection > 1:
        menuButton3.configure(font=("Press Start 2P",25))
        menuButton1.configure(font=("Press Start 2P",20))
        menuButton2.configure(font=("Press Start 2P",20))

def frage():
    global canvasTextfeld, delayFrage
    frageSpielbeginn = "Moves "
    frageSpielbeginnText = canvasTextfeld.create_text(10,5, width= 650, anchor = NW, text="", fill="#333", font=("Press Start 2P", 30))

    for x in range(len(frageSpielbeginn)):
        delayFrage = 40 * x
        frage = frageSpielbeginn[:x]
        frageUpdate = lambda frage=frage: canvasTextfeld.itemconfigure(frageSpielbeginnText, text=frage)
        canvasTextfeld.after(delayFrage, frageUpdate)


#Erstellen des Tkinter Fensters. Hintergrund wird auf schwarz gesetzt
spielfeld = Tk()
spielfeld.title("Pokemon in gut")
spielfeld.geometry("800x800")
spielfeld.configure(bg="#333")

menuselection = 0

setup()
intro()
figuren()

spielfeld.mainloop()











