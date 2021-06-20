import random
import time
from tkinter import *
from tkinter.font import Font

def setup():
    global canvasSpielfeld, canvasTextfeld, spielerFigurAnzeige, spielerFigur, projektFigurAnzeige, projektFigur, balken

    canvasSpielfeld = Canvas(spielfeld, height=500, width=800)
    canvasSpielfeld.configure(bg="#fff")
    canvasSpielfeld.pack()

    #Erstellen des Canvas, zur Darstellung von Spieltext und Buttons
    canvasTextfeld = Canvas(spielfeld, height=300, width=800)
    canvasTextfeld.configure(bg="#fff")
    canvasTextfeld.pack()

    spielerFigur = PhotoImage(file="Assets/Images/Gruppe.png")
    spielerFigurAnzeige = canvasSpielfeld.create_image(800, 330, anchor=W, image=spielerFigur)

    projektFigur = PhotoImage(file="Assets/Images/coronavirus.png")
    projektFigurAnzeige = canvasSpielfeld.create_image(0, 150, anchor=E, image=projektFigur)

    #balken = canvasSpielfeld.create_rectangle(700, 370, 500, 420, fill="green")


    figuren(800, 0)

def figuren(frames, durchlaeufe):
    global spielerFigurAnzeige, projektFigurAnzeige, currentKP, balken

    movespielerFigur = lambda: canvasSpielfeld.move(spielerFigurAnzeige,-5,0)
    canvasSpielfeld.after(durchlaeufe*10, movespielerFigur)

    moveprojektFigur = lambda: canvasSpielfeld.move(projektFigurAnzeige,+5,0)
    canvasSpielfeld.after(durchlaeufe*10, moveprojektFigur)

    frames -= 5

    if frames == 20:
        canvasSpielfeld.after(1700, lambda: intro())
        canvasSpielfeld.after(1700, lambda: spielfeldGraphik(1,1))

    else:
        durchlaeufe +=1
        figuren(frames, durchlaeufe)

def spielfeldGraphik(spieler,projekt):
    global currentKP, spielerArrow, nameSpieler, projektArrow, healthbarProjektWhite, healthbarProjektColor, healthbarSpielerWhite, healthbarSpielerColor, currentHealthBarSpieler


    spielerName = canvasSpielfeld.create_text(123,90,text="PROJEKT", anchor=SW, font=("Press Start 2P", 18), tags="KP")
    projektName = canvasSpielfeld.create_text(500, 370, text=nameSpieler, anchor= SW, font=("Press Start 2P", 18), tags="KP")

    spielerArrow = PhotoImage(file="Assets/Images/arrowSpieler.png")
    spielerHealthBarArrow = canvasSpielfeld.create_image(410, 410, anchor=W, image=spielerArrow)

    projektArrow = PhotoImage(file="Assets/Images/arrowProjekt.png")
    projektHealthBarArrow = canvasSpielfeld.create_image(45, 120, anchor=W, image=projektArrow)

    # healthColorSpieler = "green" if spieler >= 0.8 else "orange" if spieler < 0.8 and spieler >= 0.5 else "yellow" if spieler < 0.5 and spieler >= 0.2 else "red"
    # healthColorProjekt = "green" if projekt >= 0.8 else "orange" if projekt < 0.8 and projekt >= 0.5 else "yellow" if projekt < 0.5 and projekt >= 0.2 else "red"

    if spieler == 1:
        currentHealthBarProjekt = 200 * projekt + 123
        currentHealthBarSpieler = 200 * spieler + 500

        healthbarProjektWhite = canvasSpielfeld.create_rectangle(123, 100, 323, 120, fill="white")
        healthbarProjektColor = canvasSpielfeld.create_rectangle(123, 100, 323, 120, fill="green")

        healthbarSpielerWhite = canvasSpielfeld.create_rectangle(700, 400, 500, 380, fill="white")
        healthbarSpielerColor = canvasSpielfeld.create_rectangle(700, 400, 500, 380, fill="green")

        kraftpunkte = canvasSpielfeld.create_text(100,112,text="KP:", font=("Press Start 2P", 15), tags="KP")
        kraftpunkte = canvasSpielfeld.create_text(477, 392, text="KP:", font=("Press Start 2P", 15), tags="KP")

        currentKPIndex = str(int(100 * spieler)) + "/ 100"

        currentKP = canvasSpielfeld.create_text(700, 425, text= "100/ 100", anchor= E, font=("Press Start 2P", 18))


