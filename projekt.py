from tkinter import *
import random


def setupWindow():
    global canvasSpielfeld, canvasTextfeld
    canvasSpielfeld = Canvas(spielfeld, height=500, width=800)
    canvasSpielfeld.configure(bg="#fff")
    canvasSpielfeld.pack()

    canvasTextfeld = Canvas(spielfeld, height=300, width=800)
    canvasTextfeld.configure(bg="#fff")
    canvasTextfeld.pack()

    introStory(1)

def introStory(round):
    global picture

    canvasTextfeld.delete("intro")

    introText = canvasTextfeld.create_text(400, 10, width=780, anchor=N, text="", font=("Press Start 2P", 17), tags="intro")

    if round == 1:
        picture = PhotoImage(file="Assets/Images/001_Sternenhimmel.png")
        intro = "Vor sehr langer Zeit… sehr sehr langer Zeit… mindestens drei Wochen her… beginnt unsere Geschichte. "
    if round == 2:
        picture = PhotoImage(file="Assets/Images/002_Schule.png")
        intro = "Es war ein normaler Tag, an einer normalen Schule, in einem alles andere als normalen Jahr. Doch die Schmorona-Pandemie änderte alles."
    if round == 3:
        picture = PhotoImage(file="Assets/Images/003_Schule_Apokalypse.png")
        intro = 'Ok vielleicht nicht so drastisch. Aber Klausuren fanden nicht statt und Lehrer forderten "Ersatzleistungen". Und darüber handelt auch unsere Geschichte. Doch warum seht ihr nicht einfach selbst!'
    if round == 4:
        picture = PhotoImage(file="Assets/Images/coronavirus.png")
        intro = "Schaut wie naiv und unschuldig noch alle sind! Das wird sich sogleich ändern."
    if round == 5:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        intro = "So liebe Klasse! Da wir aufgrund der Schmorona-Pandemie keine Klausuren und auch keinen Unterricht halten konnten, werdet ihr ein Gruppenprojekt machen müssen. Dieses Projekt ist gleich eure Endnote, also verhaut es nicht. Findet eine Gruppe und los geht's!"
    
    canvasSpielfeld.create_image(400, 250, anchor= CENTER, image=picture)

    for x in range(len(intro)+1):
        delay = 40 * x
        text = intro[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(introText, text=text)
        canvasTextfeld.after(delay, textUpdate)
    round += 1
    buttonNextIntro(round)


def buttonNextIntro(round):
    global button1

    button1 = Button(spielfeld, text="PRESS ENTER", highlightthickness=0, bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 15))
    canvasTextfeld.create_window(400, 280, window=button1)
    spielfeld.bind("<KeyPress-Return>", lambda b: introStory(round))
    if round == 6:
        spielfeld.bind("<KeyPress-Return>", lambda b: setup())


def setup():
    global playerFigurAnzeige, playerFigur, projectFigurAnzeige, projectFigur, whiteBackground

    canvasSpielfeld.delete("all")
    canvasTextfeld.delete("all")
    spielfeld.unbind("<KeyPress-Return>")

    whiteBackground = PhotoImage(file="Assets/Images/White.png")
    whiteBackgroundPlayer = canvasSpielfeld.create_image(20, 330, anchor=W,image=whiteBackground, tag="whitePl")
    whiteBackgroundProject = canvasSpielfeld.create_image(780, 150, anchor=E,image=whiteBackground, tag="whitePr")

    playerFigur = PhotoImage(file="Assets/Images/Gruppe.png")
    playerFigurAnzeige = canvasSpielfeld.create_image(800, 330, anchor=W, image=playerFigur)

    projectFigur = PhotoImage(file="Assets/Images/coronavirus.png")
    projectFigurAnzeige = canvasSpielfeld.create_image(0, 150, anchor=E, image=projectFigur)

    figurenMove(800, 0)


def figurenMove(frames, durchlaeufe):
    global playerFigurAnzeige, projectFigurAnzeige

    moveplayerFigur = lambda: canvasSpielfeld.move(playerFigurAnzeige, -5, 0)
    canvasSpielfeld.after(durchlaeufe * 10, moveplayerFigur)

    moveprojectFigur = lambda: canvasSpielfeld.move(projectFigurAnzeige, +5, 0)
    canvasSpielfeld.after(durchlaeufe * 10, moveprojectFigur)

    frames -= 5

    if frames == 20:
        canvasSpielfeld.after(1700, lambda: introFight())
        canvasSpielfeld.after(1700, lambda: spielfeldGraphik())

    else:
        durchlaeufe += 1
        figurenMove(frames, durchlaeufe)


