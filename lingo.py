class Lingo:
    def __init__(self, woord):
        self.woord = woord
        self.beurt = 1

    def validate_input(self, invoer):
        lengte = False
        #controleer dat input 5 letters is
        if len(invoer) != 5:
            print("Voer een 5 letter woord in")
            exit()
        self.beurt += 1

        #print de eerste letter van het goede woord
        print([*self.woord][0].upper() + " _ _ _ _")

        #splits het woord op in de letters
        goedWoord = [*self.woord]
        goede_letters = [" _"," _"," _"," _"," _"]
        letter_nummer = 0
        
        #controleer of de letter van invoer in het woord zit en op de goede plek zit
        for letter in invoer:
            if letter == self.woord[letter_nummer]:
                goede_letters[letter_nummer] = letter.upper()
                goedWoord[letter_nummer] = ""
            #als het niet op de goede plek staat kleine letter
            else:
                for letter_goedWoord in goedWoord:
                    if letter == letter_goedWoord:
                        goede_letters[letter_nummer] = letter.lower()
                        goedWoord[letter_nummer] = ""
            letter_nummer += 1
        #maak van de lijst een string
        out = "".join(goede_letters)
        goed = out.isupper()
        #als alles is ingevuld en alles hoofdletter is
        if len(out) == 5 and goed == True:
            print("gefeliciteerd je hebt het goed geraden")
        else:
            print(out)   