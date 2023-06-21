import sqlite3
import datetime

class HighScores:
    def __init__(self):
        #controleren of tabel bestaat + aanmaken
        self.create_table()

    def create_table(self):
        #connectie maken
        connection = sqlite3.connect("lingo.sqlite3")
        cursor = connection.cursor()
        #uitvoeren statement
        cursor.execute("""CREATE TABLE IF NOT EXISTS highscores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
            );""")
        connection.close()

    def add_entry(self, name, score):
        #score toevoegen aan tabel
        print("add score, name " + name + ", score " + score)
        connection = sqlite3.connect("lingo.sqlite3")
        cursor = connection.cursor()
        query = "INSERT INTO highscores(name, score) VALUES (?, ?); "
        cursor.execute(query, (name, score))
        connection.commit()
        connection.close()

    def get_list(self):
        pass