def spielfeldGraphik():
    global currentKPIndex, playerArrow, projectArrow, healthbarPlayerColor, healthbarProjectColor, healthbarProjectWhite

    playerName = canvasSpielfeld.create_text(123, 90, text="PROJEKT", anchor=SW, font=("Press Start 2P", 18), tags="project")
    projectName = canvasSpielfeld.create_text(500, 370, text="Gruppe", anchor=SW, font=("Press Start 2P", 18), tags="player")

    playerArrow = PhotoImage(file="Assets/Images/arrowSpieler.png")
    playerHealthBarArrow = canvasSpielfeld.create_image(410, 410, anchor=W, image=playerArrow, tags="player")

    projectArrow = PhotoImage(file="Assets/Images/arrowProjekt.png")
    projectHealthBarArrow = canvasSpielfeld.create_image(45, 120, anchor=W, image=projectArrow, tags="project")

    healthbarProjectWhite = canvasSpielfeld.create_rectangle(123, 100, 323, 120, fill="white", tags="project")
    healthbarProjectColor = canvasSpielfeld.create_rectangle(123, 100, 323, 120, fill="green", tags="project")

    healthbarPlayerWhite = canvasSpielfeld.create_rectangle(700, 400, 500, 380, fill="white", tags="player")
    healthbarPlayerColor = canvasSpielfeld.create_rectangle(700, 400, 500, 380, fill="green", tags="player")

    kraftpunkte = canvasSpielfeld.create_text(477, 392, text="KP:", font=("Press Start 2P", 15), tags="player")
    kraftpunkte = canvasSpielfeld.create_text(100, 112, text="KP:", font=("Press Start 2P", 15), tags="project")

    currentKPIndex = canvasSpielfeld.create_text(700, 425, text="100/ 100", anchor=E, font=("Press Start 2P", 18), tags="player")


def introFight():
    global canvasTextfeld, canvasSpielfeld

    introFight = canvasTextfeld.create_text(400, 10, width=750, anchor=N, text="", font=("Press Start 2P", 35), tags="intro")
    intro = "Ein wildes PROJEKT ist aufgetaucht! "
    for x in range(len(intro)):
        delay = 40 * x
        text = intro[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(introFight, text=text)
        canvasTextfeld.after(delay, textUpdate)

    spielfeld.after(delay + 200, lambda: buttonErsteRunde())


def buttonErsteRunde():
    global button1

    button1 = Button(spielfeld, text="PRESS ENTER", highlightthickness=0, bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 23))
    canvasTextfeld.create_window(400, 270, window=button1)
    spielfeld.bind("<KeyPress-Return>", lambda b: ersteRunde())


def ersteRunde():
    global canvasTextfeld, button1, delayFrage

    canvasTextfeld.delete("intro")
    button1.destroy()
    spielfeld.after(100, menu())


