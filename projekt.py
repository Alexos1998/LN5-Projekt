from tkinter import *
import random


def setupWindow():
    # Variablen werden global definiert, damit sie auch außerhalb der lokalen Funktion geladen werden können
    global canvasGrafiken, canvasTextfeld

    # Erstellen von 2 Canvas Objekten, in denen später Grafiken und Texte dargestellt werden
    # Tkinter Objekte werden nach dem Schema (tkinter-Fenster, Optionen) erstellt
    canvasGrafiken = Canvas(spielfeld, height=500, width=800)
    canvasGrafiken.configure(bg="#fff")
    # Mit .pack() werden Objekte zentriert untereinander im Fenster geladen
    canvasGrafiken.pack()

    canvasTextfeld = Canvas(spielfeld, height=300, width=800)
    canvasTextfeld.configure(bg="#fff")
    canvasTextfeld.pack()

    setup()

def setup():
    global playerFigurAnzeige, playerFigur, projectFigurAnzeige, projectFigur, whiteBackground

    # Alle Objekte werden von beiden Canvas-Fenstern gelöscht und Funktion der Entertaste wird gelöst
    canvasGrafiken.delete("all")
    canvasTextfeld.delete("all")
    spielfeld.unbind("<KeyPress-Return>")

    # Mehrere Bildobjekte werden geladen und mit create_image angezeigt.
    whiteBackground = PhotoImage(file="Assets/Images/White.png")
    whiteBackgroundPlayer = canvasGrafiken.create_image(20, 330, anchor=W, image=whiteBackground, tag="whitePl")
    whiteBackgroundProject = canvasGrafiken.create_image(780, 150, anchor=E, image=whiteBackground, tag="whitePr")

    playerFigur = PhotoImage(file="Assets/Images/Gruppe.png")
    playerFigurAnzeige = canvasGrafiken.create_image(800, 330, anchor=W, image=playerFigur)

    projectFigur = PhotoImage(file="Assets/Images/coronavirus.png")
    projectFigurAnzeige = canvasGrafiken.create_image(0, 150, anchor=E, image=projectFigur)

    # Aufrufen der Funktion figurenMove mit Übergabeparameter "800", welcher die Koordinaten der x-Achse repräsentiert und
    # "0" welcher als Counter benutzt wird
    figurenMove(800, 0)


def figurenMove(coordinates, durchlaeufe):
    global playerFigurAnzeige, projectFigurAnzeige

    # Mit der Methode .move werden die Grafiken bei jedem Durchlauf um x,y Koordinaten verschoben.
    # lambda verhindert, dass die Aktion direkt ausgeführt wird und später mit .after mit einem delay aufgerufen
    # werden kann.
    moveplayerFigur = lambda: canvasGrafiken.move(playerFigurAnzeige, -5, 0)
    canvasGrafiken.after(durchlaeufe * 10, moveplayerFigur)

    moveprojectFigur = lambda: canvasGrafiken.move(projectFigurAnzeige, +5, 0)
    canvasGrafiken.after(durchlaeufe * 10, moveprojectFigur)

    coordinates -= 5

    if coordinates == 20:
        canvasGrafiken.after(1700, lambda: introFight())
        canvasGrafiken.after(1700, lambda: spielfeldGraphik())

    else:
        durchlaeufe += 1
        figurenMove(coordinates, durchlaeufe)


def spielfeldGraphik():
    global currentKPIndex, playerArrow, projectArrow, healthbarPlayerColor, healthbarProjectColor, healthbarProjectWhite

    playerName = canvasGrafiken.create_text(123, 90, text="PROJEKT", anchor=SW, font=("Press Start 2P", 18),
                                            tags="project")
    projectName = canvasGrafiken.create_text(500, 370, text="GRUPPE", anchor=SW, font=("Press Start 2P", 18),
                                             tags="player")

    playerArrow = PhotoImage(file="Assets/Images/arrowSpieler.png")
    playerHealthBarArrow = canvasGrafiken.create_image(410, 410, anchor=W, image=playerArrow, tags="player")

    projectArrow = PhotoImage(file="Assets/Images/arrowProjekt.png")
    projectHealthBarArrow = canvasGrafiken.create_image(45, 120, anchor=W, image=projectArrow, tags="project")

    healthbarProjectWhite = canvasGrafiken.create_rectangle(123, 100, 323, 120, fill="white", tags="project")
    healthbarProjectColor = canvasGrafiken.create_rectangle(123, 100, 323, 120, fill="green", tags="project")

    healthbarPlayerWhite = canvasGrafiken.create_rectangle(700, 400, 500, 380, fill="white", tags="player")
    healthbarPlayerColor = canvasGrafiken.create_rectangle(700, 400, 500, 380, fill="green", tags="player")

    kraftpunkte = canvasGrafiken.create_text(477, 392, text="KP:", font=("Press Start 2P", 15), tags="player")
    kraftpunkte = canvasGrafiken.create_text(100, 112, text="KP:", font=("Press Start 2P", 15), tags="project")

    currentKPIndex = canvasGrafiken.create_text(700, 425, text="100/ 100", anchor=E, font=("Press Start 2P", 18),
                                                tags="player")