def lifeAnimation(spieler,projekt):
    global healthbarProjektColor, healthbarSpielerColor, currentLifeProjekt, currentLifeSpieler, changeLifeColor, balken

    healthDiffSpieler = int(round(currentLifeSpieler - spieler,2)*100)
    healthDiffProjekt = int(round(currentLifeProjekt - projekt,2)*100)


    #if durchlaeufeS > 0:
    healthBarReductionSpieler(1, healthDiffSpieler)
    # if durchlaeufeP > 0:
    healthBarReductionProjekt(1, healthDiffProjekt)

def healthBarReductionSpieler(durchlaeufe, healthDiff):
    global currentLifeSpieler, healthbarSpielerColor

    reduceBalken = lambda: canvasSpielfeld.coords(healthbarSpielerColor, 700 - durchlaeufe*2, 400, 500, 380)
    canvasSpielfeld.after(durchlaeufe * 40, reduceBalken)


    currentKPIndex = currentLifeSpieler*100 - durchlaeufe
    changeKPIndex = lambda: canvasSpielfeld.itemconfigure(currentKP, text=str(currentKPIndex) +"/ 100")
    canvasSpielfeld.after(durchlaeufe * 40, changeKPIndex)

    healthColor = "green" if currentKPIndex >= 80 else "orange" if currentKPIndex < 80 and currentKPIndex >= 50 else "yellow" if currentKPIndex < 50 and currentKPIndex >= 20 else "red"
    #print(healthColor, currentKPIndex)
    if currentKPIndex < 79:
        changeColor = lambda: canvasSpielfeld.itemconfigure(healthbarSpielerColor, fill=healthColor)
        canvasSpielfeld.after(durchlaeufe * 40, changeColor)

    if durchlaeufe < healthDiff:
        durchlaeufe += 1
        healthBarReductionSpieler(durchlaeufe, healthDiff)


def healthBarReductionProjekt(durchlaeufe, healthDiff):

    currentKPIndex = currentLifeProjekt*100 - durchlaeufe
    reduceBalken = lambda: canvasSpielfeld.coords(healthbarProjektColor, 123, 100, 323- durchlaeufe*2, 120)
    canvasSpielfeld.after(durchlaeufe * 40, reduceBalken)

    healthColor = "green" if currentKPIndex >= 80 else "orange" if currentKPIndex < 80 and currentKPIndex >= 50 else "yellow" if currentKPIndex < 50 and currentKPIndex >= 20 else "red"
    
    if currentKPIndex < 79:
        changeColor = lambda: canvasSpielfeld.itemconfigure(healthbarProjektColor, fill=healthColor)
        canvasSpielfeld.after(durchlaeufe * 40, changeColor)

    if durchlaeufe < healthDiff:
        durchlaeufe += 1
        healthBarReductionProjekt(durchlaeufe, healthDiff)


