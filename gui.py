import tkinter as tk
from lingo import Lingo
from timer import Timer
from highscores import HighScores
from threading import Thread
from threading import Event
import time

#aanmaken van het object
lingo = Lingo()

#bepaal het woord
lingo.woord = lingo.set_woord()

invoervelden = {}

#aanmaken timer en op 0 zetten
timer = Timer()
timer.reset()

def run_timer(sluit):
    while True:
        timerLabel["text"] = str(timer.get_elapsed_s())
        time.sleep(1)
        if sluit.is_set():
            break

def naam(event):
    lingo.naam = naamVeld.get()
    print(lingo.naam)

def handle_clear(event):
    #pack gameframe weer en vergeet resultaat
    gameFrame.pack()
    resultFrame.pack_forget()
    #reset alle labels
    statusLabel["text"] = "Succes!"
    statusLabel["fg"] = "green"
    naamVeld.delete(0, "end")
    for veld in invoervelden:
        invoervelden[veld].delete(0, "end")
    beurtLabel["text"] = "1/5"
    #zet het object weer op 0
    lingo.woord = lingo.set_woord()
    lingo.beurt = 1
    lingo.score = 0
    lingo.naam = ""
    timer.reset()
    
def handle_sluit(event):
    sluit.set()
    thread.join()
    window.quit()    



def validate(event):
    #pak de naam uit naamveld
    lingo.naam = naamVeld.get()
    print(lingo.naam)
    #print debug
    print("woord: " + lingo.woord)
    print("beurt: "+ str(lingo.beurt))
    print("ingevoerd: " + invoervelden[lingo.beurt-1].get())
    #pak de invoer uit het veld
    invoer = invoervelden[lingo.beurt-1].get()
    #run de functie validate_input om de status te bepalen en weer te geven
    status = lingo.validate_input(invoer)
    statusLabel["text"] = status

    #aanpassen van de kleur van statuslabel
    if status != "Voer een 5 letter woord in!":
        invoervelden[lingo.beurt-2].insert("end", " > " + status)

    if status == "Voer een 5 letter woord in!":
        statusLabel["fg"] = "red"
    elif status == "Je hebt het goed geraden!":
        statusLabel["fg"] = "green"
    else:
        statusLabel["fg"] = "#3366cc"

    #beurt bepalen en weergeven
    if lingo.beurt < 6:
        beurtLabel["text"] = str(lingo.beurt) + "/5"
    else:
        statusLabel["fg"] = "red"
        statusLabel["text"] = "Het juiste woord was " + lingo.woord

    if status == "Je hebt het goed geraden!" or status == "Het juiste woord was " + lingo.woord:
        #laat resultaat zien
        resultFrame.pack()
        gameFrame.pack_forget()
        #laat status zien
        eindLabel["text"] = status
        #laat verstreken tijd zien
        tijd = timer.get_elapsed_s()
        print(tijd)
        tijdLabel["text"] = timer.get_elapsed_time()

        #laat score zien
        if status == "Je hebt het goed geraden!":
            resultaatLabel["text"] = "Uw score is "+ str(lingo.beurt-1)
            score = HighScores()
            behaaldeScore = (lingo.beurt-1) * tijd
            score.add_entry(lingo.naam, str(behaaldeScore))      

    
window = tk.Tk()
window.title("Lingo")
window.geometry("300x400")
window.resizable(False, False)

gameFrame = tk.Frame()
gameFrame.pack()

resultFrame = tk.Frame()

welkomLabel = tk.Label(gameFrame, text="Welkom bij LINGO", font=("Arial", 18, "bold"))
welkomLabel.pack()

uitlegLabel = tk.Label(gameFrame, text="Raad het 5 letter woord in 5 beurten", font=("Arial", 10, "italic"))
uitlegLabel.pack()

naamLabel = tk.Label(gameFrame, text="voer hier onder je naam in", font=("Arial", 10,))
naamLabel.pack()

naamVeld = tk.Entry(gameFrame, bg="grey", justify="left", font=("arial", 12, "bold"), fg="white")
naamVeld.pack()
naamVeld.bind("<Return>", naam)

statusLabel = tk.Label(gameFrame, text="Succes!", font=("Arial", 14, "bold"), fg="green")
statusLabel.pack()

beurtLabel = tk.Label(gameFrame, text="1/5", font=("Arial", 18, "bold"))
beurtLabel.pack()

timerLabel = tk.Label(gameFrame, text="00", font=("Arial", 18, "italic"))
timerLabel.pack()

resultaatLabel = tk.Label(resultFrame, text="" , font=("Arial", 20, "bold"), fg="green")
resultaatLabel.pack()

eindLabel = tk.Label(resultFrame, text="", font=("Arial", 14, "bold"), fg="green")
eindLabel.pack()

tijdLabel = tk.Label(resultFrame, text="", font=("Arial", 14, "bold"), fg="green")
tijdLabel.pack()


clear = tk.Button(resultFrame, text="clear")
clear.pack()
clear.bind("<Button-1>", handle_clear)

sluit = tk.Button(resultFrame, text="Exit")
sluit.pack()
sluit.bind("<Button-1>", handle_sluit)

#invoervelden aanmaken
for veld in range(5):
    invoerVeld = tk.Entry(gameFrame, bg="#3366cc", justify="left", font=("arial", 24, "bold"), fg="white")
    invoerVeld.pack()
    invoervelden[veld] = invoerVeld
    invoerVeld.bind("<Return>", validate)

sluit = Event()

#aanmaken thread om timer gelijk te runnen met programma
thread = Thread(target=run_timer, args=(sluit,))
thread.start()


window.mainloop()