from modules.Database.Database import Database
from telebot import types
from config.config import bot_object as bot

class Admin:
    def __init__(self):
        self.db = Database()

    def send_applications(self, message):


        buttons = [f'types.InlineKeyboardButton("{el["name"]}", callback_data="{el["name"]}_application")' for el in self.db.applications_db['applications'].find()]

        for application in [el['name'] for el in self.db.applications_db['applications'].find()]:
            print(application)
            applications_accept_keyboard = types.InlineKeyboardMarkup()
            applications_accept_keyboard.add(types.InlineKeyboardButton('accept', callback_data=f'{application}_applicationaccept'), types.InlineKeyboardButton('reject', callback_data=f'{application}_applicationreject'))
            bot.send_message(message.chat.id, application, reply_markup=applications_accept_keyboard)