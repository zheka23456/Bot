import telebot
import constants
import os
import Nachalniki
bot = telebot.TeleBot(constants.token)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start','/help')
    user_markup.row('розклад', 'заміни', 'дзвінки')
    user_markup.row('заява', 'пояснювальна')
    user_markup.row('Ми на карті')
    user_markup.row('Де знаходиться:?')
    user_markup.row('Маршрут №15:')
    bot.send_message(message.from_user.id, "Доброго часу доби)", reply_markup=user_markup)

print(bot.get_me())


def log(message, answer):
                print("\n-----")
                from datetime import datetime
                print((datetime.now()))
                print(" Сообщение от {0} {1}. (id={2} )\n  Текст - {3}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                str(message.from_user.id),
                                                                 message.text))
                print("   Ответ - " + answer)


@bot.message_handler(commands=["help"])
def handle_text(message):
                    bot.send_message(message.chat.id, "Привіт, Мене звуть Марія Іванівна."
                                                      "\n Я можу відповісти на питання стововно технікуму та навчання."
                                                      "\n Основні питання, які можуть виникати у вас, я відвела"
                                                      " в окремому меню."
                                                      "\n Просто відкрийте випадаюче меню та оберіть питання, "
                                                      "яке вас цікавить."
                                                      "\n Також ви можете спілкуватися зі мною за допомогою звичайної"
                                                      "клавіатури звичним способом."
                                                      "\n Приємного спілкування 😉 ")


