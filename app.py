from entry import Entry
from db_boss import DBManager
import sqlite3
import pandas as pd


currentDB = DBManager()

def user_add_to_db():
    input_loop = True
    while input_loop:
        try:
            w, x, y, z = input("New entry? Enter title"
                               "/language/attempts/wins: ").split()
            y = int(y)
            z = int(z)
            input_loop = False
        except:
            print("Need 4 values")
            continue
    DBManager.place_data_in_db(w, x, y, z)
    currentEntry = Entry(w, x, y, z)
    print("Database updated")
    print(currentEntry)

def get_value_from_db():
    title_to_fetch = input("What algorithm are you searching for?: ")

    DBManager.get_value_by_title(title_to_fetch, validate_user_preference)


def validate_user_preference():
    input_loop = True
    user_preference = input("Do you wish to perform a CRUD method to the db or just see whats in the db? (crud/db): ")
    if user_preference == "crud":
        crud_letter = specify_which_crud_user_wants(input_loop)
        perform_CRUD(crud_letter)
    if user_preference == "db":
        connection = sqlite3.connect("data.db")
        data = pd.read_sql_query("SELECT * FROM entries",connection)
        print("Here are the results")
        print(data)
        connection.close()

def specify_which_crud_user_wants(input_loop):

    while input_loop:
        crud_letter = input("Which method? (c r u d)?: ")
        if crud_letter == "c" or crud_letter == "r" or crud_letter == "u" or crud_letter == "d":
            input_loop = False
            return crud_letter
        else:
            print("Invalid input")
            continue

def perform_CRUD(letter):
    if letter == "c":
        return user_add_to_db()
    if letter == "r":
        get_value_from_db()
        



def run_app():
    validate_user_preference()





if __name__ == '__main__':
    print(Entry.find_entry_by_title("hello world"))
    run_app()
