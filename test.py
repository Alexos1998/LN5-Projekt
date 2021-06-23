from tkinter import *

def setup():
    global canvasSpielfeld, canvasTextfeld, playerFigurAnzeige, playerFigur, projectFigurAnzeige, projectFigur, whiteBackground

    canvasSpielfeld = Canvas(spielfeld, height=500, width=800)
    canvasSpielfeld.configure(bg="#fff")
    canvasSpielfeld.pack()

    # Erstellen des Canvas, zur Darstellung von Spieltext und Buttons
    canvasTextfeld = Canvas(spielfeld, height=300, width=800)
    canvasTextfeld.configure(bg="#fff")
    canvasTextfeld.pack()


    whiteBackground = PhotoImage(file="Assets/Images/White.png")
    whiteBackgroundPlayer = canvasSpielfeld.create_image(20, 330, anchor=W,image=whiteBackground, tag="whitePl")
    whiteBackgroundProject = canvasSpielfeld.create_image(780, 150, anchor=E,image=whiteBackground, tag="whitePr")

    playerFigur = PhotoImage(file="Assets/Images/Gruppe.png")
    playerFigurAnzeige = canvasSpielfeld.create_image(800, 330, anchor=W, image=playerFigur)

    projectFigur = PhotoImage(file="Assets/Images/coronavirus.png")
    projectFigurAnzeige = canvasSpielfeld.create_image(0, 150, anchor=E, image=projectFigur)

    figurenMove(800, 0)


def figurenMove(frames, durchlaeufe):
    global playerFigurAnzeige, projectFigurAnzeige, currentKP, balken

    moveplayerFigur = lambda: canvasSpielfeld.move(playerFigurAnzeige, -5, 0)
    canvasSpielfeld.after(durchlaeufe * 10, moveplayerFigur)

    moveprojectFigur = lambda: canvasSpielfeld.move(projectFigurAnzeige, +5, 0)
    canvasSpielfeld.after(durchlaeufe * 10, moveprojectFigur)

    frames -= 5

    if frames == 20:
        canvasSpielfeld.after(1700, lambda: intro())
        canvasSpielfeld.after(1700, lambda: spielfeldGraphik())

    else:
        durchlaeufe += 1
        figurenMove(frames, durchlaeufe)


def spielfeldGraphik():
    global currentKPIndex, playerArrow, projectArrow, healthbarProjectWhite, healthbarProjectColor, healthbarPlayerWhite, healthbarPlayerColor, currentHealthBarPlayer

    playerName = canvasSpielfeld.create_text(123, 90, text="PROJEKT", anchor=SW, font=("Press Start 2P", 18))
    projectName = canvasSpielfeld.create_text(500, 370, text="Gruppe", anchor=SW, font=("Press Start 2P", 18))

    playerArrow = PhotoImage(file="Assets/Images/arrowSpieler.png")
    playerHealthBarArrow = canvasSpielfeld.create_image(410, 410, anchor=W, image=playerArrow)

    projectArrow = PhotoImage(file="Assets/Images/arrowProjekt.png")
    projectHealthBarArrow = canvasSpielfeld.create_image(45, 120, anchor=W, image=projectArrow)

    healthbarProjectWhite = canvasSpielfeld.create_rectangle(123, 100, 323, 120, fill="white")
    healthbarProjectColor = canvasSpielfeld.create_rectangle(123, 100, 323, 120, fill="green")

    healthbarPlayerWhite = canvasSpielfeld.create_rectangle(700, 400, 500, 380, fill="white")
    healthbarPlayerColor = canvasSpielfeld.create_rectangle(700, 400, 500, 380, fill="green")

    kpPlayer = canvasSpielfeld.create_text(477, 392, text="KP:", font=("Press Start 2P", 15), tags="KP")
    kpProject = canvasSpielfeld.create_text(100, 112, text="KP:", font=("Press Start 2P", 15), tags="KP")

    currentKPIndex = canvasSpielfeld.create_text(700, 425, text="100/ 100", anchor=E, font=("Press Start 2P", 18))


def intro():
    global introText, canvasTextfeld, canvasSpielfeld

    introText = canvasTextfeld.create_text(400, 10, width=750, anchor=N, text="", font=("Press Start 2P", 35))
    intro1 = "Ein wildes PROJEKT ist aufgetaucht! "
    for x in range(len(intro1)):
        delay = 40 * x
        text = intro1[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(introText, text=text)
        canvasTextfeld.after(delay, textUpdate)

    spielfeld.after(delay + 200, lambda: buttonErsteRunde())


def buttonErsteRunde():
    global button1

    button1 = Button(spielfeld, text="PRESS ENTER", highlightthickness=0, bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 23), command=lambda: ersteRunde())
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


