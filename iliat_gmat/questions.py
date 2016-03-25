__author__ = 'qhuydtvt'

from mongoengine import *
from answer_choices import AnswerChoice

class Question(Document):
    type = StringField()
    sub_type = StringField()
    stimulus = StringField()
    stem = StringField()
    answer_choices = ListField(EmbeddedDocumentField('AnswerChoice'))
    right_answer = IntField()

    @classmethod
    def to_formatted_json(cls, question_list):
        json_list = [question.to_json(sort_keys=True, indent= 4 * "&nbsp",
                                          separators=(',', ': ')) for question in question_list]
        return str.format("[<br>{0}<br>]",
                      (",<br>".join(json_list)).replace("\n", "<br>"))

class QuestionCollection(Document):
    version = StringField()
    questions = ListField(EmbeddedDocumentField('Question'))


    # def get_json(self, json_encoder):
    #     return json_encoder.encode(self.to_mongo())

# def from_questions_to_json_string(question_list):
#     # json_encoder = JSONEncoder()
#     json_list = [question.to_json(sort_keys=True, indent= 4 * "&nbsp", separators=(',', ': ')) for question in question_list]
#     # return str.format('{0}: [<br>' +  + '<br>]')
#     return str.format("{0} : [<br>{1}<br>]", QUESTION_KEY,
#                       (",<br>".join(json_list)).replace("\n", "<br>"))
        # .replace(" ", "&nbsp")

# def from_json_to_string(json_object):
#     print(json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': ')))
#     return json.dumps(json_object, sort_keys=True, indent=4, separators=(',', ': '))