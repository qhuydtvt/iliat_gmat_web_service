__author__ = 'qhuydtvt'

from mongoengine import *

class Version(Document):
    value = StringField()
