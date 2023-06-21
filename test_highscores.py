from highscores import HighScores
import sqlite3

#maken tabel5
scores = HighScores()

#toevoegen van score
scores.add_entry("Harmen", 100)

# connection = sqlite3.connect('lingo.sqlite3')
# cursor = connection.cursor()
# cursor.execute("DROP TABLE highscores; ")
# connection.close()