def introFight():
    global canvasTextfeld, canvasGrafiken

    introFight = canvasTextfeld.create_text(400, 10, width=750, anchor=N, text="", font=("Press Start 2P", 35),
                                            tags="intro")
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
    spielfeld.unbind("<KeyPress-Return>")

    turnRandomText = canvasTextfeld.create_text(400, 50, width=790, anchor=N, text="", font=("Press Start 2P", 28))

    textRandom = "abcdefghijklmnopqrstuvwxyz0123456789öäüÖÄÜABCDEFGHIJKLMOPQRSTUVWXYZ"
    gruppeStart = "Die Gruppe fängt an!"
    projektStart = "Das Projekt fängt an!"

    randomizer = random.randint(0, 0)
    if randomizer == 0:
        roundStart = gruppeStart
        spielfeld.bind("<KeyPress-Return>", lambda b: menu())
    else:
        roundStart = projektStart
        spielfeld.bind("<KeyPress-Return>", lambda b: projectAction())

    index = 0
    for x in range(37):

        if x < 15:
            delay = 90 * x
            text = ''.join(random.sample(textRandom, 19))
        elif x <= 15+len(roundStart):
            delay = 500 + 60 * x
            textEnd = ''.join(random.sample(textRandom, 19))
            text = roundStart[:index] + textEnd[index:]
            index += 1
        updateText = lambda t=text: canvasTextfeld.itemconfigure(turnRandomText, text=t)
        canvasTextfeld.after(delay, updateText)

    button1 = Button(spielfeld, text="PRESS ENTER", highlightthickness=0, bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 23))
    canvasTextfeld.create_window(400, 270, window=button1)


def menu():
    global menuButton1, menuButton2, menuButton3, spielfeld, selectionMarker, selection, menuListMoves, menuListSpecial

    canvasTextfeld.delete("all")

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
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0, 1))
        else:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0, 0.5))
    elif menuSelectionUpDown == 2:
        selectionMarker = canvasTextfeld.create_image(95, 167, anchor=E, image=selection, tags="menu")
        menuButton2.configure(fg="black", font=("Press Start 2P", 25))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(1, 0))
        else:
            spielfeld.bind("<KeyPress-Return>", lambda b: action5())
    elif menuSelectionUpDown == 3:
        selectionMarker = canvasTextfeld.create_image(95, 237, anchor=E, image=selection, tags="menu")
        menuButton3.configure(fg="black", font=("Press Start 2P", 25))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            spielfeld.bind("<KeyPress-Return>", lambda b: healthDiffCalc(0.2, 0))
        else:
            spielfeld.bind("<KeyPress-Return>", lambda b: action6())
    elif menuSelectionUpDown == 0:
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        spielfeld.unbind("<KeyPress-Return>")


def projectAction():
    text="hier passiert noch gar nichts"
    print(text)

def actionText(entity, text):
    print("nichts")


def healthDiffCalc(player, project):
    global healthbarProjectColor, healthbarPlayerColor, currentLifeProject, currentLifePlayer, dmgProject, dmgPlayer

    if player > 0:
        dmgAnimationPlayer(1)
        dmgPlayer = player
        healthReductionPlayer = int(round(player * 100))
        canvasGrafiken.after(500, lambda: healthBarReductionPlayer(1, healthReductionPlayer))

    if project > 0:
        dmgAnimationProject(1)
        dmgProject = project
        healthReductionProject = int(round(project * 100))
        canvasGrafiken.after(500, lambda: healthBarReductionProject(1, healthReductionProject))


def dmgAnimationPlayer(durchlaeufe):
    raiseWhite = lambda: canvasGrafiken.tag_raise("whitePl")
    canvasGrafiken.after(durchlaeufe * 70, raiseWhite)
    lowerWhite = lambda: canvasGrafiken.tag_lower("whitePl")
    canvasGrafiken.after(durchlaeufe * 100, lowerWhite)

    if durchlaeufe < 5:
        durchlaeufe += 1
        dmgAnimationPlayer(durchlaeufe)


