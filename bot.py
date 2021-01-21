from config.config import bot_object as bot
from modules.Translator.Translator import Translator
from telebot import types
from modules.Database.Database import Database
from modules.Vocabulary.Vocabulary import Vocabulary
from modules.Module.Module import Module
import random
import telebot
import time

db = Database()
voc = Vocabulary()
module = Module()

skip = 0
count = 0


main_keyboard = types.ReplyKeyboardMarkup()

main_keyboard.add(types.KeyboardButton('translate'), types.KeyboardButton('my vocabulary'))
main_keyboard.add(types.KeyboardButton('new module'), types.KeyboardButton('manage modules'))
teachers_keyboard = types.ReplyKeyboardMarkup()
teachers_keyboard.add(types.KeyboardButton(''))


trans = Translator()

@bot.message_handler(commands=['start', 'help', 'translate', 'test', 'forteachers'])
def get_command(message):
    if message.text == '/translate':
        pass
    elif message.text == '/start':
        bot.send_message(message.chat.id, 'lets learn new words!', reply_markup=main_keyboard)
    elif message.text == '/test':
        print(module.stats)
    elif message.text == '/forteachers':
        pass

@bot.message_handler(content_types=['text'])
def get_text_command(message):
    global skip
    global count

    if message.text == 'translate':
        bot.send_message(message.chat.id, 'im waiting for your word:')
        bot.register_next_step_handler(message, trans.send_word)
    elif message.text == 'my vocabulary':
        print(str(id))
        print(str(message.chat.id) not in db.words_db.collection_names())
        if str(message.chat.id) not in db.words_db.collection_names():
            bot.send_message(message.chat.id, 'your vocabulary is empty')
        else:
            #switch on your own vocabulary database
            module.current_module = None
            db.all = True
            db.current_option = 'None'

            skip = 0
            count = 10
            module.send_current_ten(message.chat.id, skip, count, module=db.current_module, option=db.current_option, all=db.all)
            print(db.is_unique(message.chat.id, 'carpet'))

    elif message.text == 'try knowledge':
        pass
    elif message.text == 'manage modules':
        print(1)
        if not db.collection_length(message.chat.id, all=True) or db.collection_length(message.chat.id) == db.collection_length(message.chat.id, all=True):
            more_create_module_keyboard = types.InlineKeyboardMarkup()
            more_create_module_keyboard.add(types.InlineKeyboardButton('create new module', callback_data="more_create_module"))
            bot.send_message(message.chat.id, 'there are no new modules', reply_markup=more_create_module_keyboard)
        else:
            module.send_all_modules(message.chat.id)

    elif message.text == 'new module':
        bot.send_message(message.chat.id, 'enter module name')
        bot.register_next_step_handler(message, module.send_choice)

