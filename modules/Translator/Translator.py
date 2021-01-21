from googletrans import Translator as tr
from config.config import bot_object as bot, parts_of_speech
from gtts import gTTS
from telebot import types
from deep_translator import GoogleTranslator
from nltk.tokenize import word_tokenize
from PyDictionary import PyDictionary
import nltk
import enchant
from modules.Database.Database import Database
import langdetect
from textblob import TextBlob

db = Database()

class Translator:
    def __init__(self):
        self.translator = tr()
        self.current_word_obj = ''
        self.dictionary = PyDictionary()

    def cldir(self, path):
        import os
        if os.listdir(path) != []:
            for item in os.listdir(path):
                os.remove(path + '/' + item)

    def word_checker(self, word):
        if self.dictionary.synonym(word) == None:
            return False
        return True

    def get_binary(self, word, source_='ru', destination_='en'):
        from_src_to_dest = GoogleTranslator(source=source_, target=destination_)
        self.cldir('cache')
        gTTS(text=from_src_to_dest.translate(word), lang=destination_).save('cache/word.wav')
        return open('cache/word.wav', 'rb').read()

    def create_object(self, id, word, source='ru', destination='en'):
        from_src_to_dest = GoogleTranslator(source=source, target=destination)
        from_dest_to_src = GoogleTranslator(source=destination, target=source)

        print(word, self.word_checker(word))
        #print(from_src_to_dest.translate(word), self.word_checker(from_src_to_dest.translate(word)))

        try:
            return {
            'is_learnt': False,
            'module': None,
            'teacher': None,
            'values': {
                'src': word.lower(),
                'dest': from_src_to_dest.translate(word).lower()
            },
            'languages': {
                'src': source,
                'dest': destination
            },
            'audio':
                {
                    'dest': self.get_binary(word, source_=source, destination_=destination) if word else None,
                    'src': self.get_binary(word, source_=destination, destination_=source) if word else None

                },
            'syntax': {
                'src': {
                    'part of speech': None if len(word_tokenize(word)) > 1 else (parts_of_speech[nltk.pos_tag(word_tokenize(word))[-1][1]] if source == 'en' else from_dest_to_src.translate(parts_of_speech[nltk.pos_tag(word_tokenize(from_src_to_dest.translate(word)))[-1][1]])),
                    'synonyms': None if len(word_tokenize(word)) > 1 or (not self.word_checker(word) and not self.word_checker(from_src_to_dest.translate(word))) else (self.dictionary.synonym(word)[:3] if source == 'en' else [from_dest_to_src.translate(el) for el in self.dictionary.synonym(from_src_to_dest.translate(word))[:3]])
                },
                'dest': {
                    'part of speech': None if len(word_tokenize(word)) > 1 else (parts_of_speech[nltk.pos_tag(word_tokenize(word))[-1][1]] if destination == 'en' else from_src_to_dest.translate(parts_of_speech[nltk.pos_tag(word_tokenize(from_dest_to_src.translate(word)))[-1][1]])),
                    'synonyms': None if len(word_tokenize(word)) > 1 or (not self.word_checker(word) and not self.word_checker(from_src_to_dest.translate(word))) else (self.dictionary.synonym(from_src_to_dest.translate(word))[:3] if destination == 'en' else [from_src_to_dest.translate(el) for el in self.dictionary.synonym(word)[:3]])
                }
            }
        }
        except:
            bot.send_message(id, 'text length need to be between 1 and 5000 characters')


    def send_word(self, message):

        # create inline keyboard
        add_to_vocab = types.InlineKeyboardMarkup()
        add_to_vocab.add(types.InlineKeyboardButton('add to vocabluary', callback_data='add_to_voc'))
        try:
            if TextBlob(message.text).detect_language() != 'en':
                print('185')
                #create word object
                word_obj = self.create_object(message.chat.id, message.text, source='ru', destination='en')

                print(db.is_unique(message.chat.id, message.text.lower()))
                self.current_word_obj = word_obj

                print(word_obj)

                # send translate
                bot.send_message(message.chat.id, word_obj['values']['dest'])

                #send pronunciation
                bot.send_voice(message.chat.id, word_obj['audio']['dest'], reply_markup=add_to_vocab)
            else:
                import datetime
                now = datetime.datetime.now()
                # create word object
                word_obj = self.create_object(message.chat.id, message.text, source='en', destination='ru')

                creating_time = datetime.datetime.now() - now
                print(creating_time)

                self.current_word_obj = word_obj

                #send translate
                bot.send_message(message.chat.id, word_obj['values']['dest'])

                #send pronunciation
                bot.send_voice(message.chat.id, word_obj['audio']['dest'], reply_markup=add_to_vocab)
        except Exception as e:
            print(e)