def dmgAnimationProject(durchlaeufe):
    raiseWhite = lambda: canvasGrafiken.tag_raise("whitePr")
    canvasGrafiken.after(durchlaeufe * 70, raiseWhite)
    lowerWhite = lambda: canvasGrafiken.tag_lower("whitePr")
    canvasGrafiken.after(durchlaeufe * 100, lowerWhite)

    if durchlaeufe < 5:
        durchlaeufe += 1
        dmgAnimationProject(durchlaeufe)


def healthBarReductionPlayer(durchlaeufe, healthReduction):
    global currentLifePlayer

    currentKP = round(currentLifePlayer * 100 - durchlaeufe)

    reduceBalken = lambda: canvasGrafiken.coords(healthbarPlayerColor, 500 + currentKP * 2, 400, 500, 380)
    canvasGrafiken.after(durchlaeufe * 40, reduceBalken)

    changeKPIndex = lambda: canvasGrafiken.itemconfigure(currentKPIndex, text=str(currentKP) + "/ 100")
    canvasGrafiken.after(durchlaeufe * 40, changeKPIndex)

    healthColor = "green" if currentKP > 80 else "#0C0" if currentKP > 60 else "yellow" if currentKP > 40 else "orange" if currentKP > 20 else "red"

    changeColor = lambda: canvasGrafiken.itemconfigure(healthbarPlayerColor, fill=healthColor)
    canvasGrafiken.after(durchlaeufe * 40, changeColor)

    if durchlaeufe < healthReduction and currentKP > 0:
        durchlaeufe += 1
        healthBarReductionPlayer(durchlaeufe, healthReduction)
    elif currentKP > 0:
        currentLifePlayer -= dmgPlayer
    else:
        currentLifePlayer = 0
        canvasGrafiken.after(durchlaeufe * 40, lambda: spielEnde("verloren"))


def healthBarReductionProject(durchlaeufe, healthReduction):
    global currentLifeProject

    currentKP = round(currentLifeProject * 100 - durchlaeufe)

    reduceBalken = lambda: canvasGrafiken.coords(healthbarProjectColor, 123, 100, 123 + currentKP * 2, 120)
    canvasGrafiken.after(durchlaeufe * 40, reduceBalken)

    healthColor = "green" if currentKP > 80 else "#0C0" if currentKP > 60 else "yellow" if currentKP > 40 else "orange" if currentKP > 20 else "red"

    changeColor = lambda: canvasGrafiken.itemconfigure(healthbarProjectColor, fill=healthColor)
    canvasGrafiken.after(durchlaeufe * 40, changeColor)

    if durchlaeufe < healthReduction and currentKP > 0:
        durchlaeufe += 1
        healthBarReductionProject(durchlaeufe, healthReduction)
    elif currentKP > 0:
        currentLifeProject -= dmgProject
    else:
        currentLifeProject = 0
        canvasGrafiken.after(durchlaeufe * 40, lambda: spielEnde("gewonnen"))


def spielEnde(ende):
    spielfeld.unbind("<KeyPress-Down>")
    spielfeld.unbind("<KeyPress-Up>")
    spielfeld.unbind("<KeyPress-Right>")
    spielfeld.unbind("<KeyPress-Left>")
    spielfeld.unbind("<KeyPress-Return>")

    if ende == "gewonnen":
        canvasGrafiken.after(500, lambda: animationGewonnen(1, 300))
        canvasGrafiken.after(1200, lambda: textfightEnde(ende))
    else:
        canvasGrafiken.after(1000, lambda: animationVerloren(1, 350))
        canvasGrafiken.after(1200, lambda: textfightEnde(ende))


def animationGewonnen(durchlaeufe, coordinates):
    canvasGrafiken.delete("project")
    moveprojectFigur = lambda: canvasGrafiken.move(projectFigurAnzeige, 0, -5)
    canvasGrafiken.after(durchlaeufe * 10, moveprojectFigur)

    if coordinates > 0:
        durchlaeufe += 1
        animationGewonnen(durchlaeufe, coordinates - 5)


def animationVerloren(durchlaeufe, coordinates):
    canvasGrafiken.delete("player")
    moveplayerFigur = lambda: canvasGrafiken.move(playerFigurAnzeige, 0, +5)
    canvasGrafiken.after(durchlaeufe * 10, moveplayerFigur)

    if coordinates > 0:
        durchlaeufe += 1
        animationVerloren(durchlaeufe, coordinates - 5)