@bot.callback_query_handler(func=lambda call: True)
def get_query(query):
    global skip
    global count
    if query.data == 'more_create_module':
        bot.send_message(query.message.chat.id, 'enter module name')
        bot.register_next_step_handler(query.message, module.send_choice)
    if query.data.split('_')[-1] == 'None':
        #db.current_module = query.data.split('_')[1]
        voc.send_full_word(query.message.chat.id, module.current_ten[(int(query.data.split('_')[0]) % 10) - 1])
    elif query.data.split('_')[-1] == 'firstinsertfromvocabulary':
        print('what module', module.module_name)
        print(query.data)
        #print(voc.current_ten)
        word_number = int(query.data.split('_')[0])
        module.add_to_the_module(query, word_number)

    elif query.data == 'add_to_voc':
        if db.is_unique(query.message.chat.id, trans.current_word_obj['values']['src'], module=module.current_module, all=True):
            db.add_one_to_voc(trans.current_word_obj, query.message, module=module.current_module)
            bot.answer_callback_query(callback_query_id=query.id, text='word added')
        else:
            bot.send_message(query.message.chat.id, 'word already there')

    elif query.data == 'next_list':
        print('skip', skip)
        print('count', count)

        if (skip + count) > db.collection_length(query.message.chat.id, module=module.current_module, all=db.all):
            bot.send_message(query.message.chat.id, 'that is all')
        elif db.collection_length(query.message.chat.id, module=module.current_module, all=db.all) - (skip + count) < count:
            skip += count
            module.send_current_ten(query.message.chat.id, skip, db.collection_length(query.message.chat.id, module=module.current_module, all=db.all) - (skip), module=module.current_module, option=db.current_option, all=db.all)

    elif query.data == 'previous_list':
        if skip - 10 < 0:
            skip = 0
            bot.send_message(query.message.chat.id, 'you are on already first page')
        else:
            skip -= 10
            module.send_current_ten(query.message.chat.id, skip, count, module=module.current_module, option=db.current_option, all=db.all)

    elif query.data == 'insert_first_word_from_voc':
        print(db.is_vocabulary_permeability(query.message.chat.id))
        print('ooooooo')
        if db.is_vocabulary_permeability(query.message.chat.id):
            #switch on mosules database
            #module.module_name = None
            db.current_option = 'firstinsertfromvocabulary'
            db.all = True

            print(db.current_module)
            skip = 0
            count = 10
            module.send_current_ten(query.message.chat.id, skip, count, module=module.current_module, option=db.current_option, all=db.all)
        else:
            bot.send_message(query.message.chat.id, 'your vocabulary is empty')

    elif query.data == 'input':
        bot.send_message(query.message.chat.id, 'enter the word:')
        bot.register_next_step_handler(query.message, module.add_from_input)

    elif query.data.split('_')[-1] == 'rename':
        module.old_module_name = query.data.split('_')[0]
        bot.send_message(query.message.chat.id, 'enter the new module name:')
        bot.register_next_step_handler(query.message, module.rename_module)

    elif query.data.split('_')[-1] == 'edit':
        module.current_module = query.data.split('_')[0]
        module.module_name = module.current_module
        db.current_option = 'editword'
        skip = 0
        count = 10
        module.send_current_ten(query.message.chat.id, skip, count, module=module.current_module, option=db.current_option, edit=True)

    elif query.data.split('_')[-1] == 'editword':
        '''        if edit:
            navigation_keyboard.add(types.InlineKeyboardButton('delete', callback_data='delete_current_word'), types.InlineKeyboardButton('add', callback_data='add_new_word'))
            navigation_keyboard.add(types.InlineKeyboardButton('alter', callback_data='alter_word'))'''
        module.current_word_index = int(query.data.split('_')[0]) - 1
        functionality_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('delete', callback_data='delete_current_word'), types.InlineKeyboardButton('alter', callback_data='alter_word'))
        bot.send_message(query.message.chat.id, '.', reply_markup=functionality_keyboard)

    elif query.data.split('_')[-1] == 'delete':
        db.delete_module(query.message.chat.id, query.data.split('_')[0])
        bot.send_message(query.message.chat.id, f'module with name {query.data.split("_")[0]} was deleted')

    elif len(query.data.split("_")) == 3 and query.data.split('_')[-1] == 'show':
        print('AAAAAAAA', query.data)
        print(module.current_ten[(int(query.data.split('_')[0]) % 10) - 1])
        voc.send_full_word(query.message.chat.id, module.current_ten[(int(query.data.split('_')[0]) % 10) - 1])

    elif query.data.split('_')[-1] == 'show':
        print('adasdasdasd', query.data)
        skip = 0
        count = 10
        module.current_module = query.data.split('_')[0]
        module.send_current_ten(query.message.chat.id, skip, count, module=module.current_module, option="show")

    elif query.data.split('_')[-1] == 'try':
        module.learn_history = []
        module.current_learning_module = query.data.split('_')[0]
        module.learning_word = 0
        module.current_learning_words = db.get_all_module_words(query.message.chat.id, module.current_learning_module)
        module.stats['correct_count'] = 0
        module.stats['whole_count'] = len(module.current_learning_words)

        module.learn_word(query.message)
    elif query.data.split('_')[-1] == 'answer':
        if query.data.split('_')[0] == module.current_learning_words[module.learning_word]['values']['dest']:
            module.stats['correct_count'] += 1
            module.chose_truth_answer(query.message, correct=True)
        else:
            module.chose_truth_answer(query.message, correct=False)

    elif query.data == 'next_learning_word':
        module.learning_word += 1
        module.learn_word(query.message)

    elif query.data == 'alter_word':
        module.logic_alter_word(query.message)

    elif query.data == 'delete_last_word_from_module_confident':
        db.delete_word_from_module(query.message.chat.id, module.current_ten[module.current_word_index])
        bot.send_message(query.message.chat.id, f'word ***{module.current_ten[module.current_word_index]["values"]["src"]} - {module.current_ten[module.current_word_index]["values"]["dest"]}*** which was single in this module deleted, then was deleted this module', parse_mode='Markdown')
    elif query.data == 'delete_current_word':
        if len(module.current_ten) == 1:
            bot.send_message(query.message.chat.id, 'module has 1 word, so if you delete that module will be deleted', reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('are you sure?', callback_data='delete_last_word_from_module_confident')))
        else:
            db.delete_word_from_module(query.message.chat.id, module.current_ten[module.current_word_index])
            bot.send_message(query.message.chat.id, f'word ***{module.current_ten[module.current_word_index]["values"]["src"]} - {module.current_ten[module.current_word_index]["values"]["dest"]}*** was deleted', parse_mode='Markdown')

    elif query.data == 'add_new_word':
        module.logic_add_new_word_to_module(query.message)

    elif query.data == 'view_results':
        db.insert_stats(query.message.chat.id, module.learn_history)
        module.send_stats(query.message.chat.id)

    elif query.data == 'add_new_word_from_vocabulary':
        if db.is_vocabulary_permeability(query.message.chat.id):
            db.current_option = 'add'
            db.all = True

            print(db.current_module)
            skip = 0
            count = 10
            module.send_current_ten(query.message.chat.id, skip, count, module=module.current_module, option=db.current_option, all=db.all)
        else:
            bot.send_message(query.message.chat.id, 'your vocabulary is empty')

    elif query.data.split('_')[-1] == 'add':
        print(query.data.split('_')[0])
        print('asdadads', query.data)
        module.add_to_the_module(query, int(query.data.split('_')[0]))
    elif query.data == 'add_new_word_from_input':
        bot.send_message(query.message.chat.id, 'enter the word:')
        bot.register_next_step_handler(query.message, module.add_from_input)

    elif query.data == 'stop':
        bot.send_message(query.message.chat.id, 'are you sure? if you accept, your progress will be not saved', reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('im sure', callback_data='sureness')))
    elif query.data == 'sureness':
        bot.send_message(query.message.chat.id, 'stopped')

bot.polling()