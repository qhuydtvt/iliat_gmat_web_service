__author__ = 'qhuydtvt'

from mongoengine import *

class AnswerChoice(Document):
    index = IntField()
    choice = StringField()
    explanation = StringField()
    note = StringField()
