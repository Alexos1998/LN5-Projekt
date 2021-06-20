from tkinter import *

def setup():
    #Festlegen von globalen Variablen die auch außerhalb der lokalen Funktion genutzt werden sollen
    global canvasSpielfeld, canvasTextfeld, spielerFigurAnzeige, spielerFigur, projektFigurAnzeige, projektFigur, button1

    # Erstellen eines Canvas für den oberen Spielfeldbereich, in den später Bilder und Animationen geladen werden
    canvasSpielfeld = Canvas(spielfeld, height=500, width=800, bg="#fff")
    canvasSpielfeld.pack()

    #Erstellen des Canvas, zur Darstellung von Spieltext und des Kampf-Menüs
    canvasTextfeld = Canvas(spielfeld, height=300, width=800, bg="#fff")
    canvasTextfeld.pack()

    #Laden der Bilddateien für die Gruppe und das Projekt mit der Funktion PhotoImage.
    #Darstellung des Bildes auf dem Canvas mit der Methode create_image und entsprechenden xy-Koordinaten
    spielerFigur = PhotoImage(file="Assets/Images/Gruppe.png")
    spielerFigurAnzeige = canvasSpielfeld.create_image(20, 330, anchor=W, image=spielerFigur)

    projektFigur = PhotoImage(file="Assets/Images/coronavirus.png")
    projektFigurAnzeige = canvasSpielfeld.create_image(780, 150, anchor=E, image=projektFigur)

    # Erstellen des Intro-Texts. Hier wird mit tags="" eine Art Anker gesetzt, über den das Objekt vom Modul aufgerufen werden kann
    introText = canvasTextfeld.create_text(10,5, width=750, anchor=NW, text="Ein wildes PROJEKT ist aufgetaucht!", font=("Press Start 2P", 35), tags="intro")

    button1 = Button(spielfeld, text="Auf gehts",highlightthickness=0, bd=0, bg="#fff",fg="#555",command=lambda: ersteRunde())
    canvasTextfeld.create_window(400, 280, window=button1)

    spielfeldGraphik(1,1)

def spielfeldGraphik(spieler,projekt):
    global nameSpieler, durchlauf

    # Darstellung der Namen auf dem Spielfeld. Der Name des Spielers wird basierend auf der Eingabe am Anfang definiert
    canvasSpielfeld.create_text(123,90,text="PROJEKT", anchor=SW, font=("Press Start 2P", 18))
    canvasSpielfeld.create_text(500, 370, text=nameSpieler, anchor= SW, font=("Press Start 2P", 18))

    # Prozentuale Leben des Spielers und des Projekts werden umgerechnet um als x-Koordinate für die darstellung der
    # Lebensbalken
    currentHealthProjektXCoord = 200 * projekt + 123
    currentHealthSpielerXCoord = 200 * spieler + 500

    # Erstellen der beiden Lebensbalken für das Projekt. Größe wird durch die Koordinaten der
    # Ecken des Rechtecks bestimmt (Schema: x1, y1, x2, y2)
    canvasSpielfeld.create_rectangle(123, 100, 323, 120, fill="white")
    canvasSpielfeld.create_rectangle(123, 100, currentHealthProjektXCoord, 120, fill="green")

    # Erstellen der beiden Lebensbalken für das Projekt. Größe wird durch die Koordinaten der
    # Ecken des Rechtecks bestimmt (Schema: x1, y1, x2, y2)
    canvasSpielfeld.create_rectangle(700, 400, 500, 380, fill="white")
    canvasSpielfeld.create_rectangle(currentHealthSpielerXCoord, 400, 500, 380, fill="green")

    #Prozentuale Leben des spielers werden in einem String dargestellt um als Text zur Darstelung weitergegben werden zu können
    currentKPIndex = str(int(100 * spieler)) + "/ 100"

    #Überpüfung ob der Spieler volle Leben hat (1 = 100%)
    if durchlauf == 1:
        # Aktuellen Leben werden als Text dargestellt, wenn der Spieler 100% Leben hat
        canvasSpielfeld.create_text(700, 425, text= currentKPIndex, anchor= E, font=("Press Start 2P", 18), tags="currentKP")
        durchlauf += 1
    else:
        # Anzeige der aktuellen Leben wird basierend auf den neuen prozentualen Leben verändert
        canvasSpielfeld.itemconfigure("currentKP", text=currentKPIndex)

def ersteRunde():
    global canvasTextfeld, delayFrage

    canvasTextfeld.delete("intro")
    button1.destroy()
    spielfeld.after(100, menu())

def menu():
    global menuButton1, menuButton2, menuButton3, spielfeld, selectionMarker, selection, menuListMoves, menuListSpecial

    #Erstellen von 5 verschiedenen Knöpfen:
    #2 Menü-Knöpfe werden zur Dartellung und zum umschalten der unterschiedlichen Menüs benutzt.
    #3 Actions-Knöpfe werden zum ausführen der Kampsactionen benutzt
    menuListMoves = Button(spielfeld, text="Moves", bg="#fff", highlightthickness=0, bd=0, fg="#555", font=("Press Start 2P", 30), command = lambda: changeMenu("menu"))
    canvasTextfeld.create_window(10, 0, window=menuListMoves, anchor=NW)

    menuListSpecial = Button(spielfeld, text="Spezial", bg="#fff",highlightthickness=0, bd=0, fg="#555", font=("Press Start 2P", 30), command = lambda: changeMenu("spezial"))
    canvasTextfeld.create_window(280, 0, window=menuListSpecial, anchor=NW)

    menuButton1 = Button(spielfeld, text="Power Nap", bg="#fff",highlightthickness=0, bd=0, fg="#555", anchor=W, font=("Press Start 2P", 20),command = lambda: spielfeldGraphik(1,0.8))
    canvasTextfeld.create_window(100, 100, window=menuButton1, anchor=W)

    menuButton2 = Button(spielfeld, text="Energy Booster", bg="#fff",highlightthickness=0, bd=0, fg="#555", anchor=W, font=("Press Start 2P", 20), command = lambda: spielfeldGraphik(0.8,0.8))
    canvasTextfeld.create_window(100, 170, window=menuButton2, anchor=W)

    menuButton3 = Button(spielfeld, text="Kaffee Booster", bg="#fff",highlightthickness=0, bd=0, fg="#555", anchor=W, font=("Press Start 2P", 20), command = lambda: action(3))
    canvasTextfeld.create_window(100, 240, window=menuButton3, anchor=W)

def changeMenu(changemenuspezial):
    global selection

    if changemenuspezial =="menu":
        if selection == 1:
            selection -= 0
        menuButton1.configure(text="Power Nap")
        menuButton2.configure(text="Energy Booster")
        menuButton3.configure(text="Kaffee Booster")

    elif changemenuspezial =="spezial":
        if selection == 1:
            selection +=1
        menuButton1.configure(text="Gruppenarbeit")
        menuButton2.configure(text="Nachtschicht")
        menuButton3.configure(text="Keine Idee mehr")

def action():
    print("ich tue gar nichts")


#Erstellen des Tkinter Fensters. Hintergrund wird auf dunkel grau gesetzt
spielfeld = Tk()
spielfeld.title("Pokemon in gut")
spielfeld.geometry("800x800")
spielfeld.configure(bg="#555")

#Definieren einiger globaler Variablen die später gebraucht werden
selection = 0
durchlauf = 1
nameSpieler = "GRUPPE"
setup()
spielfeld.mainloop()

