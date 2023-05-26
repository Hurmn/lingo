import tkinter as tk
from lingo import Lingo

lingo = Lingo("hoger")

invoervelden = {}

def validate(event):
    print("beurt: " + lingo.woord)
    print("woord: "+ str(lingo.beurt))
    print("ingevoerd: " + invoervelden[lingo.beurt-1].get())
    invoer = invoervelden[lingo.beurt-1].get()
    lingo.validate_input(invoer)


window = tk.Tk()
window.title("Lingo")
window.geometry("300x400")
window.resizable(False, False)


welkomLabel = tk.Label(window, text="Welkom bij LINGO", font=("Arial", 18, "bold"))
welkomLabel.pack()

uitlegLabel = tk.Label(window, text="Raad het 5 letter woord in 5 beurten", font=("Arial", 10, "italic"))
uitlegLabel.pack()

statusLabel = tk.Label(window, text="Succes", font=("Arial", 14, "bold"), fg="green")
statusLabel.pack()

beurtLabel = tk.Label(window, text="1/5", font=("Arial", 18, "bold"))
beurtLabel.pack()

for veld in range(5):
    invoerVeld = tk.Entry(window, bg="#3366cc", justify="left", font=("arial", 24, "bold"), fg="white")
    invoerVeld.pack()
    invoervelden[veld] = invoerVeld
    invoerVeld.bind("<Return>", validate)

window.mainloop()