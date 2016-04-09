from flask import Flask

from questions import Question, QuestionCollection
from versions import Version
from question_packs import QuestionPack, QuestionPackCollection
import mongoengine


host = "ds011840.mlab.com"
port = 11840
db_name = "gmat"
user_name = "admin"
password = "admin"

mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

app = Flask(__name__)

def remove_dollar_sign(s):
    OLD_OID = "$oid"
    NEW_OID = "oid"
    return s.replace(OLD_OID, NEW_OID)

@app.route('/')
def hello_world():
    return "Iliat GMATers, don't panic!"


@app.route('/api/question_collection')
@app.route('/api/questions')
def get_gmat_question_collection():
    questions = Question.objects
    version = Version.objects[0]
    question_collection = QuestionCollection(version=version.value, questions=questions)
    return remove_dollar_sign(str(question_collection.to_json()))

@app.route('/api/question_pack_collection')
@app.route('/api/question_packs')
def get_gmat_question_pack_collection():
    question_packs = QuestionPack.objects
    question_pack_collection = QuestionPackCollection(question_packs = question_packs)
    return remove_dollar_sign(str(question_pack_collection.to_json()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)

