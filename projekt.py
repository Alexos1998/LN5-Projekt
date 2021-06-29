from tkinter import *
import random


def setupWindow():
    # Variablen werden global definiert, damit sie auch außerhalb der lokalen Funktion geladen werden können
    global canvasGrafiken, canvasTextfeld

    # Erstellen von 2 Canvas Objekten, in denen später Grafiken und Texte dargestellt werden
    # Tkinter Objekte werden nach dem Schema (tkinter-Fenster, Optionen) erstellt
    canvasGrafiken = Canvas(tkinterFenster, height=500, width=800)
    canvasGrafiken.configure(bg="#fff")
    # Mit .pack() werden Objekte zentriert untereinander im Fenster geladen
    canvasGrafiken.pack()

    canvasTextfeld = Canvas(tkinterFenster, height=300, width=800)
    canvasTextfeld.configure(bg="#fff")
    canvasTextfeld.pack()

    # Der Funktion introStory wird mit 1 als Übergabeparameter aufgerufen. 
    # Der Parameter wird als Counter verwendet und zählt die Anzahl der Durchläufe der Funktion
    introStory(0)

def introStory(round):
    # Die Variable picture wird global gesetzt, da Bildelemente mit PhotoImage nur lokal geladen werden und der
    # Tkinter.mainloop die Dateien sonst nicht erkennt
    global picture, text

    # Mit .delete werden alle Elemente mit dem tag "intro" vom Canvas gelöscht. Dies ist eine Canvas eigene Methode
    canvasTextfeld.delete("intro")

    # Ein leerer String wird als Text im canvasTextfeld erstellt. Dem Textobjekt werden dabei die Position in x,y Koordinaten 
    # mitgegeben. Ebenfalls werden die Breite (width), Ausrichtung (anchor) und Schriftart (font), sowie größe festgelegt.
    introText = canvasTextfeld.create_text(400, 10, width=780, anchor=N, text="", font=("Press Start 2P", 17), tags="intro")

    # Basierend auf dem Parameter round wird ein Foto mit der Funktion PhotoImage geladen und ein Text wird der Variable
    # intro zugewiesen
    if round == 0:
        picture = PhotoImage(file="Assets/Images/000 Titelbild.png")
        intro = ""

    if round == 1:
        picture = PhotoImage(file="Assets/Images/001 Sternenhimmel.png")
        intro = "Vor sehr langer Zeit… sehr sehr langer Zeit… mindestens drei Wochen her… beginnt unsere Geschichte."

    if round == 2:
        picture = PhotoImage(file="Assets/Images/002 Schule.png")
        intro = 'Es war ein normaler Tag an einer normalen Schule an einem alles als normalen Jahr. Die Schmorona-Pandemie änderte alles.'

    if round == 3:
        picture = PhotoImage(file="Assets/Images/003 Schule Apokalypse.png")
        intro = "Ok vielleicht nicht so drastisch, aber ihr versteht den Punkt. Vieles änderte sich. Klausuren fanden nicht statt und Lehrer forderten „Ersatzleistungen“. Und darüber handelt auch unsere Geschichte. Doch warum seht ihr nicht einfach selbst!"

    if round == 4:
        picture = PhotoImage(file="Assets/Images/005 Klassenzimmer Voll.png")
        intro = "Schaut wie naiv und unschuldig noch alle sind! Das wird sich sogleich ändern."

    if round == 5:
        picture = PhotoImage(file="Assets/Images/007 Lehrer.png")
        intro = "„So Klasse! Ich habe mir etwas überlegt. Da wir aufgrund der Schmorona-Pandemie leider keine Klausuren und auch keinen Unterricht halten konnten, werdet ihr ein Gruppenprojekt machen müssen. Dieses Projekt ist gleich eure Endnote, also verhaut es nicht. Findet eine Gruppe und los geht’s!“"
    
    if round == 6:
        picture = PhotoImage(file="Assets/Images/005 Klassenzimmer Voll.png")
        intro = ""

    if round == 7:
        picture = PhotoImage(file="Assets/Images/006 Rauchwolke.png")
        intro = ""

    if round == 8:
        picture = PhotoImage(file="Assets/Images/004 Klassenzimmer Vier.png")
        intro = "Und so bahnte das Schicksal unseren Helden einen Weg. Doch den Kampf werden Sie selber führen müssen. Können Sie bestehen und ihre Note retten?"

    # Das geladene Bild wird mit der Methode create_image dargestellt und zentriert ausgerichtet. Zenter basiert auf den x,y-Koordinaten.
    canvasGrafiken.create_image(400, 250, anchor=CENTER, image=picture)

    # In einer Schleife wird dem leeren Text inkrementell der Inhalt von intro zugewiesen. Schleife wird n + 1 mal basierend auf der
    # länge des Strings ausgeführt
    for x in range(len(intro)+1):
        # Eine zeitliche Verzögerung mit 40mal dem Wert von x wird berechnet
        delay = 30 * x
        # Mit ":x" innerhalb eines Listenindexes werden die Werte bis zum Index "x" einbezogen und der Variable text zugewiesen
        text = intro[:x]
        # Der Variable wird die anonyme Funktion lambda zugewiesen. lambda wird der Übergabeparameter "t" mitgegeben, 
        # welcher mit text gleichgesetzt wird (t=text:),
        # nach dem ":" folgt dann der Inhalt der Funktion. Hier wird die Canvas-Methode .itemconfigure aufgerufen, um den text des Canvas Objekts anzupassen
        # Der Text ist dabei gleich dem Übergabeparameter "t", also dem vorher definierten text
        textUpdate = lambda t=text: canvasTextfeld.itemconfigure(introText, text=t)
        # Mit der Methode .after wird textUpdate, nach der Zeit "delay" in ms verzögert ausgeführt
        canvasTextfeld.after(delay, textUpdate)
    round += 1
    buttonNextIntro(round)


def buttonNextIntro(round):
    global button
    # Mit der Funktion Button, wird ein aktivierbarer Knopf erstellt, Option "bd=0" entfernt die Ränder vom Knopf
    button = Button(tkinterFenster, text="PRESS ENTER", bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 16))
    # Canvas-Methode .create_window erstellt ein Fenster bei x,y-Koordinaten und setzt lädt button im Fenster
    canvasTextfeld.create_window(400, 275, window=button)
    # Tkinter-Methode .bind weißt dem Tastendruck Enter, die Funktion "introStory" zu.
    tkinterFenster.bind("<KeyPress-Return>", lambda b: introStory(round))
    
    # Wenn round = 5 ist, wird der Tastendruck für Enter neu definiert und führt die Funktion setup aus
    if round == 9:
        tkinterFenster.bind("<KeyPress-Return>", lambda b: setup())


