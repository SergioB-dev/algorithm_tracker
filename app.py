from flask import Flask
from flask_restful import Api
from entry import Entry
from helper import Helper
from db_boss import DBManager


app = Flask(__name__)
app.secret_key = "xyz"
api = Api(app)
currentDB = DBManager()

api.add_resource(Helper, "/entry/<string:title>", resource_class_kwargs={"title":""})

@app.route("/", methods=["GET"])
def getAll():
    return currentDB.getAll()

# entry1 = Entry("two-sum")
# entry1.record_attempts_and_wins(3, 1)
#
# print(entry1)
# print(entry1.percentage)
# print(entry1.attempt_count)
print(Entry.find_entry_by_title("hello world"))




if __name__ == '__main__':
    app.run(debug=True)