def textfightEnde(ende):
    canvasTextfeld.delete("menu")
    spielfeld.bind("<KeyPress-Return>", lambda b: outro())

    fightEnd = canvasTextfeld.create_text(400, 10, width=780, anchor=N, text="", font=("Press Start 2P", 30))
    if ende == "gewonnen":
        fightEndText = "Das Projekt wurde besiegt!"
    else:
        fightEndText = "Die Gruppe wurde besiegt!"

    for x in range(len(fightEndText) + 1):
        delay = 40 * x
        text = fightEndText[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(fightEnd, text=text)
        canvasGrafiken.after(delay, textUpdate)

    button1 = Button(spielfeld, text="PRESS ENTER", highlightthickness=0, bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 20))
    canvasTextfeld.create_window(400, 275, window=button1)


def outro():
    global picture

    canvasGrafiken.delete("all")
    canvasTextfeld.delete("all")
    spielfeld.unbind("<KeyPress-Return>")

    outroText = canvasTextfeld.create_text(400, 10, width=780, anchor=N, text="", font=("Press Start 2P", 17))
    lifeLeft = round(currentLifePlayer,2)

    if lifeLeft > 0.8:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        outro = "War es ein Wunder? War es pures Können? Das alles spielte keine Rolle. Den Helden war es gelungen, was bis jetzt noch niemandem gelungen war. Sie hatten eine 1 für ihr Projekt bekommen. Der erste Schritt in eine steile Karriere."
    elif lifeLeft > 0.6:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        outro = "Ach eine 2. Die vielleicht beste Note. Viele würden jetzt protestieren und sagen: „Momentmal eine 1 ist doch viel besser. Doch ist sie das? Also faktisch ist sie natürlich besser! Aber wer will schon der Streber sein, der für eine Zahl so ackert. Nein die zwei ist perfekt!“"
    elif lifeLeft > 0.4:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        outro = 'Eine 3. Im anderen Kontext ist befriedigend das Ziel. Hier ist es zumindest keine Schande.'
    elif lifeLeft > 0.2:
        picture = PhotoImage(file="Assets/Images/coronavirus.png")
        outro = "Knapp getroffen gilt auch noch. Mit der 4 hat man es zwar gerade noch so geschafft, aber solange die Note hinter einem Kaffeefleck auf dem Zeugnis verschwindet, passt das schon."
    elif lifeLeft > 0:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        outro = "Uff, eine 5. Das tut weh! Sich zu schämen ist hier wohl angebracht. Der einzige Wehrmutstropfen ist: Es geht noch schlimmer."
    else:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        outro = "Eine 6? Da könnte man ja glatt meinen die Helden hätten es gar nicht versucht. Wobei Helden in diesem Fall wohl nicht mehr angebracht ist. Nennen wir sie einfach Personen. Ja die Personen haben ins Klo gegriffen!"

    canvasGrafiken.create_image(400, 250, anchor=CENTER, image=picture)

    for x in range(len(outro) + 1):
        delay = 40 * x
        text = outro[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(outroText, text=text)
        canvasTextfeld.after(delay, textUpdate)


# Erstellen des Tkinter Fensters. Mit dem definieren der Variable spielfeld, als Funktion Tk(), wird ds Fenster initialisiert.
spielfeld = Tk()
# Über verschiedene Methoden können Tkinter Objekte angepasst werden.
# .title setzt einen Fenster-Namen fest.
spielfeld.title("Pokemon in gut")
# .geometry setzt die Größe in x*y coordinatesn fest
spielfeld.geometry("800x800")
# .configure bearbeitet Eigenschaften eines Tkinter Objekts. Mit bg, wird der Background auf einen Hexcode gesetzt
spielfeld.configure(bg="#555")

# Definieren einiger globaler variablen die später benötigt werden
# menuSelection wird für die Auswahl im Kampfmenü verwendet
menuSelectionUpDown = 0
menuSelectionLeftRight = 0
# currentLife sind die Prozentualen Leben der beiden Entitites
currentLifeProject = 1
currentLifePlayer = 1

# Aufrufe der ersten Funktion setupWindow()
setupWindow()

# .mainloop beendet den Loop in den Tkinter Funktionen und Methoden lesen und ausführen kann.
# Die Methode muss global definiert sein und darf nicht durch schleifen die den Main-Thread unterbrechen gestoppt werden.
spielfeld.mainloop()