def setup():
    global playerFigurAnzeige, playerFigur, projectFigurAnzeige, projectFigur, whiteBackground

    # Alle Objekte werden von beiden Canvas-Fenstern gelöscht und Funktion der Entertaste wird über die Methode
    # .unbind wieder gelöst.
    # Ansprechen aller Canvas Objekte funktioniert über den Tag "all", welcher vordefiniert ist.
    canvasGrafiken.delete("all")
    canvasTextfeld.delete("all")
    tkinterFenster.unbind("<KeyPress-Return>")
    
    # Mehrere Bildobjekte, für die Darstellung der Charaktere, werden geladen und mit der Methode .create_image angezeigt.
    whiteBackground = PhotoImage(file="Assets/Images/White.png")
    # Weiße Hintergründe werden für die Beiden Entitäten erstellt. Diese werden später für die dmgAnimation benötigt.
    # Ein tag muss hier festgelegt werden, um später mit einer speziellen Methode auf die Objekte zugreifen zu können.
    whiteBackgroundPlayer = canvasGrafiken.create_image(20, 350, anchor=W,image=whiteBackground, tag="whitePl")
    whiteBackgroundProject = canvasGrafiken.create_image(780, 150, anchor=E,image=whiteBackground, tag="whitePr")

    playerFigur = PhotoImage(file="Assets/Images/013 Gruppe.png")
    playerFigurAnzeige = canvasGrafiken.create_image(800, 330, anchor=W, image=playerFigur)

    projectFigur = PhotoImage(file="Assets/Images/012 Projekt Kampf Hintergrund.png")
    projectFigurAnzeige = canvasGrafiken.create_image(0, 150, anchor=E, image=projectFigur)

    # Aufrufen der Funktion figurenMove mit Übergabeparameter "800", welcher die Koordinaten der x-Achse repräsentiert und
    # "0" welcher als Counter benutzt wird
    figurenMove(800, 0)


def figurenMove(coordinates, durchlaeufe):
    global playerFigurAnzeige, projectFigurAnzeige

    # Mit der Methode .move werden die Grafiken bei jedem Durchlauf um x,y Koordinaten verschoben.
    # lambda verhindert, dass die Aktion direkt ausgeführt wird und später mit der .after Methode, in einem delay aufgerufen
    # werden kann. 
    moveplayerFigur = lambda: canvasGrafiken.move(playerFigurAnzeige, -5, 0)
    canvasGrafiken.after(durchlaeufe * 10, moveplayerFigur)

    moveprojectFigur = lambda: canvasGrafiken.move(projectFigurAnzeige, +5, 0)
    canvasGrafiken.after(durchlaeufe * 10, moveprojectFigur)

    coordinates -= 5

    # Wenn die Bilder um 780 Pixel verschoben wurden (800-20), werden die anderen Grafiken und der intro text des Kampfes geladen.
    # Der delay von 1700 basiert hier auf der Zeit, die die Verschiebung benötigt (780/5 * 10)+ etwas extra Zeit
    if coordinates == 20:
        canvasGrafiken.after(1700, lambda: introFight())
        canvasGrafiken.after(1700, lambda: tkinterFensterGraphic())

    #Falls coordinates != 20, also die Verscheibung noch nicht abgeschlossen ist, wird durchlaeufe erhöht und die Funktion erneut aufgerufen
    else:
        durchlaeufe += 1
        figurenMove(coordinates, durchlaeufe)


def tkinterFensterGraphic():
    global currentKPIndex, playerArrow, projectArrow, healthbarPlayerColor, healthbarProjectColor

    # Erstellen mehrerer Text und Bild Elemente auf dem Canvas, zur Dartsellung von Leben, Namen und kleinen Akzenten
    # Für jedes Element werden tags für entweder den Spieler oder das Projekt hinzugefügt, da diese als Gruppe angesteuert
    # werden sollen
    playerName = canvasGrafiken.create_text(123, 90, text="PROJEKT", anchor=SW, font=("Press Start 2P", 18), tags="project")
    projectName = canvasGrafiken.create_text(500, 370, text="GRUPPE", anchor=SW, font=("Press Start 2P", 18), tags="player")

    kraftpunkte = canvasGrafiken.create_text(477, 392, text="KP:", font=("Press Start 2P", 15), tags="player")
    kraftpunkte = canvasGrafiken.create_text(100, 112, text="KP:", font=("Press Start 2P", 15), tags="project")

    currentKPIndex = canvasGrafiken.create_text(700, 425, text="100/ 100", anchor=E, font=("Press Start 2P", 18), tags="player")

    playerArrow = PhotoImage(file="Assets/Images/arrowSpieler.png")
    playerHealthBarArrow = canvasGrafiken.create_image(410, 410, anchor=W, image=playerArrow, tags="player")

    projectArrow = PhotoImage(file="Assets/Images/arrowProjekt.png")
    projectHealthBarArrow = canvasGrafiken.create_image(45, 120, anchor=W, image=projectArrow, tags="project")

    # Erstellen von jeweils 2 Rechtecken über die Methode .create_rectangle für den Lebensbalken der beiden Entitäten
    # Die Größe wird über die Koordinaten von 2 gegenüberliegenden Eckpunkten bestimmt, im Schema (x1,y1,x2,y2).
    # Die Farbe wird wie bei anderen Objekten mit fill angepasst. Rechtecke haben dabei standardmäßig einen schwarzen Rand.
    healthbarProjectWhite = canvasGrafiken.create_rectangle(123, 100, 323, 120, fill="white", tags="project")
    healthbarProjectColor = canvasGrafiken.create_rectangle(123, 100, 323, 120, fill="green", tags="project")

    healthbarPlayerWhite = canvasGrafiken.create_rectangle(700, 400, 500, 380, fill="white", tags="player")
    healthbarPlayerColor = canvasGrafiken.create_rectangle(700, 400, 500, 380, fill="green", tags="player")


# Funktion zur Darstellung des Textes zu Beginn des Kampfes
def introFight():

    # Erstellen eines leeren Textobjekts für das Kampf Intro
    introFight = canvasTextfeld.create_text(400, 10, width=750, anchor=N, text="", font=("Press Start 2P", 35), tags="intro")
    # Text für das Kampf Intro
    intro = "Ein wildes PROJEKT ist aufgetaucht! "
    # Schleife zur inkrementellen Darstelllung des Textes im Textobjekt
    for x in range(len(intro)):
        delay = 40 * x
        text = intro[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(introFight, text=text)
        canvasTextfeld.after(delay, textUpdate)

    # Aufrufen der Funktion zur Darstellung eines Knopfes wird nach dem delay aus der Textdarstellung ausgeführt
    tkinterFenster.after(delay + 200, lambda: buttonErsteRunde())


def buttonErsteRunde():
    global button

    # Erstellung eines Buttons mit dem Text 'Press Enter', Knopf bekommt keine Aktion/ Funktion zugewiesen
    button = Button(tkinterFenster, text="PRESS ENTER", bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 23))
    # Laden des Knopfes als Canvas-Window
    canvasTextfeld.create_window(400, 270, window=button)
    # Verknüpfen der Enter-Taste mit der Funktion ersteRunde()
    tkinterFenster.bind("<KeyPress-Return>", lambda b: ersteRunde())