def menuHighlight(keystroke):
    global menuSelectionUpDown, menuSelectionLeftRight, selection

    if keystroke.keysym == "Right" or keystroke == "Right":
        menuSelectionUpDown = 0
        if menuSelectionLeftRight == 0:
            menuSelectionLeftRight += 1
    elif keystroke.keysym == "Left":
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

    if keystroke.keysym == "Down":
        if menuSelectionUpDown < 3:
            menuSelectionUpDown += 1
    elif keystroke.keysym == "Up":
        if menuSelectionUpDown > 1:
            menuSelectionUpDown -= 1

    selection = PhotoImage(file="Assets/Images/selection.png")

    if menuSelectionUpDown == 1:
        selectionMarker = canvasTextfeld.create_image(95, 97, anchor=E, image=selection)
        menuButton1.configure(fg="black", font=("Press Start 2P", 25))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0.15,0))
        else:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0,0.15))
    elif menuSelectionUpDown == 2:
        selectionMarker = canvasTextfeld.create_image(95, 167, anchor=E, image=selection)
        menuButton2.configure(fg="black", font=("Press Start 2P", 25))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0.15,0.12))
        else:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0,0.12))
    elif menuSelectionUpDown == 3:
        selectionMarker = canvasTextfeld.create_image(95, 237, anchor=E, image=selection)
        menuButton3.configure(fg="black", font=("Press Start 2P", 25))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0,0))
        else:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0.2,0.2))
    elif menuSelectionUpDown == 0:
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        spielfeld.unbind("<KeyPress-Return>")


def healthDiffCalc(player, project):
    global healthbarProjectColor, healthbarPlayerColor, currentLifeProject, currentLifePlayer, dmgProject, dmgPlayer

    if player > 0:
        dmgAnimationPlayer(1)
        dmgPlayer = player
        healthReductionPlayer = int(round(player * 100))
        canvasSpielfeld.after(500, lambda: healthBarReductionPlayer(1, healthReductionPlayer))

    if project > 0:
        dmgAnimationProject(1)
        dmgProject = project
        healthReductionProject = int(round(project * 100))
        canvasSpielfeld.after(500, lambda: healthBarReductionProject(1, healthReductionProject))

def dmgAnimationPlayer(durchlaeufe):

    raiseWhite = lambda: canvasSpielfeld.tag_raise("whitePl")
    canvasSpielfeld.after(durchlaeufe * 70, raiseWhite)
    lowerWhite = lambda: canvasSpielfeld.tag_lower("whitePl")
    canvasSpielfeld.after(durchlaeufe * 100, lowerWhite)

    if durchlaeufe < 5:
        durchlaeufe += 1
        dmgAnimationPlayer(durchlaeufe)


def dmgAnimationProject(durchlaeufe):

    raiseWhite = lambda: canvasSpielfeld.tag_raise("whitePr")
    canvasSpielfeld.after(durchlaeufe * 70, raiseWhite)
    lowerWhite = lambda: canvasSpielfeld.tag_lower("whitePr")
    canvasSpielfeld.after(durchlaeufe * 100, lowerWhite)

    if durchlaeufe < 5:
        durchlaeufe += 1
        dmgAnimationProject(durchlaeufe)


def healthBarReductionPlayer(durchlaeufe, healthReduction):
    global currentLifePlayer

    currentHealthBarPlayer = currentLifePlayer * 200 + 500

    reduceBalken = lambda: canvasSpielfeld.coords(healthbarPlayerColor, currentHealthBarPlayer - durchlaeufe * 2, 400, 500, 380)
    canvasSpielfeld.after(durchlaeufe * 40, reduceBalken)

    currentKP = round(currentLifePlayer * 100 - durchlaeufe)
    changeKPIndex = lambda: canvasSpielfeld.itemconfigure(currentKPIndex, text=str(currentKP) + "/ 100")
    canvasSpielfeld.after(durchlaeufe * 40, changeKPIndex)

    healthColor = "green" if currentKP >= 80 else "yellow" if currentKP < 80 and currentKP >= 50 else "orange" if currentKP < 50 and currentKP >= 20 else "red"

    changeColor = lambda: canvasSpielfeld.itemconfigure(healthbarPlayerColor, fill=healthColor)
    canvasSpielfeld.after(durchlaeufe * 40, changeColor)

    if durchlaeufe < healthReduction:
        durchlaeufe += 1
        healthBarReductionPlayer(durchlaeufe, healthReduction)
    else:
        currentLifePlayer -= dmgPlayer


def healthBarReductionProject(durchlaeufe, healthReduction):
    global currentLifeProject

    currentHealthBarProject = currentLifeProject * 200 + 123

    currentKP = currentLifeProject * 100 - durchlaeufe

    reduceBalken = lambda: canvasSpielfeld.coords(healthbarProjectColor, 123, 100, currentHealthBarProject - durchlaeufe * 2, 120)
    canvasSpielfeld.after(durchlaeufe * 40, reduceBalken)

    healthColor = "green" if currentKP >= 80 else "yellow" if currentKP < 80 and currentKP >= 50 else "orange" if currentKP < 50 and currentKP >= 20 else "red"
    changeColor = lambda: canvasSpielfeld.itemconfigure(healthbarProjectColor, fill=healthColor)
    canvasSpielfeld.after(durchlaeufe * 40, changeColor)

    if durchlaeufe < healthReduction:
        durchlaeufe += 1
        healthBarReductionProject(durchlaeufe, healthReduction)
    else:
        currentLifeProject -= dmgProject


# Erstellen des Tkinter Fensters. Hintergrund wird auf dunkel grau gesetzt
spielfeld = Tk()
spielfeld.title("Pokemon in gut")
spielfeld.geometry("800x800")
spielfeld.configure(bg="#555")

menuSelectionUpDown = 0
menuSelectionLeftRight = 0
currentLifeProject = 1
currentLifePlayer = 1

setup()

spielfeld.mainloop()