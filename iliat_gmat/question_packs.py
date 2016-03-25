__author__ = 'qhuydtvt'

from mongoengine import *
from versions import Version

class QuestionPack(Document):
    available_time = StringField()
    question_ids = ListField(StringField())

class QuestionPackCollection(Document):
    version = EmbeddedDocumentField('Version')
    question_packs = ListField(EmbeddedDocumentField('QuestionPack'))