# Funktion in der bestimmt wird, wer den Kampf beginnt und demnach das Menü lädt oder eine Kampfaktion ausführt
def ersteRunde():
    global canvasTextfeld, button, delayFrage, turn

    # Löschen von allen Bild und Textelementen mit dem tag "all"
    canvasTextfeld.delete("all")
    button.destroy()
    tkinterFenster.unbind("<KeyPress-Return>")

    #Erstellen eines leeren TextObjekt auf dem Canvas
    turnRandomText = canvasTextfeld.create_text(400, 30, width=800, anchor=N, text="", font=("Press Start 2P", 28))

    # Festlegen eines strings mit allen Buchstaben und Zahlen. Aus dem String werden zufällige Elemente ausgesucht, um einen
    # random String zu erstellen
    textRandom = "abcdefghijklmnopqrstuvwxyz0123456789öäüABCDEFGHIJKLMOPQRSTUVWXYZ"
    # Definieren der Strings, die angezigt werden, wenn Die Gruppe oder das Projekt beginnt
    gruppeStart = "Die Gruppe fängt an!"
    projektStart = "Das Projekt fängt an!"

    #Eine Zahl zwischen eins und nur wird zufällig generiert und der Variable turn zugewiesen.
    turn = random.randint(1,1)
    # Wenn turn == 0 ist, fängt der Spieler an, bei turn == 1, das Projekt
    # Der Variable roundStart wird der String der beginnenden Entität zugewiesen und die Enter-Taste wird mit der entspechenden
    # Funktion belegt (Wenn der Spieler anfängt wird menu() ausgeführt, wenn das projekt anfängt wird projectAction() ausgeführt
    if turn == 0:
        roundStart = gruppeStart
        tkinterFenster.bind("<KeyPress-Return>", lambda b: menu())
    else:
        roundStart = projektStart
        tkinterFenster.bind("<KeyPress-Return>", lambda b: projectAction())

    # Initialisieren eines Indexes der zusätzlich in der Schleife gebraucht wird.
    index = 0
    for x in range(len(roundStart)+16):
        # Wenn x kleiner als 15 ist, wird der Variable text eine zufällige Auswahl aus dem String/Liste 'textRandom' zugewiesen und
        # der delay zwischen jeder Zuweisung wird auf 70ms festgelegt
        if x < 15:
            delay = 70 * x
            # Mit der .join Methode werden alle Elemente eines Tuples oder einer Liste zusammengefügt als String
            text = "".join(random.sample(textRandom,len(roundStart)))
        # Wenn x größer als 15 ist werden dem text inkrementell Elemente aus dem String roundStart angefügt
        elif x >= 15:
            # Im delay wird eine Verzögerung von 500ms eingebaut und die Zuweisung geschieht etwas schneller nach 60ms
            delay = 300 + 50 * x
            # Zuerst wird wieder ein random string mit der .join Methode erstellt und der Variable textEnd zugewiesen
            # Anschließend werden der variable text, alle Elemente aus dem String roundStart bis zum Listenindex "index" und
            # alle Elemente des Strings textEnd vom Index bis zum Ende des Strings angefügt
            textEnd = "".join(random.sample(textRandom,len(roundStart)))
            text = roundStart[:index] + textEnd[index:]
            # Am Ende der Zuweisung wird der "index" um 1 erhöht
            index += 1
        # Mit der Variable updateText und der .after Methode werden die Textelemte inkrementell in das Canvas-Textobjekt turnRandomText
        # geladen
        updateText = lambda t=text: canvasTextfeld.itemconfigure(turnRandomText,text=t)
        canvasTextfeld.after(delay, updateText)

    #Erstellen eines Textfeldes mit dem Text "PRESS ENTER"
    button = canvasTextfeld.create_text(400,288, text="PRESS ENTER", anchor=S, fill="#555", font=("Press Start 2P", 23))


def menu():
    global menuButton1, menuButton2, menuButton3, tkinterFenster, selectionMarker, selection, menuListMoves, menuListSpecial

    # Löschen aller Canvas Objekte auf dem CanvasTextfeld
    canvasTextfeld.delete("all")

    # Erstellen von 5 verschiedenen Knöpfen:
    # 2 Listen-Knöpfe werden zur Dartellung und zum Umschalten der unterschiedlichen Menüs benutzt.
    # 3 Actions-Knöpfe werden zum ausführen der Kampfactionen verwendet
    # Aufrufen der Knöpfe erfolgt später über zuweisung der Entertaste anstatt über die interne Command Funktion
    # Knöpfe werden also nur zur Textdarstellung benutzt
    menuListMoves = Button(tkinterFenster, text="Moves", bg="#fff",
                            bd=0, fg="#000",
                            font=("Press Start 2P", 30))
    canvasTextfeld.create_window(10, 0, window=menuListMoves, anchor=NW, tags="menu")

    menuListSpecial = Button(tkinterFenster, text="Spezial", bg="#fff",
                            bd=0, fg="#555",
                            font=("Press Start 2P", 30))
    canvasTextfeld.create_window(280, 0, window=menuListSpecial, anchor=NW, tags="menu")

    menuButton1 = Button(tkinterFenster, text="Power Nap", bg="#fff",
                         bd=0, fg="#555", anchor=W,
                         font=("Press Start 2P", 20))
    canvasTextfeld.create_window(100, 100, window=menuButton1, anchor=W, tags="menu")

    menuButton2 = Button(tkinterFenster, text="Energy trinken", bg="#fff",
                         bd=0, fg="#555", anchor=W,
                         font=("Press Start 2P", 20))
    canvasTextfeld.create_window(100, 170, window=menuButton2, anchor=W, tags="menu")

    menuButton3 = Button(tkinterFenster, text="Kaffee trinken", bg="#fff",
                         bd=0, fg="#555", anchor=W,
                         font=("Press Start 2P", 20))
    canvasTextfeld.create_window(100, 240, window=menuButton3, anchor=W, tags="menu")

    # Aufrufen der Funktion menuNavigation
    menuNavigation()


