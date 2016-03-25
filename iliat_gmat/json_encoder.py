__author__ = 'qhuydtvt'

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            print("ObjectId")
            return str(o["$oid"])
        return json.JSONEncoder.default(self, o)