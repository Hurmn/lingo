class Lingo:
    def __init__(self, woord):
        self.woord = woord

    def validate_input(self):
        
        print([*self.woord][0].upper() + " _ _ _ _")

        for beurten in range(5):
            goedWoord = [*self.woord]
            goede_letters = [" _"," _"," _"," _"," _"]
            letter_nummer = 0
            lengte = False
            while lengte == False:
                [*invoer] = input("Wat is het woord? // ")
                if len(invoer) == 5:
                    lengte = True
            
            for letter in invoer:
                if letter == self.woord[letter_nummer]:
                    goede_letters[letter_nummer] = letter.upper()
                    goedWoord[letter_nummer] = ""
                else:
                    for letter_goedWoord in goedWoord:
                        if letter == letter_goedWoord:
                            goede_letters[letter_nummer] = letter.lower()
                            goedWoord[letter_nummer] = ""
                letter_nummer += 1

            for letter in goede_letters:
                if letter == "*":
                    letter = " _"
                else:
                    pass

            print(goede_letters)
            out = "".join(goede_letters)
            goed = out.isupper()
            if len(out) == 5 and goed == True:
                print("gefeliciteerd je hebt het goed geraden")
                break
            else:
                aantal = 5-len(out)
                under = aantal * "_ "
                print(out + under)   