def menu():
    global menuButton1, menuButton2, menuButton3, spielfeld, selectionMarker, selection, menuListMoves, menuListSpecial

    menuListMoves = Button(spielfeld, text="Moves", bg="#fff",
                           highlightthickness=0, bd=0, fg="#000",
                           font=("Press Start 2P", 30))
    canvasTextfeld.create_window(10, 0, window=menuListMoves, anchor=NW, tags="menu")

    menuListSpecial = Button(spielfeld, text="Spezial", bg="#fff",
                             highlightthickness=0, bd=0, fg="#555",
                             font=("Press Start 2P", 30))
    canvasTextfeld.create_window(280, 0, window=menuListSpecial, anchor=NW, tags="menu")

    menuButton1 = Button(spielfeld, text="Power Nap", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555", anchor=W,
                         font=("Press Start 2P", 20))
    canvasTextfeld.create_window(100, 100, window=menuButton1, anchor=W, tags="menu")

    menuButton2 = Button(spielfeld, text="Energy Booster", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555", anchor=W,
                         font=("Press Start 2P", 20))
    canvasTextfeld.create_window(100, 170, window=menuButton2, anchor=W, tags="menu")

    menuButton3 = Button(spielfeld,
                         text="Kaffee Booster", bg="#fff",
                         highlightthickness=0, bd=0, fg="#555", anchor=W,
                         font=("Press Start 2P", 20))
    canvasTextfeld.create_window(100, 240, window=menuButton3, anchor=W, tags="menu")

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
        selectionMarker = canvasTextfeld.create_image(95, 97, anchor=E, image=selection, tags="menu")
        menuButton1.configure(fg="black", font=("Press Start 2P", 25))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0,1))
        else:
            spielfeld.bind("<KeyPress-Return>", lambda b: action4())
    elif menuSelectionUpDown == 2:
        selectionMarker = canvasTextfeld.create_image(95, 167, anchor=E, image=selection, tags="menu")
        menuButton2.configure(fg="black", font=("Press Start 2P", 25))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(1,0))
        else:
            spielfeld.bind("<KeyPress-Return>", lambda b: action5())
    elif menuSelectionUpDown == 3:
        selectionMarker = canvasTextfeld.create_image(95, 237, anchor=E, image=selection,tags="menu")
        menuButton3.configure(fg="black", font=("Press Start 2P", 25))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            spielfeld.bind("<KeyPress-Return>", lambda b: action3())
        else:
            spielfeld.bind("<KeyPress-Return>", lambda b: action6())
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

    currentKP = round(currentLifePlayer * 100 - durchlaeufe)

    reduceBalken = lambda: canvasSpielfeld.coords(healthbarPlayerColor, 500+ currentKP * 2, 400, 500, 380)
    canvasSpielfeld.after(durchlaeufe * 40, reduceBalken)

    changeKPIndex = lambda: canvasSpielfeld.itemconfigure(currentKPIndex, text=str(currentKP) + "/ 100")
    canvasSpielfeld.after(durchlaeufe * 40, changeKPIndex)

    healthColor = "green" if currentKP >= 80 else "yellow" if currentKP < 80 and currentKP >= 50 else "orange" if currentKP < 50 and currentKP >= 20 else "red"

    changeColor = lambda: canvasSpielfeld.itemconfigure(healthbarPlayerColor, fill=healthColor)
    canvasSpielfeld.after(durchlaeufe * 40, changeColor)

    if durchlaeufe < healthReduction and currentKP > 0:
        durchlaeufe += 1
        healthBarReductionPlayer(durchlaeufe, healthReduction)
    elif currentKP > 0:
        currentLifePlayer -= dmgPlayer
    else:
        currentLifePlayer = 0
        canvasSpielfeld.after(durchlaeufe * 40, lambda: spielEnde("verloren"))

def healthBarReductionProject(durchlaeufe, healthReduction):
    global currentLifeProject

    currentKP = round(currentLifeProject * 100 - durchlaeufe)

    reduceBalken = lambda: canvasSpielfeld.coords(healthbarProjectColor, 123, 100, 123 + currentKP * 2, 120)
    canvasSpielfeld.after(durchlaeufe * 40, reduceBalken)

    healthColor = "green" if currentKP >= 80 else "yellow" if currentKP < 80 and currentKP >= 50 else "orange" if currentKP < 50 and currentKP >= 20 else "red"

    changeColor = lambda: canvasSpielfeld.itemconfigure(healthbarProjectColor, fill=healthColor)
    canvasSpielfeld.after(durchlaeufe * 40, changeColor)

    if durchlaeufe < healthReduction and currentKP > 0:
        durchlaeufe += 1
        healthBarReductionProject(durchlaeufe, healthReduction)
    elif currentKP > 0:
        currentLifeProject -= dmgProject
    else:
        currentLifeProject = 0
        canvasSpielfeld.after(durchlaeufe * 40, lambda: spielEnde("gewonnen"))

def spielEnde(ende):

    spielfeld.unbind("<KeyPress-Down>")
    spielfeld.unbind("<KeyPress-Up>")
    spielfeld.unbind("<KeyPress-Right>")
    spielfeld.unbind("<KeyPress-Left>")
    spielfeld.bind("<KeyPress-Return>", lambda b: test())

    if ende == "gewonnen":
        canvasSpielfeld.after(500, lambda: animationGewonnen(1, 300))
        canvasSpielfeld.after(1200, lambda: textfightEnde(ende))
    else:
        canvasSpielfeld.after(1000, lambda: animationVerloren(1, 350))
        canvasSpielfeld.after(1200, lambda: textfightEnde(ende))

