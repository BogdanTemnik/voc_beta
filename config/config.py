import telebot
from modules.Database.Database import Database
from pymongo import MongoClient

db = Database()

TOKEN = '1401690541:AAFOAOKMsLfKP0p1r3e9do-NWEz9GWKdSRE'

parts_of_speech = {'CC': 'coordinating conjunction', 'CD': 'cardinal digit', 'DT': 'determiner', 'EX': 'existential there', 'FW': 'foreign word', 'IN': 'preposition/subordinating conjunction', 'JJ': 'adjective', 'VP': 'Verb Phrase', 'JJR': 'adjective, comparative', 'JJS': 'adjective, superlative', 'LS': 'list marker', 'MD': 'modal', 'NN': 'noun, singular', 'NNS': 'noun plural', 'PP': 'Preposition Phrase', 'NNP': 'proper noun, singular', 'NNPS': 'proper noun, plural', 'PDT': 'predeterminer', 'POS': 'possessive ending', 'PRP': 'personal pronoun', 'PRP$': 'possessive pronoun', 'RB': 'adverb', 'RBR': 'adverb, comparative', 'RBS': 'adverb, superlative', 'RP': 'particle', 'TO': 'to go', 'UH': 'interjection', 'VB': 'verb, base form', 'VBD': 'verb, past tense', 'VBG': 'verb, gerund/present participle', 'VBN': 'verb, past participle', 'VBP': 'verb, sing. present, non-3d', 'VBZ': 'verb, 3rd person sing. present', 'WDT': 'wh-determiner', 'WP': 'wh-pronoun', 'WP$': 'possessive wh-pronoun', 'WRB': 'wh-abverb'}

teachers = [580125422]

modules_methods = ['rename', 'add', 'edit', 'delete']

bot_object = telebot.TeleBot(TOKEN)