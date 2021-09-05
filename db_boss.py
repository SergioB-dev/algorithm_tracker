import sqlite3
import os


class DBManager:
    def __init__(self, name="data.db"):
        self.name = name

    def createDB(self):
        if os.path.exists("./" + self.name):
            return
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()

        create_table = "CREATE TABLE entries(title text, language text, attempts int, wins int)"
        cursor.execute(create_table)
        connection.close()
    @classmethod
    def place_data_in_db(cls, title, language, attempts, wins):
        entry = (title, language, attempts, wins)

        query = "INSERT INTO entries VALUES(?,?,?,?)"

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute(query, (entry))

        connection.commit()
        connection.close()

    def getAll(self):
        entries = []
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()

        query = "SELECT * FROM entries"
        results = cursor.execute(query)
        if results:
            for entry in results:
                entries.append(entry)
        return {"entries": entries }

        connection.close()

try1 = DBManager()
try1.place_data_in_db(title="x", language="", attempts=1, wins=0)