def animationGewonnen(durchlaeufe, frames):

    canvasSpielfeld.delete("project")
    moveprojectFigur = lambda: canvasSpielfeld.move(projectFigurAnzeige, 0,-5)
    canvasSpielfeld.after(durchlaeufe * 10, moveprojectFigur)

    if frames > 0:
        durchlaeufe += 1
        animationGewonnen(durchlaeufe, frames - 5)

def textfightEnde(ende):

    canvasTextfeld.delete("menu")
    spielfeld.bind("<KeyPress-Return>", lambda b: outro())

    fightEnd = canvasTextfeld.create_text(400, 10, width=780, anchor=N, text="", font=("Press Start 2P", 30))
    if ende == "gewonnen":
        fightEndText = "Das Projekt wurde besiegt!"
    else:
        fightEndText = "Die Gruppe wurde besiegt!"


    for x in range(len(fightEndText)+1):
        delay = 40 * x
        text = fightEndText[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(fightEnd, text=text)
        canvasSpielfeld.after(delay, textUpdate)

    button1 = Button(spielfeld, text="PRESS ENTER", highlightthickness=0, bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 20))
    canvasTextfeld.create_window(400, 275, window=button1)


def animationVerloren(durchlaeufe, frames):

    canvasSpielfeld.delete("player")
    moveplayerFigur = lambda: canvasSpielfeld.move(playerFigurAnzeige, 0, +5)
    canvasSpielfeld.after(durchlaeufe * 10, moveplayerFigur)

    if frames > 0:
        durchlaeufe += 1
        animationVerloren(durchlaeufe, frames - 5)

def outro():
    global currentLifePlayer, picture

    canvasSpielfeld.delete("all")
    canvasTextfeld.delete("all")

    outroText = canvasTextfeld.create_text(400, 10, width=780, anchor=N, text="", font=("Press Start 2P", 17))

    if  currentLifePlayer > 0.8:
        picture = PhotoImage(file="Assets/Images/001_Sternenhimmel.png")
        outro = "War es ein Wunder? War es pures Können? Das alles spielte keine Rolle. Den Helden war es gelungen, was bis jetzt noch niemandem gelungen war. Sie hatten eine 1 für ihr Projekt bekommen. Der erste Schritt in eine steile Karriere."
    elif currentLifePlayer > 0.6:
        picture = PhotoImage(file="Assets/Images/002_Schule.png")
        outro = "Ach eine 2. Die vielleicht beste Note. Viele würden jetzt protestieren und sagen: Momentmal eine 1 ist doch viel besser. Doch ist sie das? Also faktisch ist sie natürlich besser! Aber wer will schon der Streber sein, der für eine Zahl so ackert. Nein die zwei ist perfekt!"
    elif currentLifePlayer > 0.4:
        picture = PhotoImage(file="Assets/Images/003_Schule_Apokalypse.png")
        outro = 'Die drei. Im anderen Kontext ist befriedigend das Ziel. Hier ist es zumindest keine Schande.'
    elif currentLifePlayer > 0.2:
        picture = PhotoImage(file="Assets/Images/coronavirus.png")
        outro = "Knapp getroffen gilt auch noch. Mit der Vier hat man es zwar gerade noch so geschafft, aber solange die Note hinter einem Kaffeefleck auf dem Zeugnis verschwindet passt das schon."
    elif currentLifePlayer > 0:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        outro = "Uh die 5. Das tut weh! Sich zu schämen ist hier wohl angebracht. Der einzige Wehrmutstropfen ist: Es geht noch schlimmer."
    else:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        outro ="Da könnte man ja glatt meinen die Helden hätten es gar nicht versucht. Wobei Helden in diesem Fall wohl nicht mehr angebracht ist. Nennen wir sie einfach Personen. Ja die Personen haben ins Klo gegriffen!"

    canvasSpielfeld.create_image(400, 250, anchor= CENTER, image=picture)

    for x in range(len(outro)+1):
        delay = 40 * x
        text = outro[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(outroText, text=text)
        canvasTextfeld.after(delay, textUpdate)

# Erstellen des Tkinter Fensters. Hintergrund wird auf dunkel grau gesetzt
spielfeld = Tk()
spielfeld.title("Pokemon in gut")
spielfeld.geometry("800x800")
spielfeld.configure(bg="#555")

menuSelectionUpDown = 0
menuSelectionLeftRight = 0
currentLifeProject = 1
currentLifePlayer = 1

setupWindow()

spielfeld.mainloop()