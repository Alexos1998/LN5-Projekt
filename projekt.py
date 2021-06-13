import random
import time
from tkinter import *
from tkinter.font import Font

def setup():
    global canvasSpielfeld, canvasTextfeld, spielerFigurAnzeige, spielerFigur, projektFigurAnzeige, projektFigur

    canvasSpielfeld = Canvas(spielfeld, height=500, width=800)
    canvasSpielfeld.configure(bg="#fff")
    canvasSpielfeld.pack()

    #Erstellen des Canvas, zur Darstellung von Spieltext und Buttons
    canvasTextfeld = Canvas(spielfeld, height=300, width=800)
    canvasTextfeld.configure(bg="#fff")
    canvasTextfeld.pack()

    spielerFigur = PhotoImage(file="Assets/Gruppe.png")
    spielerFigurAnzeige = canvasSpielfeld.create_image(800, 330, anchor=W, image=spielerFigur)

    projektFigur = PhotoImage(file="Assets/Gruppe.png")
    projektFigurAnzeige = canvasSpielfeld.create_image(0, 100, anchor=E, image=projektFigur)

    figuren(800, 0)

def figuren(frames, durchlaeufe):
    global canvasSpielfeld, spielerFigurAnzeige, projektFigurAnzeige

    movespielerFigur = lambda: canvasSpielfeld.move(spielerFigurAnzeige,-5,0);frames -= 5
    canvasSpielfeld.after(frames*2, movespielerFigur)

    moveprojektFigur = lambda: canvasSpielfeld.move(projektFigurAnzeige,+5,0)
    canvasSpielfeld.after(frames*2, moveprojektFigur)



    if frames == 20:
        canvasSpielfeld.after(1700, lambda: intro())
    else:
        durchlaeufe +=1
        canvasSpielfeld.after(0, lambda: figuren(frames, durchlaeufe))

def intro():
    global introText, canvasTextfeld
    intro1= "Ein wildes PROJEKT ist aufgetaucht! "
    # intro2= "Du hast nur noch 10 Stunden Zeit! "
    introText = canvasTextfeld.create_text(10,5, width=750, anchor=NW, text="", font=("Press Start 2P", 35))

    for x in range(len(intro1)):
        delay = 40*x
        text = intro1[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(introText, text=text)
        canvasTextfeld.after(delay, textUpdate)


    # for x in range(len(intro2)):
    #     delay2 = delay + 1500 + 40*x
    #     text = intro2[:x]
    #     textUpdate = lambda text=text: canvasTextfeld.itemconfigure(introText, text=text)
    #     canvasTextfeld.after(delay2, textUpdate)


    spielfeld.after(delay + 500, lambda: buttonErsteRunde())

def buttonErsteRunde():
    global button1

    button1 = Button(spielfeld, text="Auf geht's", highlightthickness=0, bd=0, bg="#fff",fg="#555", command=lambda: ersteRunde())
    canvasTextfeld.create_window(400, 280, window=button1)
    spielfeld.bind("<KeyPress-Return>", lambda b: ersteRunde())

def ersteRunde():
    global canvasTextfeld, button1, delayFrage

    canvasTextfeld.delete(introText)
    button1.destroy()
    spielfeld.after(100, menu())

def menu():
    global menuButton1, menuButton2, menuButton3, canvasTextfeld, spielfeld, menuListMoves, menuListSpecial

    # menuListMoves = canvasTextfeld.create_text(10,5, width= 650, anchor = NW, text="Moves", fill="#000", font=("Press Start 2P", 35))
    # menuListSpecial = canvasTextfeld.create_text(280,5, width= 650, anchor = NW, text="Spezial", fill="#555", font=("Press Start 2P", 30))
    menuListMoves = Button(spielfeld, text="Moves", bg="#fff",
                         highlightthickness=0, bd=0, fg="#000",
                         font=("Press Start 2P", 30),
                         command= lambda: Move1())
    canvasTextfeld.create_window(10, 0, window=menuListMoves, anchor=NW)

    menuListSpecial = Button(spielfeld, text="Spezial", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555",
                         font=("Press Start 2P", 30),
                         command=lambda: Move1())
    canvasTextfeld.create_window(280, 0, window=menuListSpecial, anchor=NW)

    menuButton1 = Button(spielfeld, text="Power Nap", bg="#fff",
                         highlightthickness=0, bd=0, fg="#000",
                         font=("Press Start 2P", 25),
                         command=lambda: Move1())
    canvasTextfeld.create_window(100, 100, window=menuButton1, anchor=W)

    menuButton2 = Button(spielfeld, text="Energy Booster", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555",
                         font=("Press Start 2P", 20),
                         command=lambda: Move2())
    canvasTextfeld.create_window(100, 170, window=menuButton2, anchor=W)

    menuButton3 = Button(spielfeld, text="Kaffee Booster", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555",
                         font=("Press Start 2P", 20),
                         command=lambda: Move3())
    canvasTextfeld.create_window(100, 240, window=menuButton3, anchor=W)
    menuNavigation()

def menuNavigation():

    # Überprüfe des System-Inputs auf die Pfeiltasten und ENTER-Taste. Bei Pfeiltasten wird das Highlighting in der Funktion "menuHighlight" angepasst. Bei Enter wird die aktuelle Auswahl ausgeführt.
    spielfeld.bind("<KeyPress-Down>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Up>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Right>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Left>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Return>", lambda b: action())

def menuHighlight(keystroke):

    global  menuButton1, menuButton2, menuButton3, menuSelectionLeftRight, menuSelectionUpDown, menuListMoves, menuListSpecial


    if keystroke.keysym =="Right" or keystroke == "Right":
        menuSelectionUpDown = 0
        if menuSelectionLeftRight == 0:
            menuSelectionLeftRight += 1
    elif keystroke.keysym =="Left":
        menuSelectionUpDown = 0
        if menuSelectionLeftRight == 1:
            menuSelectionLeftRight -= 1

    if menuSelectionLeftRight < 1:
        menuListMoves.configure(fg="#000")#, font=("Press Start 2P",35))
        menuListSpecial.configure(fg="#555")#, font=("Press Start 2P", 30))
        menuButton1.configure(text="Power Nap")
        menuButton2.configure(text="Energy Booster")
        menuButton3.configure(text="Kaffee Booster")
    elif menuSelectionLeftRight == 1:
        menuListMoves.configure(fg="#555")#, font=("Press Start 2P", 30))
        menuListSpecial.configure(fg="#000")#, font=("Press Start 2P", 35))
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
        menuButton2.configure(fg="#555",font=("Press Start 2P",20))
        menuButton3.configure(fg="#555",font=("Press Start 2P",20))
    elif menuSelectionUpDown == 1:
        menuButton2.configure(fg="black", font=("Press Start 2P",25))
        menuButton1.configure(fg="#555",font=("Press Start 2P",20))
        menuButton3.configure(fg="#555",font=("Press Start 2P",20))
    elif menuSelectionUpDown == 2:
        menuButton3.configure(fg="black",font=("Press Start 2P",25))
        menuButton2.configure(fg="#555",font=("Press Start 2P",20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))

def action():
    te

#Erstellen des Tkinter Fensters. Hintergrund wird auf schwarz gesetzt
spielfeld = Tk()
spielfeld.title("Pokemon in gut")
spielfeld.geometry("800x800")
spielfeld.configure(bg="#555")


menuSelectionUpDown = 0
menuSelectionLeftRight = 0

setup()


spielfeld.mainloop()