def menuNavigation():
    # Binden von System-Inputs auf die Pfeiltasten und ENTER-Taste.
    # Die .bind Methode üvergibt automatisch den Parameter "b" an die anonyme Funktion lambda.
    # b enthält dabei Informationen über die gedrückte Taste welche wiederum als Übergabeparameter an menuSelection übergeben werden.
    tkinterFenster.bind("<KeyPress-Down>", lambda b: menuSelection(b))
    tkinterFenster.bind("<KeyPress-Up>", lambda b: menuSelection(b))
    tkinterFenster.bind("<KeyPress-Right>", lambda b: menuSelection(b))
    tkinterFenster.bind("<KeyPress-Left>", lambda b: menuSelection(b))


def menuSelection(keystroke):
    # Laden der globalen Variablen, die am Anfang des Programms alle auf 0 definiert wurden
    global menuSelectionUpDown, menuSelectionLeftRight, selection

    # Überprüfung des Parameters keystroke, welcher Informationen über die zuvor gedrückte Taste enthält
    # Mit der Methode .keysym kann ein String extrahiert werden, welcher die gedrückte Taste beschreibt
    if keystroke.keysym == "Right":
        # Falls die rechte Pfeiltaste gedrückt wurde, werden die Variablen MenuSelectionUpDown und -LeftRight entsprechend angepasst.
        # -LeftRight wird um 1 erhöht, falls sie vorher 0 war und MenuSelectionUpDown wird wieder auf 0 gesetzt
        if menuSelectionLeftRight == 0:
            menuSelectionUpDown = 0
            menuSelectionLeftRight += 1
    elif keystroke.keysym == "Left":
        # Falls die linke Pfeiltaste gedrückt wurde, werden die Variablen MenuSelectionUpDown und -LeftRight entsprechend angepasst.
        # -LeftRight wird um 1 verringert, falls sie vorher 1 war und MenuSelectionUpDown wird wieder auf 0 gesetzt
        if menuSelectionLeftRight == 1:
            menuSelectionUpDown = 0
            menuSelectionLeftRight -= 1

    # Basierend auf den Werten für menuSelectionLeftRight werden die Buttons im Menü angepasst und der Text des aktiven Menüs
    # wird auf schwarz gestezt (#000). Für 0, wird die Menüliste Moves angezeigt, für 1 die Menüliste Spezial
    if menuSelectionLeftRight == 0:
        # Anpassung von Button-Optionen erfolgt über die Tkinter Methode .configure
        menuListMoves.configure(fg="#000")
        menuListSpecial.configure(fg="#555")
        menuButton1.configure(text="Power Nap")
        menuButton2.configure(text="Energy trinken")
        menuButton3.configure(text="Kaffee trinken")
    elif menuSelectionLeftRight == 1:
        menuListMoves.configure(fg="#555")
        menuListSpecial.configure(fg="#000")
        menuButton1.configure(text="Gruppenarbeit")
        menuButton2.configure(text="Nachtschicht")
        menuButton3.configure(text="Schummeln")

    if keystroke.keysym == "Down":
        # Falls die untere Pfeiltaste gedrückt wurde, wird die Variable MenuSelectionUpDown entsprechend angepasst.
        # -UpDown wird um 1 erhöht, falls der Index vorher < 3 war. Dies verhindert das der Index größer als die Anzahl der
        # Knöpfe werden kann.
        if menuSelectionUpDown < 3:
            menuSelectionUpDown += 1

    elif keystroke.keysym == "Up":
        # Falls die obere Pfeiltaste gedrückt wurde, wird die Variable MenuSelectionUpDown entsprechend angepasst.
        # -UpDown wird um 1 erhöht, falls der Index vorher > 1 war. Dies verhindert das der Index größer als die Anzahl der
        # Knöpfe werden kann.
        if menuSelectionUpDown > 1:
            menuSelectionUpDown -= 1

    # Laden ein Bildes zur Darstellung eines kleines Pfeils im Menü
    selection = PhotoImage(file="Assets/Images/selection.png")

    # Basierend auf dem Wert von menuselectionUpDown werden nun die Buttons im Menü entsprechend angepasst
    # So wird immer der Text des "aktiven" Buttons vergrößert auf Schriftgröße 25. Die Farbe wird auch hier auf Schwarz
    # gesetzt und das Bild mit dem Pfeil wird vor dem entsprechenden Button geladen. Die "nicht aktiven" Knöpfe werden
    # dann zurückgesetzt auf die Standardgröße und Farbe
    if menuSelectionUpDown == 1:
        selectionMarker = canvasTextfeld.create_image(95, 97, anchor=E, image=selection, tags="menu")
        menuButton1.configure(fg="#000", font=("Press Start 2P", 25))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))

        # Basierend auf dem Index von menuSelectionUpDown, also in welcher Menüliste sich das Menü befindet, werden
        # der Enter-Taste die Funktion playerAction mit dem Übergabeparameter für die entsprechende Fähigkeit zugewiesen.
        if menuSelectionLeftRight == 0:
            tkinterFenster.bind("<KeyPress-Return>", lambda b: playerAction(1))
        else:
            tkinterFenster.bind("<KeyPress-Return>", lambda b: playerAction(4))
    elif menuSelectionUpDown == 2:
        selectionMarker = canvasTextfeld.create_image(95, 167, anchor=E, image=selection, tags="menu")
        menuButton2.configure(fg="black", font=("Press Start 2P", 25))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            tkinterFenster.bind("<KeyPress-Return>", lambda b: playerAction(2))
        else:
            tkinterFenster.bind("<KeyPress-Return>", lambda b: playerAction(5))
    elif menuSelectionUpDown == 3:
        selectionMarker = canvasTextfeld.create_image(95, 237, anchor=E, image=selection,tags="menu")
        menuButton3.configure(fg="black", font=("Press Start 2P", 25))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        if menuSelectionLeftRight == 0:
            tkinterFenster.bind("<KeyPress-Return>", lambda b: playerAction(3))
        else:
            tkinterFenster.bind("<KeyPress-Return>", lambda b: playerAction(6))
    # Falls -UpDown 0 sein sollte, werden alle Buttons auf den Standard zurückgesetzt un die Funktion von der Enter-Taste
    # wird gelöst
    elif menuSelectionUpDown == 0:
        menuButton3.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton2.configure(fg="#555", font=("Press Start 2P", 20))
        menuButton1.configure(fg="#555", font=("Press Start 2P", 20))
        tkinterFenster.unbind("<KeyPress-Return>")

