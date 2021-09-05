import sqlite3

class Entry:

    def __init__(self, title, language="Python", attempts=0,wins=0):
        self.title = title
        self.language = language
        self.attempts = attempts
        self.wins = wins


    def __repr__(self):
        return "You have worked on {} {} time(s) in total.\n" \
               " You have a {:.0%} win pct. " \
               "".format(self.title, self.attempts, self.percentage)


    def record_attempts_and_wins(self, a, w=0):
        if w > a:
            raise Exception("Wins cannot exceed attempts")

        self.attempts += a
        self.wins += w

    @classmethod
    def find_entry_by_title(cls, title):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM entries WHERE title=?"
        result = cursor.execute(query, (title,))
        column = result.fetchone()
        if column:
            entry = cls(*column)
        else:
            entry = None

        connection.close()
        return entry


    @property
    def percentage(self):
        return self.wins / self.attempts

    @property
    def attempt_count(self):
        return self.attempts