@bot.message_handler(content_types=['text'])
def handle_tex(message):
    message.text = message.text.lower()
    if message.text.find("лох") != -1 or message.text.find("сук") != -1 or message.text.find("бля") != -1:
        answer = "Не висловлюйся при викладачеві!"
        log(message, answer)
        bot.send_message(message.chat.id, "Не висловлюйся при викладачеві!")
    elif message.text.find("прив") != -1 or message.text.find("доброго") != -1 or message.text.find("ghbd") != -1\
            or message.text.find("добрый") != -1 or message.text.find("здравств") != -1:
            answer = "Доброго дня" + " " + str(message.from_user.first_name) + "!"
            log(message, answer)
            bot.send_message(message.chat.id, "Доброго дня" + " " + str(message.from_user.first_name) + "!")
    elif message.text.find("cghfdb") != -1 or message.text.find("ltkf") != -1 or message.text.find("дела") != -1\
            or message.text.find("справи") != -1:
        answer = "Все добре,чим можу допомогти?"
        log(message, answer)
        bot.send_message(message.chat.id, "Все добре,чим можу допомогти?")
    elif message.text.find("зовут") != -1 or message.text.find("звати") != -1 or message.text.find("ім'я") != -1 \
            or message.text.find("имя") != -1:
        answer = "Мене звати Марія Іванівна"
        log(message, answer)
        bot.send_message(message.chat.id, "Мене звати Марія Іванівна")
    elif message.text.find("возраст") != -1 or message.text.find("лет") != -1 or message.text.find("років") != -1 \
            or message.text.find("вік") != -1:
        answer = "У жінок про вік не питають"
        log(message, answer)
        bot.send_message(message.chat.id, "У жінок про вік не питають")
    elif message.text.find("пар") != -1 or message.text.find("расписание") != -1 or message.text.find("розклад") != -1:
        answer = "В якій групі ви навчаєтесь?"
        log(message, answer)
        bot.send_message(message.chat.id, "В якій групі ви навчаєтесь?")
    elif message.text.find("711") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/711'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("511") != -1 or message.text.find("611") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/511_611'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("311") != -1 or message.text.find("911") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/311_911'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("111") != -1 or message.text.find("811") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/111_811'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("621") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/621'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("921") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/921'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("821") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/821'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("721") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/721'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("702") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/702'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("521") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/521'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("421") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/421'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("322") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/322'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("321") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/321'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("221") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/221'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("122") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/122'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("121") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/121'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("931") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/931'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("831") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/831'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("731") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/731'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("703") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/703'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("631") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/631'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("531") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/531'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            answer = "Ось вам розклад занятть:"
            log(message, answer)
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("431") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/431'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("332") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/332'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("331") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/331'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("231") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/231'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("132") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/132'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("131") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/131'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("941") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/941'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("741") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/741'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("342") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/342'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("142") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ось вам розклад занятть:")
        directory = 'D:\Programs\Бот\Documents/142'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("замен") != -1 or message.text.find("замін") != -1:
        answer = "Ось вам розклад занятть:"
        log(message, answer)
        bot.send_message(message.chat.id, "Заміни на завтра:")
        directory = 'D:\Programs\Бот\Documents\zameni'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("заяв") != -1:
        answer = "Бланк заповнення заяви:"
        log(message, answer)
        bot.send_message(message.chat.id, "Бланк заповнення заяви:")
        directory = 'D:\Programs\Бот\Documents\zayava'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("поясн") != -1 or message.text.find("Обьясн") != -1:
        answer = "Бланк заповнення пояснювальної записки:"
        log(message, answer)
        bot.send_message(message.chat.id, "Бланк заповнення пояснювальної записки:")
        directory = 'D:\Programs\Бот\Documents\poyasnyuvalna'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("дзв") != -1 or message.text.find("звон") != -1:
        answer = "Розклад дзвінків:"
        log(message, answer)
        bot.send_message(message.chat.id, "Розклад дзвінків:")
        directory = 'D:\Programs\Бот\Documents/dzvinki'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("локация") != -1 or message.text.find("адрес") != -1 or message.text.find("нахождения") != -1\
            or message.text.find("знаходження") != -1 or message.text.find("карт") != -1 \
            or message.text.find("локація") != -1:
        answer = "Ми на карті:"
        log(message, answer)
        bot.send_message(message.chat.id, "Ми на карті:")
        bot.send_chat_action(message.chat.id, 'find_location')
        bot.send_location(message.chat.id, 51.224849650919865, 33.2270427122603)
    elif message.text.find("де") and message.text.find("знах") != -1 or message.text.find("где") \
            and message.text.find("наход") != -1:
        answer = "Ми на карті:"
        log(message, answer)
        bot.send_message(message.chat.id, " - Відділ кадрів знаходиться на другому поверсі, кабінет № ... ")
        bot.send_message(message.chat.id, " - Профком знаходиться на ... поверсі, кабінет № ... ")
        bot.send_message(message.chat.id, " - Студентський парламент знаходиться на ... поверсі, кабінет № ... ")
        bot.send_message(message.chat.id, " - Бухгалтерія знаходиться на другому поверсі, кабінет № ... ")
    elif message.text.find("зав") != -1 and message.text.find("відд") != -1 or message.text.find("зав") != -1\
            and message.text.find("отдел") != -1:
        answer = "На якому курсі ви навчаєтесь? \n Чи є ви студентом проф освіти (так або ні)"
        log(message, answer)
        bot.send_message(message.chat.id, "На якому курсі ви навчаєтесь? \n Чи є ви студентом проф освіти (так або ні)")
    elif message.text.find("1") != -1 and message.text.find("так") != -1 \
            or message.text.find("1") != -1 and message.text.find("да") != -1 \
            or message.text.find("2") != -1 and message.text.find("так") != -1 \
            or message.text.find("2") != -1 and message.text.find("да") != -1 \
            or message.text.find("3") != -1 and message.text.find("так") != -1 \
            or message.text.find("3") != -1 and message.text.find("да") != -1 \
            or message.text.find("пер") != -1 and message.text.find("так") != -1 \
            or message.text.find("пер") != -1 and message.text.find("да") != -1 \
            or message.text.find("втор") != -1 and message.text.find("так") != -1 \
            or message.text.find("втор") != -1 and message.text.find("да") != -1 \
            or message.text.find("други") != -1 and message.text.find("так") != -1 \
            or message.text.find("други") != -1 and message.text.find("да") != -1 \
            or message.text.find("трет") and message.text.find("так") != -1 \
            or message.text.find("трет") and message.text.find("да") != -1:
        answer = "Ваш зав відділенням: " + Nachalniki.Zhmud.prizv \
                 + Nachalniki.Zhmud.name + Nachalniki.Zhmud.po_batkovi
        log(message, answer)
        bot.send_message(message.chat.id, "Ваш зав відділенням:" + Nachalniki.Zhmud.prizv
                         + Nachalniki.Zhmud.name + Nachalniki.Zhmud.po_batkovi)
    elif message.text.find("2") != -1 and message.text.find("ні") != -1 \
            or message.text.find("2") != -1 and message.text.find("нет") != -1 \
            or message.text.find("3") != -1 and message.text.find("ні") != -1 \
            or message.text.find("3") != -1 and message.text.find("нет") != -1 \
            or message.text.find("4") != -1 and message.text.find("ні") != -1 \
            or message.text.find("4") != -1 and message.text.find("нет") != -1 \
            or message.text.find("втор") != -1 and message.text.find("ні") != -1 \
            or message.text.find("втор") != -1 and message.text.find("нет") != -1 \
            or message.text.find("други") != -1 and message.text.find("ні") != -1 \
            or message.text.find("други") != -1 and message.text.find("нет") != -1 \
            or message.text.find("трет") != -1 and message.text.find("ні") != -1 \
            or message.text.find("трет") != -1 and message.text.find("нет") != -1 \
            or message.text.find("чет") != -1 and message.text.find("ні") != -1 \
            or message.text.find("чет") != -1 and message.text.find("нет") != -1:
        answer = "Ваш зав відділенням: " + Nachalniki.Sovgir.prizv + Nachalniki.Sovgir.name + Nachalniki.Sovgir.po_batkovi
        log(message, answer)
        bot.send_message(message.chat.id, "Ваш зав відділенням: " + Nachalniki.Sovgir.prizv
                         + Nachalniki.Sovgir.name + Nachalniki.Sovgir.po_batkovi)
    elif message.text.find("1") != -1 and message.text.find("ні") != -1 != -1 \
            or message.text.find("1") != -1 and message.text.find("нет") != -1 \
            or message.text.find("пер") != -1 and message.text.find("ні") != -1 \
            or message.text.find("пер") != -1 and message.text.find("нет") != -1:
        answer = "Ваш зав відділенням: " + Nachalniki.Vasiletc.prizv \
                 + Nachalniki.Vasiletc.name + Nachalniki.Vasiletc.po_batkovi
        log(message, answer)
        bot.send_message(message.chat.id, "Ваш зав відділенням: " + Nachalniki.Vasiletc.prizv
                         + Nachalniki.Vasiletc.name + Nachalniki.Vasiletc.po_batkovi)
    elif message.text.find("марш") != -1 or message.text.find("15") != -1:
        answer = "Розклад маршруту №15:"
        log(message, answer)
        bot.send_message(message.chat.id, "Розклад маршруту №15:")
        directory = 'D:\Programs\Бот\Documents\marsha'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for files in all_files_in_directory:
            doc = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.chat.id, 'upload_document')
            bot.send_document(message.chat.id, doc)
            doc.close()
    elif message.text.find("директ") != -1:
        answer = "Наш директор: " + Nachalniki.Director.prizv \
                 + Nachalniki.Director.name + Nachalniki.Director.po_batkovi
        log(message, answer)
        bot.send_message(message.chat.id,
                         "Наш " + Nachalniki.Director.posada + ": " + Nachalniki.Director.prizv
                         + Nachalniki.Director.name + Nachalniki.Director.po_batkovi)
    elif message.text.find("зам") != -1:
        answer = Nachalniki.Zamistnik.posada + ": " + Nachalniki.Director.posada + ": " + Nachalniki.Zamistnik.prizv \
                 + Nachalniki.Zamistnik.name + Nachalniki.Zamistnik.po_batkovi
        log(message, answer)
        bot.send_message(message.chat.id,
                         Nachalniki.Zamistnik.posada + ": " + Nachalniki.Zamistnik.prizv
                         + Nachalniki.Zamistnik.name + Nachalniki.Zamistnik.po_batkovi)
    else:
        answer = "Я не впевнена, що зрозуміла вас правильно"
        log(message, answer)
        bot.send_message(message.chat.id, "Я не впевнена, що зрозуміла вас правильно")


if __name__ == '__main__':
    bot.polling(none_stop=True)