# Funktion in der die verschiedenen Fähigkeiten der Gruppe definiert werden
def playerAction(move):
    global healing

    # Definieren einiger variablen für die Chance zu verfehlen, den Schaden, den der Spieler erleidet und ob eine
    # abfrage ob die ausgeführte Fähigkeit heilen können soll.

    missChance = 0
    dmgPlayer = 0
    healing = FALSE

    if move == 1:
        actionText = "Die Gruppe hat einen Power Nap gemacht!"
        dmgPlayer = round(0.1 +random.randint(-5,20)/100,2)
        dmgProject = 0
        healing = TRUE
    elif move == 2:
        actionText = "Die Gruppe hat Energy getrunken!"
        dmgProject = 0.2
        missChance = random.randint(1, 5)
    elif move == 3:
        actionText = "Die Gruppe hat Kaffee getrunken!"
        dmgProject = 0.25
        missChance = random.randint(1, 4)
    elif move == 4:
        actionText = "Die Gruppe hat Gruppenarbeit eingesetzt!"
        dmgProject = round(0.3 +random.randint(-30,0)/100,2)
        missChance = random.randint(1, 3)
    elif move == 5:
        actionText = "Die Gruppe hat eine Nachtschicht eingelegt!"
        dmgProject = round(0.33 + random.randint(-20,5)/100,2)
        selfDamageModifier = random.randint(1,10)
        if selfDamageModifier <= 5:
            dmgPlayer = round(0.1 +random.randint(0,10)/100,2)
            actionText= "Die Gruppe ist übermüdet und fügt sich selbst Schaden zu"
    else:
        actionText = "Die Gruppe hat Schummeln benutzt!"
        dmgProject = 0.5
        missSchummeln = random.randint(1, 10)
        selfDamageModifier = random.randint(1,10)
        if missSchummeln <= 7:
            dmgProject = 0
            dmgPlayer = 0.3 if selfDamageModifier <= 7 else 0.09 if selfDamageModifier <= 9 else 0
        if dmgPlayer > 0:
            actionText = "Die Gruppe ist beim Schummeln aufgeflogen!"
        elif dmgPlayer == 0 and dmgProject == 0:
            missChance = 1


    if missChance == 1:
        miss = TRUE
        dmgProject = 0
    else:
        miss = FALSE

    dmgProcessing(dmgPlayer,dmgProject, actionText, miss)

def projectAction():
    global healing, currentLifeProject

    missChance = 0
    miss = FALSE
    dmgProject = 0
    healing = FALSE
    randomizer = random.randint(1,100)

    if randomizer <= 5:
        actionText = "Das Projekt setzt Moodle ist gnadenlos!!1!11! ein"
        dmgPlayer = 1
        missChance = 0
    elif randomizer <= 25 and currentLifeProject <= 0.9:
        actionText = "Das Projekt wird schwieriger!"
        dmgPlayer = 0
        dmgProject = round(0.1 +random.randint(-5,20)/100,2)
        healing = TRUE
    elif randomizer <= 50:
        actionText = "Das Projekt hat 3 gemacht!"
        dmgPlayer = round(0.2 + random.randint(-5,5)/100, 2)
        missChance = random.randint(1, 5)
    elif randomizer <= 75:
        actionText = "Das Projekt hat 4 gemacht!"
        dmgPlayer = round(0.25 + random.randint(-5,5)/100,2)
        missChance = random.randint(1, 5)
    elif randomizer <= 90:
        actionText = "Das Projekt hat 5 gemacht!"
        dmgPlayer = round(0.3 + random.randint(-10,15)/100,2)
        missChance = random.randint(1, 4)
    elif randomizer <= 100:
        actionText = "Das Projekt hat 6 gemacht!"
        dmgPlayer = round(0.3 + random.randint(-5,20)/100,2)
        missChance = random.randint(1, 3)


    if missChance == 1:
        dmgPlayer = 0
        miss =TRUE

    dmgProcessing(dmgPlayer, dmgProject, actionText, miss)

def dmgProcessing(player, project, text, miss):
    global menuSelectionLeftRight, menuSelectionUpDown, menhealthbarProjectColor, healthbarPlayerColor, currentLifeProject, currentLifePlayer
    # Zu Beginn der Verarbeitung der ausgeführten Aktion werden zunächst alle Keybindings gelöst und alle Elemente werden von vom Textfeld gelöscht.
    tkinterFenster.unbind("<KeyPress-Down>")
    tkinterFenster.unbind("<KeyPress-Up>")
    tkinterFenster.unbind("<KeyPress-Right>")
    tkinterFenster.unbind("<KeyPress-Left>")
    tkinterFenster.unbind("<KeyPress-Return>")
    canvasTextfeld.delete("all")

    # Die Variablen zur Menüauswahl werden wieder auf 0 genutzt, damit in der nächsten Runde keine Vorauswahl besteht
    menuSelectionLeftRight = 0
    menuSelectionUpDown = 0

    #Erstellen eines leeren Textobjekt auf dem Canvas
    textMove = canvasTextfeld.create_text(400, 20,width=750, anchor=N, text="", font=("Press Start 2P", 25))

    # Mit der üblichen Funktion werden dem Objekt textMove der String aus dem Übergabeparameter actionText inkrementell
    # übergeben
    for x in range(len(text)+1):
        delay = 40 * x
        actionText = text[:x]
        updateText = lambda t=actionText: canvasTextfeld.itemconfigure(textMove, text=t)
        canvasTextfeld.after(delay, updateText)
    # Sollte der Parameter miss = TRUE sein, wird zusätzlich ein der String inder Varaible "miss" an textMove übergeben.
    if miss == TRUE:
        miss = "Der Angriff hat verfehlt!"
        for x in range(len(miss) + 1):
            delay = 2000 + 40 * x
            missText = miss[:x]
            updateText = lambda t=missText: canvasTextfeld.itemconfigure(textMove, text=t)
            canvasTextfeld.after(delay, updateText)

    # Sollten die übergebenen Schadenswerte player größer als 0 sein, werden die Animationen für den Kmapf
    # und die Darstellung der Leben geladen.
    if player > 0:
        # Nach dem Delay in dem der Text erstellt wurde, wird zunächst die dmgAnimation aufgerufen mit dem Übergabeparameter (0), dieser
        # zählt die Durchläufe innerhalb der Funktion
        canvasGrafiken.after(delay + 500, lambda: dmgAnimationPlayer(0))
        # Der übergebene Schaden in Prozent also "0." Wert wird in eine ganze Zahl umgerechnet, aufgerundet und als Variable "healthReductionPlayer" gespeichert
        healthReductionPlayer = int(round(player * 100))
        # Die Werte 1, welcher wieder als Index für die Schleifendurchläufe dient, die Variable healthReductionPlayer und der Parameter player, werden nun
        # als Übergabeparameter an die Funktion healtBarReductionPlayer übergeben
        canvasGrafiken.after(delay + 800, lambda: healthBarReductionPlayer(1, healthReductionPlayer, player))

    # Sollten die übergebenen Schadenswerte project und project größer als 0 sein, werden die Animationen für das Projekt geladen.
    # Diese funktionieren genau wie beim Spieler auch
    if project > 0:
        # Nach dem Delay in dem der Text erstellt wurde, wird zunächst die dmgAnimation aufgerufen mit dem Übergabeparameter (0), dieser
        # zählt die Durchläufe innerhalb der Funktion
        canvasGrafiken.after(delay + 500, lambda: dmgAnimationProject(0))
        # Der übergebene Schaden in Prozent also "0." Wert wird in eine ganze Zahl umgerechnet, aufgerundet und als Variable "healthReductionProject" gespeichert
        healthReductionProject = int(round(project * 100))
        # Die Werte 1, welcher wieder als Index für die Schleifendurchläufe dient, die Variable healthReductionProject und der Parameter player, werden nun
        # als Übergabeparameter an die Funktion healtBarReductionProject übergeben
        canvasGrafiken.after(delay + 800, lambda: healthBarReductionProject(1, healthReductionProject, project))

    # Die Funktion buttonNextRound wird nach dem delay geladen.
    canvasGrafiken.after(delay, lambda: buttonNextRound())

