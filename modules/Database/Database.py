from pymongo import MongoClient
import datetime

class Database:
    def __init__(self):
        self.client = MongoClient()
        self.users_db = self.client['users']
        self.words_db = self.client['words']
        self.history_db = self.client['history']

        self.dbs = {
            'words': self.words_db,
            'users': self.users_db,
        }

        self.current_module = None
        self.current_option = None
        self.all = False

    def get_full_words(self, id, skip, count):
        return [el for el in self.words_db[f'{id}'].find({}).skip(skip).limit(count).sort([('languages.src', 1)])]
    def prepare_data(self, start, stop, id):
        collection = self.words_db[id]

        return collection.find({}).skip(start).limit(stop).sort([('languages.src', 1)])

    def add_one_to_voc(self, word_obj, message, module=None):
        #insert user object into current user collection
        if f'{message.chat.id}' not in self.words_db.list_collection_names():
            current_user_data_collection = self.users_db[f'{message.chat.id}']
            current_user_data_collection.insert_one(
                {
                    'first_name': message.chat.first_name,
                    'last_name': message.chat.last_name,
                    'username': message.chat.username,
                    'auth_datetime': datetime.datetime.now()
                }
            )

        #word_obj['values']['src'] = word_obj['values']['src'].lower()
        #word_obj['values']['dest'] = word_obj['values']['dest'].lower()

        #change module to current
        word_obj['module'] = self.current_module

        #connect to current user words collection by id
        current_user_words_collection = self.words_db[f'{message.chat.id}']

        #insert word object
        current_user_words_collection.insert_one(word_obj)

    def get_current_words(self, id, skip, count, m=None):
        current_collection = self.words_db[f'{id}']
        print(len([el for el in current_collection.find({'module': m}).skip(skip).limit(count).sort([('languages.src', 1)])]))
        return [el for el in current_collection.find({'module': m}).skip(skip).limit(count).sort([('languages.src', 1)])]

    '''def create_module(self, message):
        back_from_module_creating_keyboard = types.InlineKeyboardMarkup()
        back_from_module_creating_keyboard.add(types.InlineKeyboardButton('back', callback_data='back_from_module_creating'))
        bot.send_message(message.chat.id, 'module must include at least 1 word, please input it:', reply_markup=back_from_module_creating_keyboard)

        self.modules_db[f'{message.chat.id}'].insert_one(self.tr.create_object(message.text))
'''

    def collection_length(self, id, module=None, all=False):
        if all:
            return self.words_db[f'{id}'].find().count()
        else:
            return self.words_db[f'{id}'].find({'module': module}).count()

    def is_unique(self, id, word, module=None, all=False):
        print(1)
        if all:
            return True if not [el for el in self.words_db[f'{id}'].find({"$or": [{'values.src': word.lower()}, {'values.dest': word.lower()}]})] else False
        else:
            return True if not [el for el in self.words_db[f'{id}'].find({'module': module, "$or": [{'values.src': word.lower()}, {'values.dest': word.lower()}]})] else False

    def is_unique_module(self, id, module=None):
        return True if not [el for el in self.words_db[f'{id}'].find({'module': module})] else False

    def current_db_queries(self, db, skip, count):
        temp = []
        buttons = []
        for i in range(skip, count + skip):
            print(i)
            temp.append(f'types.InlineKeyboardButton({i + 1}, callback_data="{i + 1}_{db}")')
            if (i + 1) % 5 == 0 or (i + 1) == count + skip:
                buttons.append(temp)
                temp = []
        return buttons

    def add_to_the_module(self, id, word_obj, module=None, from_input=False):
        if from_input:
            pass
        else:
            self.words_db[f'{id}'].update_one({'$or': [{'values.src': word_obj['values']['src'].lower()}, {'values.dest': word_obj['values']['dest'].lower()}]}, {'$set': {'module': module}})

    def is_word_not_in_module(self, id, word):
        return True if [el for el in self.words_db[f'{id}'].find({'module': None, "$or": [{'values.src': word.lower()}, {'values.dest': word.lower()}]})] else False

    def i(self):
        self.words_db['580125422'].insert({'values': {'src': 'cake', 'dest': 'торт'}, 'module': 'food'})

    def is_exists(self, id):
        pass

    def get_all_modules(self, id):
        return list(set([el['module'] for el in self.words_db[f'{id}'].find({}) if el['module'] is not None]))

    def rename_modules_with_name(self, id, old, new):
        print(old, new)
        self.words_db[f'{id}'].update_many({'module': old}, {'$set': {'module': new}})

    def delete_module(self, id, module):
        self.words_db[f'{id}'].update_many({'module': module}, {'$set': {'module': None}})

    def get_all_module_words(self, id, module):
        return [el for el in self.words_db[str(id)].find({'module': module})]

    def insert_stats(self, id, history):
        self.history_db[str(id)].insert_one({'datetime': datetime.datetime.now(), 'results': history})

    def is_vocabulary_permeability(self, id):
        return True if 'words' in [el['name'] for el in self.client.list_databases()] and self.words_db[f'{id}'].count() != 0 else False

    def alter_word(self, id, old_word_obj, new_string):
        self.words_db[f'{id}'].update_one({'values.src': old_word_obj['values']['src']}, {'$set': {'values.src': new_string.split('-')[0], 'values.dest': new_string.split('-')[-1]}})

    def delete_word_from_module(self, id, word_obj):
        self.words_db[f'{id}'].update({'values.src': word_obj['values']['src']}, {'$set': {'module': None}})

    def is_vocabulary_empty(self, id):
        return True if not self.words_db[f"{id}"].count() != 0 else False