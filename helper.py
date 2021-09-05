from flask_restful import Resource
from entry import Entry
import json

class Helper(Resource):
    def __init__(self, **kwargs):
        self.title = kwargs["title"]

    def get(self, title):
        entry = Entry.find_entry_by_title(title)
        if entry:
            return json.dumps(entry.__dict__)
        else:
            return None
