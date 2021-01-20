from pymongo import MongoClient
from modules.Translator.Translator import Translator
t = Translator()

c = MongoClient()

db = c['words']

col = db['580125422']

col.insert_one(t.create_object())