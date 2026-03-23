# main.py

# import library
import telebot
import telegram_database
import os
from dotenv import load_dotenv
import random
from telebot import types

# load const from .env file
load_dotenv()

# create a Telegram bot
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(token=TOKEN)

# buttons name for main menu
class Command:
    ADD_WORD = 'Добавить слово ➕'
    DELETE_WORD = 'Удалить слово 🔙'
    NEXT = 'Дальше ⏭'

# save a current word
current_word = {}

# start command
@bot.message_handler(commands = ['start'])
def start(message):
    print('start command')
    markup = types.ReplyKeyboardRemove()    # remove a menu
    bot.send_message(message.chat.id, f"Привет, юзер {message.from_user.first_name} {message.from_user.last_name}. Я бот изучения английского языка", reply_markup = markup)
    draw_menu(message = message)    # draw a main menu

# draw main menu
def draw_menu(message):
    user_id = telegram_database.get_user_id(message.from_user.id)
    words = telegram_database.get_words(user_id)    # get all words for translate

    if not words:
        # no words in database - draw command buttons only
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        buttons = list()
        buttons.append(types.KeyboardButton(Command.NEXT))
        buttons.append(types.KeyboardButton(Command.ADD_WORD))
        buttons.append(types.KeyboardButton(Command.DELETE_WORD))
        markup.add(*buttons)

        bot.send_message(message.chat.id,"База слов пуста. Добавьте новые слова с помощью кнопки 'Добавить слово'.", reply_markup = markup)
        return

    # get random word for translate from words array
    word_id, target_word, transl_word = random.choice(words)
    # save current word for current user
    current_word[message.chat.id] = {
        'word_id': word_id,
        'target_word': target_word,
        'transl_word': transl_word
    }
    # create keyboard with current word + 3 random words
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    word_list = [transl_word]   # current word
    while len(word_list) < 4:
        random_word = random.choice(words)[2]   #translate
        word_list.append(random_word)
    #shuffle words
    random.shuffle(word_list)
    # add words buttons
    buttons = [types.KeyboardButton(text=word) for word in word_list]
    # add main menu buttons
    buttons.append(types.KeyboardButton(Command.NEXT))
    buttons.append(types.KeyboardButton(Command.ADD_WORD))
    buttons.append(types.KeyboardButton(Command.DELETE_WORD))
    markup.add(*buttons)    # draw keyboard

    bot.send_message(message.chat.id, f"Выбери перевод слова:\n🇬🇧 {target_word}", reply_markup=markup)    # send message with keyboard

# add button
@bot.message_handler(func=lambda message: message.text == Command.ADD_WORD)
def add_word_button(message):
    msg = bot.reply_to(message, "Введите английское слово для добавления:")
    bot.register_next_step_handler(msg, add_word_en)    # wait user answer and call add_word_en

# next button
@bot.message_handler(func=lambda message: message.text == Command.NEXT)
def next_word_button(message):
    draw_menu(message)

# delete button
@bot.message_handler(func=lambda message: message.text == Command.DELETE_WORD)
def delete_word_button(message):
    user_id = telegram_database.get_user_id(message.from_user.id)
    words = telegram_database.get_words_for_delete(user_id)

    if not words:
        bot.send_message(message.chat.id, "Нет доступных слов для удаления.")
        return

    # create keyboard of word
    markup = types.InlineKeyboardMarkup()
    for word_id, word, translation in words:
        button_text = f"{word} ({translation})"
        callback_data = f"delete_word:{word_id}"    # callback for button
        button = types.InlineKeyboardButton(text=button_text, callback_data=callback_data)
        markup.add(button)

    bot.send_message(message.chat.id, "Выберите слово для удаления:", reply_markup=markup)

# test callback from keyboard (delete mode)
@bot.callback_query_handler(func=lambda call: call.data.startswith('delete_word:'))
def delete_word_confirmation(call):
        word_id = call.data.split(':')[1]   #  find word id in callback
        user_id = telegram_database.get_user_id(call.from_user.id)

        telegram_database.delete_word(user_id, word_id)
        bot.send_message(call.message.chat.id, "Слово удалено.")
        # update words list
        draw_menu(call.message)

# answer eng word - save a word
def add_word_en(message):
    current_word[message.chat.id] = {'word': message.text}  # save eng
    msg = bot.reply_to(message, "Введите перевод на русский:")
    bot.register_next_step_handler(msg, add_word_ru)    # after enter goto next step - add_word_ru

# answer rus word
def add_word_ru(message):
    translation = message.text.lower()  # load ru
    user_id = telegram_database.get_user_id(message.from_user.id)
    chat_id = message.chat.id
    word = current_word[chat_id]['word']    # load eng

    telegram_database.add_word(user_id, word, translation)
    print(f'Добавлено слово в словарь: {word} -> {translation}')
    bot.send_message(message.chat.id, f'Добавлено слово в словарь: {word} -> {translation}')
    draw_menu(message)

# test answer from user
# ставим самой последней проверкой, чтобы сначала обработались кнопки клавиатуры
# и переходы
@bot.message_handler(func=lambda message: True, content_types=['text'])
def message_reply(message):
    chat_id = message.chat.id
    target_word = current_word[chat_id]['target_word']  # load eng
    transl_word = current_word[chat_id]['transl_word']  # load ru

    if not target_word:
        bot.send_message(chat_id, f"Ответ не распознан - нет целевого слова")
        draw_menu(message)
        return

    # compare ru and answer
    if message.text.lower() == transl_word.lower():
        bot.send_message(chat_id, f"Верно! {target_word} -> {transl_word}")
        current_word.pop(chat_id)
        draw_menu(message)
    else:
        bot.send_message(chat_id,"Неправильно. Повторите еще раз.")

# start
# не забудьте включить ВПН - без него ничего не работает!!!
if __name__ == '__main__':
    print('Бот запущен...')
    print('Для завершения нажмите Ctrl+Z')
    bot.infinity_polling(timeout=90, long_polling_timeout=5)    # здесь идет бесконечный цикл, после него ничего не выполняется!!!



