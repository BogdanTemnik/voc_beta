from modules.Database.Database import Database
from config.config import bot_object as bot
from telebot import types

class Teacher:
    def __init__(self):
        self.db = Database()
        self.current_class_list = None
        self.current_student_id = None
        self.current_class_stats = None

    def send_students(self, teacher_id):
        students_objects = self.db.get_students(teacher_id)
        print(students_objects)
        buttons = []
        temp = []
        n = 'name'
        id = 'student_id'
        for i in range(len(students_objects)):
            buttons.append(f'types.InlineKeyboardButton("{i + 1}", callback_data="{students_objects[i][id]}_student")')
            if (i + 1) % 5 == 0:
                buttons.append(temp)
                temp = []

        if temp:
            buttons.append(temp)

        print(buttons)

        output = [f'{i + 1}) {students_objects[i][n]}' for i in range(len(students_objects))]
        students_keyboard = types.InlineKeyboardMarkup()
        exec(f'students_keyboard.add({",".join(buttons)})')
        students_keyboard.add(types.InlineKeyboardButton('add', callback_data='add_first_student'))

        bot.send_message(teacher_id, '\n'.join(output), reply_markup=students_keyboard)

    def is_class_permeability(self, teacher_id):
        return True if 'classes' in [el['name'] for el in self.db.client.list_databases()] and self.db.classes_db[f'{teacher_id}'].count() else False

    def add_student(self, message):
        self.db.classes_db[f'{message.chat.id}'].insert_one({'student_id': int(message.text), 'name': self.db.users_db[f'{self.current_student_id}'].find_one({'id': int(message.text)})['first_name']})

    def is_unique_student(self, student_id, teacher_id):
        return True if not [el for el in self.db.classes_db[f'{teacher_id}'].find({'student_id': student_id})] else False

    def logic_get_student_id(self, message):
        if self.db.is_int(message.text) and self.is_unique_student(int(message.text), message.chat.id) and self.db.is_user(int(message.text)):
            self.current_student_id = int(message.text)
            print(self.current_student_id)
            self.add_student(message)
            bot.send_message(message.chat.id, 'student added')
        else:
            if not self.db.is_int(message.text):
                bot.send_message(message.chat.id, 'that is not id')
            elif not self.db.is_user(int(message.text)):
                bot.send_message(message.chat.id, 'unknown id')
            else:
                bot.send_message(message.chat.id, 'student already in your class')

    def send_class_statistic(self, teacher_id):
        output = []
        students_stats = self.db.get_class_statistic(teacher_id)


        if students_stats is not None:
            for student in students_stats:
                output.append(f"{student['name']} - {student['total']}")
            bot.send_message(teacher_id, '\n'.join(output))
        else:
            bot.send_message(teacher_id, 'error')