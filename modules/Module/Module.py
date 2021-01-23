from modules.Database.Database import Database
from config.config import bot_object as bot
from telebot import types
from modules.Translator.Translator import Translator
from langdetect import detect
import random
import requests
from deep_translator import GoogleTranslator
from nltk import word_tokenize
from textblob import TextBlob

class Module():
    def __init__(self):
        self.db = Database()
        self.is_first_insert = False
        self.current_module = None
        self.module_name = None
        self.tr = Translator()
        self.old_module_name = None
        self.new_module_name = None
        self.learning_word = None
        self.stats = {'correct_count': 0, 'whole_count': 0}
        self.current_learning_module = None
        self.current_learning_words = None
        self.next_learning_word_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('stop', callback_data='stop'), types.InlineKeyboardButton('>>>', callback_data='next_learning_word'))
        self.view_results_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('stop', callback_data='stop'), types.InlineKeyboardButton('view results', callback_data='view_results'))
        self.learn_history = []
        self.current_word_index = None
        self.current_words = None
        self.wrong_answers = None
        self.how_many_learnt = 0
        self.whole_count = 0

    def send_current_ten(self, id, skip, count, module=None, option=None, all=False, edit=False):
        print('option', option)
        print('skip in "func":', skip)
        print('count in "func":', count)
        if all:
            self.current_ten = self.db.get_full_words(id, skip, count)

            print('theretheretherethere')
        else:
            self.current_ten = self.db.get_current_words(id, skip, count, m=module)
            to = self.current_ten
        print('there')
        for i in self.current_ten:
            print(i)

        temp = []
        buttons = []

        for i in range(skip, len(self.current_ten) + skip):
            temp.append(f'types.InlineKeyboardButton({i +1}, callback_data="{i  +1}_{module}_{option}")')
            if (i + 1) % 5 == 0:
                buttons.append(temp)
                temp = []

        if temp:
            buttons.append(temp)

        print(buttons)

        navigation_keyboard = types.InlineKeyboardMarkup()

        # insert keyboard
        for el in buttons:
            exec(f"navigation_keyboard.row({','.join(el)})")

        navigation_keyboard.add(types.InlineKeyboardButton('<', callback_data='previous_list'), types.InlineKeyboardButton('>', callback_data='next_list'))
        if option == 'None':
            navigation_keyboard.add(types.InlineKeyboardButton('clear', callback_data='clear_vocabulary'))

        if edit:
            navigation_keyboard.add(types.InlineKeyboardButton('add', callback_data='add_new_word'))


        nums = [i for i in range(skip, len(self.current_ten) + skip + 1)]
        print(nums)
        output = [f'{skip + i + 1}) {self.current_ten[i]["values"]["src"]} - {self.current_ten[i]["values"]["dest"]}' for i in range(len(self.current_ten))]
        print('output', output)

        bot.send_message(id, '\n'.join(output), reply_markup=navigation_keyboard)

    def send_choice(self, message):
        self.module_name = message.text
        print(self.module_name)
        #print(self.current_module)
        if message.text == 'None':
            bot.send_message(message.chat.id, '"None" is keyword, you can\'t use that')

        elif self.db.is_unique_module(message.chat.id, module=self.module_name):
            print(self.db.is_unique_module(message.chat.id, module=message.text))
            choice = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('insert from vocabulary', callback_data='insert_first_word_from_voc'), types.InlineKeyboardButton('input', callback_data='input'))
            bot.send_message(message.chat.id, 'module must include at least 1 word, please insert from:', reply_markup=choice)
        else:
            bot.send_message(message.chat.id, 'module with this name is already created')

    def add_from_input(self, message):
        add_more_from_input_first_keyboard = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton('add more', callback_data='add_more_from_input_first'))
        if self.db.is_unique(message.chat.id, message.text, all=True):
            try:
                word_obj = self.tr.create_object(message.chat.id, message.text, source='ru', destination='en') if TextBlob(message.text).detect_language() != 'en' else self.tr.create_object(message.chat.id, message.text, source='en', destination='ru')
                word_obj['module'] = self.module_name

                self.db.words_db[f'{message.chat.id}'].insert_one(word_obj)

                bot.send_message(message.chat.id, f'word added', reply_markup=add_more_from_input_first_keyboard)
            except:
                bot.send_message(message.chat.id, 'unknown word', reply_markup=add_more_from_input_first_keyboard)

        else:
            bot.send_message(message.chat.id, 'word already in dictionary, you can add it from them', reply_markup=add_more_from_input_first_keyboard)


    def send_all_modules(self, id):
        modules = self.db.get_all_modules(id)
        print(modules)

        for i in range(len(modules)):
            options_keyboard = types.InlineKeyboardMarkup()
            options_keyboard.add(
                types.InlineKeyboardButton('rename', callback_data=f'{modules[i]}_rename'),
                types.InlineKeyboardButton('edit', callback_data=f'{modules[i]}_edit'),
                types.InlineKeyboardButton('delete', callback_data=f'{modules[i]}_delete'),
            )
            options_keyboard.add(types.InlineKeyboardButton('try', callback_data=f'{modules[i]}_try'), types.InlineKeyboardButton('show', callback_data=f'{modules[i]}_show'))
            bot.send_message(id, modules[i], reply_markup=options_keyboard)

    def rename_module(self, message):
        self.new_module_name = message.text
        if self.db.is_unique_module(message.chat.id, module=message.text):
            self.current_module = message.text
            self.db.rename_modules_with_name(message.chat.id, self.old_module_name, self.new_module_name)
            bot.send_message(message.chat.id, f'module "{self.old_module_name}" was renamed to "{self.new_module_name}"')
        else:
            bot.send_message(message.chat.id, f'module with name "{message.text}" is already exists')

    def input_learn(self, id, word):
        pass

    def __get_uqicues(self, count=3):
        #return [el for el in requests.get('https://random-word-api.herokuapp.com/word', params={'number': count}).text.replace('["', '').replace('"]', ',').split(',') if el]
        return requests.get('https://random-word-api.herokuapp.com/word', params={'number': count}).text.replace('["', '').replace('"]', '').split('","')

    def chose_truth_answer(self, message, correct=True):
        if correct:
            self.stats['correct_count'] += 1
            bot.send_message(message.chat.id, f'correct✅ {self.stats["correct_count"]}/{self.stats["whole_count"]}', reply_markup=self.view_results_keyboard if self.learning_word + 1 == len(self.current_learning_words) else self.next_learning_word_keyboard)
            self.learn_history.append({'type': 'choose', 'wrong_answers': self.wrong_answers, 'correct_answer': self.current_learning_words[self.learning_word]['values']['src'], 'is_correct': True})
        else:
            bot.send_message(message.chat.id, f'wrong answer❌ {self.stats["correct_count"]}/{self.stats["whole_count"]}', reply_markup=self.view_results_keyboard if self.learning_word + 1 == len(self.current_learning_words) else self.next_learning_word_keyboard)
            self.learn_history.append({'type': 'choose', 'wrong_answers': self.wrong_answers, 'correct_answer': self.current_learning_words[self.learning_word]['values']['src'], 'is_correct': False, 'obj': self.current_learning_words[self.learning_word]})

    def input_truth_answer(self, message):
        if message.text == self.current_learning_words[self.learning_word]['values']['dest'] and message.text != '\start':
            self.stats['correct_count'] += 1
            bot.send_message(message.chat.id, f'correct✅ {self.stats["correct_count"]}/{self.stats["whole_count"]}', reply_markup=self.view_results_keyboard if self.learning_word + 1 == len(self.current_learning_words) else self.next_learning_word_keyboard)
            self.learn_history.append({'type': 'input', 'correct_answer': self.current_learning_words[self.learning_word]['values']['src'], 'wrong_answer': message.text, 'is_correct': True, 'obj': self.current_learning_words[self.learning_word]})
        elif message.text == '\start':
            bot.send_message(message.chat.id, 'stoped')

        else:
            bot.send_message(message.chat.id, f'wrong answer❌ {self.stats["correct_count"]}/{self.stats["whole_count"]}', reply_markup=self.view_results_keyboard if self.learning_word + 1 == len(self.current_learning_words) else self.next_learning_word_keyboard)
            self.learn_history.append({'type': 'input', 'correct_answer': self.current_learning_words[self.learning_word]['values']['src'], 'wrong_answer': message.text, 'is_correct': False, 'obj': self.current_learning_words[self.learning_word]})

    def learn_word(self, message):
        if random.choice([True, False]):
            tr = GoogleTranslator(source=self.current_learning_words[self.learning_word]["languages"]["src"], target=self.current_learning_words[self.learning_word]["languages"]["dest"])
            print(self.__get_uqicues(count=2))
            self.wrong_answers = self.__get_uqicues(count=2)
            answers = [f"types.InlineKeyboardButton('{tr.translate(el)}', callback_data=\"{tr.translate(el)}_answer\")" for el in self.wrong_answers]
            answers.append(f"types.InlineKeyboardButton('{self.current_learning_words[self.learning_word]['values']['dest']}', callback_data=\"{self.current_learning_words[self.learning_word]['values']['dest']}_answer\")")
            answers_keyboard = types.InlineKeyboardMarkup()
            random.shuffle(answers)
            print(answers)
            exec(f"answers_keyboard.add({','.join(answers)})")
            print(answers_keyboard)
            bot.send_message(message.chat.id, f'choose correct translation of "**{self.current_learning_words[self.learning_word]["values"]["src"]}**"', parse_mode='Markdown', reply_markup=answers_keyboard)
        else:
            bot.send_message(message.chat.id, f'enter correct translation of "**{self.current_learning_words[self.learning_word]["values"]["src"]}**"', parse_mode='Markdown')
            bot.register_next_step_handler(message, self.input_truth_answer)

    def send_stats(self, id):
        output = []

        print(self.learn_history)

        print(self.learn_history)

        for i in range(len(self.learn_history)):
            print(self.learn_history[i]['type'])
            if self.learn_history[i]['type'] == 'input':
                tr = self.learn_history[i]['obj']['values']['src']
                de = self.learn_history[i]['obj']['values']['dest']
                output.append(f'{i + 1}) {self.learn_history[i]["correct_answer"]} - {self.learn_history[i]["wrong_answer"]} {"✅" if self.learn_history[i]["is_correct"] else f"❌ could be {tr} - {de}"}')
            elif self.learn_history[i]['type'] == 'choose':
                temp = [el for el in self.learn_history[i]['wrong_answers']]
                temp.append('*' + self.learn_history[i]['correct_answer'])

                output.append(f'{i + 1}) {" ".join(temp)} {"✅" if self.learn_history[i]["is_correct"] else "❌"}')

        bot.send_message(id, '\n'.join(output))


    #telebot "wrapper" - it means that this function uses with bot.register_next_step_handler
    def alter_wrapper(self, message):
        words = word_tokenize(message.text)
        if message.text == '-':
            bot.send_message(message.chat.id, 1)
        else:
            self.db.alter_word(message.chat.id, self.current_ten[self.current_word_index], ''.join(words))
            bot.send_message(message.chat.id, f'destination changed from "***{self.current_ten[self.current_word_index]["values"]["src"]}***" to "***{words[0]}***"\nand\ntranslation was changed from "***{self.current_ten[self.current_word_index]["values"]["dest"]}***" to "***{words[-1]}***"', parse_mode='Markdown')

    def logic_alter_word(self, message):
        bot.send_message(message.chat.id, """
                        enter the destination and translation like this:
                                    ***apple - яблоко***
                        """,
                         parse_mode='Markdown')
        bot.register_next_step_handler(message, self.alter_wrapper)


    def send_words_list(self, id, skip, count):
        pass

    def logic_add_new_word_to_module(self, message):
        add_new_word_keyboard = types.InlineKeyboardMarkup()
        add_new_word_keyboard.add(
            types.InlineKeyboardButton('vocabulary', callback_data='add_new_word_from_vocabulary'),
            types.InlineKeyboardButton('enter', callback_data='add_new_word_from_input'))
        bot.send_message(message.chat.id, f'add word from:', reply_markup=add_new_word_keyboard)

    def add_to_the_module(self, query_object, word_number):
        print(type(word_number))

        if self.db.is_word_not_in_module(query_object.message.chat.id, self.current_ten[int(word_number % 10) - 1]['values']['src']):
            #print(voc.current_ten[(int(query.data.split('_')[0]) % 10) - 1])
            self.db.add_to_the_module(query_object.message.chat.id, self.current_ten[(int(query_object.data.split('_')[0]) % 10) - 1], module=self.module_name)
            bot.answer_callback_query(callback_query_id=query_object.id, text=f'"{self.current_ten[(int(query_object.data.split("_")[0]) % 10) - 1]["values"]["src"]}" added to the "{self.module_name}"')
        else:
            bot.send_message(query_object.message.chat.id, 'this word already in other module')