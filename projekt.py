import random
import time
from tkinter import *
from tkinter.font import Font

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
    global canvasTextfeld, button1, delayFrage, menuSelectionUpDown

    canvasTextfeld.delete(introText)
    button1.destroy()
    spielfeld.after(100, lambda: menu())
    menuNavigation()

def menuNavigation():
    global menuSelectionUpDown

    spielfeld.bind("<KeyPress-Down>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Up>", lambda b: menuHighlight(b))

    spielfeld.bind("<KeyPress-Right>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Left>", lambda b: menuHighlight(b))

    spielfeld.bind("<KeyPress-Return>", lambda b: print("geht"))

def menu():
    global menuButton1, menuButton2, menuButton3, canvasTextfeld, spielfeld, menuListMoves, menuListSpecial

    menuListMoves = canvasTextfeld.create_text(10,5, width= 650, anchor = NW, text="Moves", fill="#000", font=("Press Start 2P", 35))
    menuListSpecial = canvasTextfeld.create_text(280,5, width= 650, anchor = NW, text="Spezial", fill="#333", font=("Press Start 2P", 30))


    menuButton1 = Button(spielfeld, text="Power Nap", bg="white",
                         highlightthickness=0, bd=0, fg="#000",
                         font=("Press Start 2P", 25),
                         command=lambda: print("Funktioniert super"))
    canvasTextfeld.create_window(100, 100, window=menuButton1, anchor=W)

    menuButton2 = Button(spielfeld, text="Energy Booster", bg="white",
                         highlightthickness=0, bd=0, fg="#333",
                         font=("Press Start 2P", 20),
                         command=lambda: print("Funktioniert super"))
    canvasTextfeld.create_window(100, 170, window=menuButton2, anchor=W)

    menuButton3 = Button(spielfeld, text="Kaffee Booster", bg="white",
                         highlightthickness=0, bd=0, fg="#333",
                         font=("Press Start 2P", 20),
                         command=lambda: print("Funktioniert super"))
    canvasTextfeld.create_window(100, 240, window=menuButton3, anchor=W)

#def menuLeftRight(keystroke):


def menuHighlight(keystroke):

    global menuSelectionUpDown, menuButton1, menuButton2, menuButton3, menuSelectionLeftRight, canvasTextfeld, menuListMoves, menuListSpecial


    if keystroke.keysym =="Right":
        menuSelectionUpDown = 0
        if menuSelectionLeftRight == 0:
            menuSelectionLeftRight += 1
    elif keystroke.keysym =="Left":
        menuSelectionUpDown = 0
        if menuSelectionLeftRight == 1:
            menuSelectionLeftRight -= 1

    if menuSelectionLeftRight < 1:
        canvasTextfeld.itemconfigure(menuListMoves, fill="#000", font=("Press Start 2P",35))
        canvasTextfeld.itemconfigure(menuListSpecial, fill="#333", font=("Press Start 2P", 30))
        menuButton1.configure(text="Power Nap")
        menuButton2.configure(text="Energy Booster")
        menuButton3.configure(text="Kaffee Booster")
    elif menuSelectionLeftRight == 1:
        canvasTextfeld.itemconfigure(menuListMoves, fill="#333", font=("Press Start 2P", 30))
        canvasTextfeld.itemconfigure(menuListSpecial, fill="#000", font=("Press Start 2P", 35))
        menuButton1.configure(text="Gruppenarbeit")
        menuButton2.configure(text="Nachtschicht")
        menuButton3.configure(text="Keine Idee mehr")

    if keystroke.keysym == "Down":
        if menuSelectionUpDown < 2:
            menuSelectionUpDown += 1
    elif keystroke.keysym == "Up":
        if menuSelectionUpDown > 0:
            menuSelectionUpDown -= 1

    if menuSelectionUpDown == 0:
        menuButton1.configure(fg="black", font=("Press Start 2P",25))
        menuButton2.configure(fg="#333",font=("Press Start 2P",20))
        menuButton3.configure(fg="#333",font=("Press Start 2P",20))
    elif menuSelectionUpDown == 1:
        menuButton2.configure(fg="black", font=("Press Start 2P",25))
        menuButton1.configure(fg="#333",font=("Press Start 2P",20))
        menuButton3.configure(fg="#333",font=("Press Start 2P",20))
    elif menuSelectionUpDown == 2:
        menuButton3.configure(fg="black",font=("Press Start 2P",25))
        menuButton2.configure(fg="#333",font=("Press Start 2P",20))
        menuButton1.configure(fg="#333", font=("Press Start 2P", 20))



#Erstellen des Tkinter Fensters. Hintergrund wird auf schwarz gesetzt
spielfeld = Tk()
spielfeld.title("Pokemon in gut")
spielfeld.geometry("800x800")
spielfeld.configure(bg="#333")

menuSelectionUpDown = 0
menuSelectionLeftRight = 0

setup()
intro()
figuren()

spielfeld.mainloop()