def buttonNextRound():
    global turn
    # Erstellen eines Buttons mit der Aufschrift "PRESS ENTER"
    button = Button(tkinterFenster, text="PRESS ENTER" , bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 23))
    # Laden des Buttons in Canvas Window
    canvasTextfeld.create_window(400, 270, window=button)
    # Basierend darauf wer angefangen hat bzw. zuletzt dran war, wird die nächste Aktion an die Enter-Taste gebunden.
    # Die globale Variable turn wird dafür auf ihren Wert überprüft und dann entsprechend für den nächsten Zug angepasst.
    if turn == 1:
        # War die letzte Aktion vom Projekt, wird das Kampfmenü geladen
        tkinterFenster.bind("<KeyPress-Return>", lambda b: menu())
        turn = 0
    else:
        #Wurde zuletzt eine Spieleraktion durchgeführt, wird eine Projekt Aktion ausgeführt
        tkinterFenster.bind("<KeyPress-Return>", lambda b: projectAction())
        turn = 1

# Animation die das Bild der Gruppe blinken lässt
def dmgAnimationPlayer(durchlaeufe):

    # Mit der Canvas-Methode tag_raise können alle Objekte mit dem gleichen Tag um eine Ebene nach oben, also in den Vordergrund
    # gehoben werden. Danch wird das Objekt mit der Methode tag_lower wieder in den Hintergrund geschoben. Dies geschieht in
    # zeitversetzten Abständen mit der .after Methode, wodurch ein blinkender Effekt ensteht.
    # Das verschobenen Objekt ist hier einfach nur ein weißes Quadrat, welches in der Funktion tkinterFensterGraphic() erstellt wurde
    raiseWhite = lambda: canvasGrafiken.tag_raise("whitePl")
    canvasGrafiken.after(durchlaeufe * 70, raiseWhite)
    lowerWhite = lambda: canvasGrafiken.tag_lower("whitePl")
    canvasGrafiken.after(durchlaeufe * 100, lowerWhite)

    # Die Abfrage überprüft den Parameter durchlaeufe, und erhöht in um 1, falls er kleiner als 4 sein wollte.
    if durchlaeufe < 4:
        durchlaeufe += 1
        # Solange durchlaeufe < 4 wird die Funktion erneut aufgerufen.
        dmgAnimationPlayer(durchlaeufe)

def dmgAnimationProject(durchlaeufe):

    # Mit der Canvas-Methode tag_raise können alle Objekte mit dem gleichen Tag um eine Ebene nach oben, also in den Vordergrund
    # gehoben werden. Danch wird das Objekt mit der Methode tag_lower wieder in den Hintergrund geschoben. Dies geschieht in
    # zeitversetzten Abständen mit der .after Methode, wodurch ein blinkender Effekt ensteht.
    # Das verschobenen Objekt ist hier einfach nur ein weißes Quadrat, welches in der Funktion tkinterFensterGraphic() erstellt wurde
    raiseWhite = lambda: canvasGrafiken.tag_raise("whitePr")
    canvasGrafiken.after(durchlaeufe * 70, raiseWhite)
    lowerWhite = lambda: canvasGrafiken.tag_lower("whitePr")
    canvasGrafiken.after(durchlaeufe * 100, lowerWhite)

    # Die Abfrage überprüft den Parameter durchlaeufe, und erhöht in um 1, falls er kleiner als 4 sein wollte.
    if durchlaeufe < 4:
        durchlaeufe += 1
        # Solange durchlaeufe < 4 wird die Funktion erneut aufgerufen.
        dmgAnimationProject(durchlaeufe)