def intro():
    global introText, canvasTextfeld, canvasSpielfeld

    introText = canvasTextfeld.create_text(10,5, width=750, anchor=NW, text="", font=("Press Start 2P", 35))

    intro1 = "Ein wildes PROJEKT ist aufgetaucht! "
    for x in range(len(intro1)):
        delay = 40*x
        text = intro1[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(introText, text=text)
        canvasTextfeld.after(delay, textUpdate)

    spielfeld.after(delay + 200, lambda: buttonErsteRunde())

def buttonErsteRunde():
    global button1

    button1 = Button(spielfeld, text="PRESS ENTER", highlightthickness=0, bd=0, bg="#fff", fg="#555",anchor=S, font=("Press Start 2P", 23), command=lambda: ersteRunde())
    canvasTextfeld.create_window(400, 270, window=button1)
    spielfeld.bind("<KeyPress-Return>", lambda b: ersteRunde())

def ersteRunde():
    global canvasTextfeld, button1, delayFrage

    canvasTextfeld.delete(introText)
    button1.destroy()
    spielfeld.after(100, menu())

def menu():
    global menuButton1, menuButton2, menuButton3, spielfeld, selectionMarker, selection, menuListMoves, menuListSpecial

    menuListMoves = Button(spielfeld, text="Moves", bg="#fff",
                         highlightthickness=0, bd=0, fg="#000",
                         font=("Press Start 2P", 30))
    canvasTextfeld.create_window(10, 0, window=menuListMoves, anchor=NW)

    menuListSpecial = Button(spielfeld, text="Spezial", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555",
                         font=("Press Start 2P", 30))
    canvasTextfeld.create_window(280, 0, window=menuListSpecial, anchor=NW)

    menuButton1 = Button(spielfeld, text="Power Nap", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555", anchor=W,
                         font=("Press Start 2P", 20))
    canvasTextfeld.create_window(100, 100, window=menuButton1, anchor=W)

    menuButton2 = Button(spielfeld, text="Energy Booster", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555", anchor=W,
                         font=("Press Start 2P", 20))
    canvasTextfeld.create_window(100, 170, window=menuButton2, anchor=W)

    menuButton3 = Button(spielfeld,
                         text="Kaffee Booster", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555", anchor=W,
                         font=("Press Start 2P", 20))
    canvasTextfeld.create_window(100, 240, window=menuButton3, anchor=W)

    menuNavigation()

def menuNavigation():

    # Überprüfe des System-Inputs auf die Pfeiltasten und ENTER-Taste. Bei Pfeiltasten wird das Highlighting in der Funktion "menuHighlight" angepasst. Bei Enter wird die aktuelle Auswahl ausgeführt.
    spielfeld.bind("<KeyPress-Down>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Up>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Right>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Left>", lambda b: menuHighlight(b))
    spielfeld.bind("<KeyPress-Return>", lambda b: lifeAnimation(0.1,0.5))

def menuHighlight(keystroke):

    global menuSelectionUpDown, menuSelectionLeftRight, selection

    if keystroke.keysym =="Right" or keystroke == "Right":
        menuSelectionUpDown = 0
        if menuSelectionLeftRight == 0:
            menuSelectionLeftRight += 1
    elif keystroke.keysym =="Left":
        menuSelectionUpDown = 0
        if menuSelectionLeftRight == 1:
            menuSelectionLeftRight -= 1

    if menuSelectionLeftRight < 1:
        menuListMoves.configure(fg="#000")
        menuListSpecial.configure(fg="#555")
        menuButton1.configure(text="Power Nap")
        menuButton2.configure(text="Energy Booster")
        menuButton3.configure(text="Kaffee Booster")
    elif menuSelectionLeftRight == 1:
        menuListMoves.configure(fg="#555")
        menuListSpecial.configure(fg="#000")
        menuButton1.configure(text="Gruppenarbeit")
        menuButton2.configure(text="Nachtschicht")
        menuButton3.configure(text="Keine Idee mehr")


    selection = PhotoImage(file="Assets/Images/selection.png")

    if keystroke.keysym == "Down":
        if menuSelectionUpDown < 3:
            menuSelectionUpDown += 1
    elif keystroke.keysym == "Up":
        if menuSelectionUpDown > 1:
            menuSelectionUpDown -= 1

    if menuSelectionUpDown == 1:
        selectionMarker = canvasTextfeld.create_image(95, 97, anchor=E, image=selection)
        menuButton1.configure(fg="black", font=("Press Start 2P",25))
        menuButton2.configure(fg="#555",font=("Press Start 2P",20))
        menuButton3.configure(fg="#555",font=("Press Start 2P",20))
    elif menuSelectionUpDown == 2:
        selectionMarker = canvasTextfeld.create_image(95, 167, anchor=E, image=selection)
        menuButton2.configure(fg="black", font=("Press Start 2P",25))
        menuButton1.configure(fg="#555",font=("Press Start 2P",20))
        menuButton3.configure(fg="#555",font=("Press Start 2P",20))
    elif menuSelectionUpDown == 3:
        selectionMarker = canvasTextfeld.create_image(95, 237, anchor=E, image=selection)
        menuButton3.configure(fg="black",font=("Press Start 2P",25))
        menuButton2.configure(fg="#555",font=("Press Start 2P",20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
    elif menuSelectionUpDown == 0:
        menuButton3.configure(fg="#555",font=("Press Start 2P",20))
        menuButton2.configure(fg="#555",font=("Press Start 2P",20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))

def action():
    print("test")

#Erstellen des Tkinter Fensters. Hintergrund wird auf dunkel grau gesetzt
spielfeld = Tk()
spielfeld.title("Pokemon in gut")
spielfeld.geometry("800x800")
spielfeld.configure(bg="#555")


menuSelectionUpDown = 0
menuSelectionLeftRight = 0

nameSpieler = "GRUPPE"

setup()

spielfeld.mainloop()