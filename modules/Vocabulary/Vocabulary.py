from modules.Translator.Translator import Translator
from modules.Database.Database import Database
from config.config import bot_object as bot
from telebot import types

db = Database()

class Vocabulary:
    def __init__(self):
        self.current_ten = None
        self.current_voc_obj = None
        self.db = Database()

    def is_from_navigation(self, data):
        try:
            int(data)
        except:
            return False
        else:
            return True

    def send_full_word(self, id, word_obj):
        print(word_obj)
        bot.send_message(id, f"{word_obj['values']['src']} - {word_obj['values']['dest']}")
        bot.send_message(id,
                         f'{", ".join(word_obj["syntax"]["src"]["synonyms"]) if word_obj["syntax"]["src"]["synonyms"] != None else None} - {", ".join(word_obj["syntax"]["dest"]["synonyms"]) if word_obj["syntax"]["dest"]["synonyms"] != None else None}')
        bot.send_voice(id, word_obj['audio']['src'])
        bot.send_voice(id, word_obj['audio']['dest'])