def healthBarReductionPlayer(durchlaeufe, healthReduction, dmgPlayer):
    global currentLifePlayer, healing

    # Zunächst wird über die globale Variable "healing" überprüft, ob sie TRUE oder FALSE ist, bzw. ob die Fähigkeit Schaden hinzufügen oder heilen soll
    if healing == FALSE:
        # Wenn es keine Heilung ist, werden die aktuellen Leben (ein "0."-Wert) in ein ganzzahligen Wert umgerechnet und die Anzahl der Durchläufe
        # werden von den Leben subtrahiert. Das Ergebniss wird der Variable currentKP zugewiesen.
        currentKP = round(currentLifePlayer * 100 - durchlaeufe)
    else:
        # Wenn es sich um Heilung handelt, werden die aktuellen Leben (ein "0."-Wert) in ein ganzzahligen Wert umgerechnet und die Anzahl der Durchläufe
        # werden stattdessen auf die Leben addiert.
        currentKP = round(currentLifePlayer * 100 + durchlaeufe)
        # Falls der Wert der von currentKP 100 überschreitet, wird er auf 100 zurückgesetzt.
        if currentKP > 100:
            currentKP = 100


    # Über die Canvas-Methode coords, können die Koordinaten der Rechtecke für die Leben der Spieler neu angepasst werden. Anders als bei der Methode .move
    # werden die Koordinaten komplett neu definiert, weshalb die genauen Leben, also currentKP benötigt werden, anstatt einfach nur -durchlaeufe bazuziehen.
    # Der Wert für CurrentKP wird hier * 2 gerechnet, da 2 Pixel pro Leben in der DArstellung genutzt werden.
    reduceBalken = lambda: canvasGrafiken.coords(healthbarPlayerColor, 500 + currentKP * 2, 400, 500, 380)
    # Die Anpassung wird wieder in einem delay von 40ms * durchlaufe dargestellt
    canvasGrafiken.after(durchlaeufe * 40, reduceBalken)

    # In einer weiteren Funktion werden gleichzeitig die angezeigten Leben basierend auf currentKP / 100 angepasst. Dies geschieht über die bekannte Methode
    # .itemconfigure, welche auch für alle anderen Textanimationen benutzt wird.
    changeKPIndex = lambda: canvasGrafiken.itemconfigure(currentKPIndex, text=str(currentKP) + "/ 100")
    # Die Anpassung wird ebenfalls in einem delay von 40ms * durchlaufe dargestellt.
    canvasGrafiken.after(durchlaeufe * 40, changeKPIndex)

    # Basierend auf der Größe von currentKP wird der varaible healthColor eine Farbe zugewiesen.
    healthColor = "green" if currentKP >= 80 else "lightgreen" if currentKP >= 60 else "yellow" if currentKP >= 40 else "orange" if currentKP >= 20 else "red"

    #Mit der Methode .itemconfigure wird dann die Farbe der healthBar angepasst.
    changeColor = lambda: canvasGrafiken.itemconfigure(healthbarPlayerColor, fill=healthColor)
    # Die Anpassung wird ebenfalls in einem delay von 40ms * durchlaufe dargestellt.
    canvasGrafiken.after(durchlaeufe * 40, changeColor)


    if durchlaeufe < healthReduction and currentKP > 0:
        # Wenn die Azahl der Durchläufe kleiner als die abzuziehenden Leben ist und die Leben (currentKP) nicht schon auf 0 gesunken sind, dann wird durchlaeufe um 1 erhöht
        # und die Funktion wird erneut aufgerufen.
        durchlaeufe += 1
        healthBarReductionPlayer(durchlaeufe, healthReduction, dmgPlayer)
    elif currentKP > 0 and healing == FALSE:
        # Sollten genug durchlaeufe gemacht worden sein, aber die Leben noch größer als 0 sind, wird überprüft ob es sich bei der Aktion um Heilung handelt,
        # wenn nicht wird dmgPlayer ("0."-Wert) von den aktuellen Leben des Spielers abgezogen.
        currentLifePlayer -= dmgPlayer
    elif healing == TRUE:
        # Sollte es sich um Heilung handeln, wird dmgPlayer auf die aktuellen Leben des Spielers (currentLifePlayer) drauf gerechnet.
        currentLifePlayer += dmgPlayer
        # Sollte der Wert von currentlifePlayer 100% (1) übersteigen, wird er wieder auf 1 gesetzt.
        if currentLifePlayer > 1:
            currentLifePlayer = 1
    else:
        # Sollte keine der obigen Bedingungen zutreffen, bzw. ist currentKP = 0, dann wird currentLifePlayer ebenfalls auf 0 gesetzt und
        # die Funktion spielEnde wird im gleichen Delay wie die anderen Funktionen geladen. Dabei wird der Funktion der Übergabeparameter
        # "verloren" mitgegeben
        currentLifePlayer = 0
        canvasGrafiken.after(durchlaeufe * 40, lambda: spielEnde("verloren"))


def healthBarReductionProject(durchlaeufe, healthReduction, dmgProject):
    global currentLifeProject, healing

    # Zunächst wird die globale Variable "healing" überprüft, ob sie TRUE oder FALSE ist, bzw. ob die Fähigkeit Schaden hinzufügen oder heilen soll
    if healing == FALSE:
        # Wenn es keine Heilung ist, werden die aktuellen Leben (ein "0."-Wert) in ein ganzzahligen Wert umgerechnet und die Anzahl der Durchläufe
        # werden von den Leben subtrahiert. Das Ergebniss wird der Variable currentKP zugewiesen.
        currentKP = round(currentLifeProject * 100 - durchlaeufe)
    else:
        # Wenn es sich um Heilung handelt, werden die aktuellen Leben (ein "0."-Wert) in ein ganzzahligen Wert umgerechnet und die Anzahl der Durchläufe
        # werden stattdessen auf die Leben addiert
        currentKP = round(currentLifeProject * 100 + durchlaeufe)
        # Falls der Wert der von currentKP 100 überschreitet, wird er auf 100 zurückgesetzt
        if currentKP > 100:
            currentKP = 100

    # In einer weiteren Funktion werden gleichzeitig die angezeigten Leben basierend auf currentKP / 100 angepasst. Dies geschieht über die bekannte Methode
    # .itemconfigure, welche auch für alle anderen Textanimationen benutzt wird.
    reduceBalken = lambda: canvasGrafiken.coords(healthbarProjectColor, 123, 100, 123 + currentKP * 2, 120)
    canvasGrafiken.after(durchlaeufe * 40, reduceBalken)

    # Die Anpassung wird wieder in einem delay von 40ms * durchlaufe dargestellt
    healthColor = "green" if currentKP >= 80 else "lightgreen" if currentKP >= 60 else "yellow" if currentKP >= 40 else "orange" if currentKP >= 20 else "red"

    # Mit der Methode .itemconfigure wird dann die Farbe der healthBar angepasst
    changeColor = lambda: canvasGrafiken.itemconfigure(healthbarProjectColor, fill=healthColor)
    # Die Anpassung wird ebenfalls in einem delay von 40ms * durchlaufe dargestellt
    canvasGrafiken.after(durchlaeufe * 40, changeColor)

    if durchlaeufe < healthReduction and currentKP > 0:
        # Wenn die Azahl der Durchläufe kleiner als die abzuziehenden Leben ist und die Leben (currentKP) nicht schon auf 0 gesunken sind, dann wird durchlaeufe um 1 erhöht
        # und die Funktion wird erneut aufgerufen
        durchlaeufe += 1
        healthBarReductionProject(durchlaeufe, healthReduction, dmgProject)
    elif currentKP > 0 and healing == FALSE:
        # Sollten genug durchlaeufe gemacht worden sein, aber die Leben noch größer als 0 sind, wird überprüft ob es sich bei der Aktion um Heilung handelt,
        # wenn nicht wird der Parameter dmgProject ("0."-Wert) von den aktuellen Leben des Projekts (currentLifeProject) abgezogen.
        currentLifeProject -= dmgProject
    elif healing == TRUE:
        # Sollte es sich um Heilung handeln, wird dmgPlayer auf die aktuellen Leben des Projekts drauf gerechnet
        currentLifeProject += dmgProject
        # Sollte der Wert von currentLifeProject 100% (1) übersteigen, wird er wieder auf 1 gesetzt
        if currentLifeProject > 1:
            currentLifeProject = 1
    else:
        # Sollte keine der obigen Bedingungen zutreffen, bzw. ist currentKP = 0, dann wird currentLifePlayer ebenfalls auf 0 gesetzt und
        # die Funktion spielEnde wird im gleichen Delay wie die anderen Funktionen geladen. Dabei wird der Funktion der Übergabeparameter
        # "verloren" mitgegeben
        currentLifeProject = 0
        canvasGrafiken.after(durchlaeufe * 40, lambda: spielEnde("gewonnen"))


def spielEnde(ende):

    # Belegung aller Tasten werden gelöst und das Textfeld wird gelöscht
    tkinterFenster.unbind("<KeyPress-Down>")
    tkinterFenster.unbind("<KeyPress-Up>")
    tkinterFenster.unbind("<KeyPress-Right>")
    tkinterFenster.unbind("<KeyPress-Left>")
    tkinterFenster.unbind("<KeyPress-Return>")
    canvasTextfeld.delete("all")

    # Überprüfung ob der Parameter ende "gewonnen" oder "verloren" ist
    if ende == "gewonnen":
        # Die Animation für 
        canvasGrafiken.after(500, lambda: animationGewonnen(1, 300))
        canvasGrafiken.after(1200, lambda: textfightEnde(ende))
    else:
        canvasGrafiken.after(1000, lambda: animationVerloren(1, 350))
        canvasGrafiken.after(1200, lambda: textfightEnde(ende))


def animationGewonnen(durchlaeufe, coordinates):

    canvasGrafiken.delete("project")
    moveprojectFigur = lambda: canvasGrafiken.move(projectFigurAnzeige, 0,-5)
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
    tkinterFenster.bind("<KeyPress-Return>", lambda b: outro())

    fightEnd = canvasTextfeld.create_text(400, 10, width=780, anchor=N, text="", font=("Press Start 2P", 30))
    if ende == "gewonnen":
        fightEndText = "Das Projekt wurde besiegt!"
    else:
        fightEndText = "Die Gruppe wurde besiegt!"


    for x in range(len(fightEndText)+1):
        delay = 40 * x
        text = fightEndText[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(fightEnd, text=text)
        canvasGrafiken.after(delay, textUpdate)

    button = Button(tkinterFenster, text="PRESS ENTER", bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 20))
    canvasTextfeld.create_window(400, 275, window=button)


def outro():
    global picture, button, currentLifeProject, currentLifePlayer

    canvasGrafiken.delete("all")
    canvasTextfeld.delete("all")
    tkinterFenster.bind("<KeyPress-Return>", lambda b: setup())

    outroText = canvasTextfeld.create_text(400, 10, width=780, anchor=N, text="", font=("Press Start 2P", 17))

    if  currentLifePlayer > 0.8:
        picture = PhotoImage(file="Assets/Images/001_Sternenhimmel.png")
        outro = "War es ein Wunder? War es pures Können? Das alles spielte keine Rolle. Den Helden war es gelungen, was bis jetzt noch niemandem gelungen war. Sie hatten eine 1 für ihr Projekt bekommen. Der erste Schritt in eine steile Karriere."
    elif currentLifePlayer > 0.6:
        picture = PhotoImage(file="Assets/Images/002_Schule.png")
        outro = "Ach eine 2. Die vielleicht beste Note. Viele würden jetzt protestieren und sagen: „Momentmal eine 1 ist doch viel besser. Doch ist sie das? Also faktisch ist sie natürlich besser! Aber wer will schon der Streber sein, der für eine Zahl so ackert. Nein die zwei ist perfekt!“"
    elif currentLifePlayer > 0.4:
        picture = PhotoImage(file="Assets/Images/003_Schule_Apokalypse.png")
        outro = 'Eine 3. Im anderen Kontext ist befriedigend das Ziel. Hier ist es zumindest keine Schande.'
    elif currentLifePlayer > 0.2:
        picture = PhotoImage(file="Assets/Images/coronavirus.png")
        outro = "Knapp getroffen gilt auch noch. Mit der 4 hat man es zwar nur noch geradeso geschafft, aber solange die Note hinter einem Kaffeefleck auf dem Zeugnis verschwindet, passt das schon."
    elif currentLifePlayer > 0:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        outro = "Uff, eine 5. Das tut weh! Sich zu schämen ist hier wohl angebracht. Der einzige Wehrmutstropfen ist: Es geht noch schlimmer."
    else:
        picture = PhotoImage(file="Assets/Images/Gruppe.png")
        outro ="Eine 6? Da könnte man ja glatt meinen die Helden hätten es gar nicht versucht. Wobei Helden in diesem Fall wohl nicht mehr angebracht ist. Nennen wir sie einfach Personen. Ja die Personen haben ins Klo gegriffen!"

    canvasGrafiken.create_image(400, 250, anchor= CENTER, image=picture)

    for x in range(len(outro)+1):
        delay = 30 * x
        text = outro[:x]
        textUpdate = lambda text=text: canvasTextfeld.itemconfigure(outroText, text=text)
        canvasTextfeld.after(delay, textUpdate)

    currentLifeProject = 1
    currentLifePlayer = 1
    button = Button(tkinterFenster, text="TRY AGAIN", bd=0, bg="#fff", fg="#555", anchor=S,
                     font=("Press Start 2P", 23))
    canvasTextfeld.create_window(400, 270, window=button)

# Erstellen des Tkinter Fensters. Mit dem definieren der Variable tkinterFenster, als Funktion Tk(), wird ds Fenster initialisiert.
tkinterFenster = Tk()
# Über verschiedene Methoden können Tkinter Objekte angepasst werden.
# .title setzt einen Fenster-Namen fest. 
tkinterFenster.title("Das Projekt")
# .geometry setzt die Größe in x*y Pixeln fest
tkinterFenster.geometry("800x800")
# .configure bearbeitet Eigenschaften eines Tkinter Objekts. Mit bg, wird der Background auf einen Hexcode gesetzt
tkinterFenster.configure(bg="#555")

#Definieren einiger globaler variablen die später benötigt werden
# menuSelection wird für die Auswahl im Kampfmenü verwendet  
menuSelectionUpDown = 0
menuSelectionLeftRight = 0
# currentLife sind die Prozentualen Leben der
currentLifeProject = 1
currentLifePlayer = 1

healing = FALSE


#Aufrufe der ersten Funktion setupWindow()
setupWindow()

# .mainloop beendet den Loop in den Tkinter Funktionen und Methoden lesen und ausführen kann. 
# Die Methode muss global definiert sein und darf nicht durch schleifen die den Main-Thread unterbrechen gestoppt werden.  
tkinterFenster.mainloop()