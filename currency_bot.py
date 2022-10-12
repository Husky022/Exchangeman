import settings
import exchange
import telebot
import pytz
from keyboa import Keyboa

P_TIMEZONE = pytz.timezone(settings.TIMEZONE)
TIMEZONE_COMMON_NAME = settings.TIMEZONE_COMMON_NAME

bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    telebot.types.ReplyKeyboardRemove()
    reply_keyboard = telebot.types.ReplyKeyboardMarkup(True)
    reply_keyboard.row('Курс валют к рублю', 'Помощь')
    bot.send_message(
        message.chat.id,
        'Привет! Я могу показывать курсы валют!\n' +
        'Список валют - нажми /exchange.\n' +
        'Чтобы запросить помощь - нажми /help.', reply_markup=reply_keyboard
    )


@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Message the developer', url='telegram.me/balashovia'
        )
    )
    bot.send_message(
        message.chat.id,
        '1) Чтобы увидеть список доступных валют, нажмите /exchange.\n' +
        '2) Нажмите на интересующую Вас валюту.\n' +
        '3) Вы получите информацию по продаже и покупке выбранной валюты по курсу ЦБ.\n' +
        '4) Нажмите “Update”, чтобы обновить текущую информацию по курсу.\n' +
        '5) Поддержка Бота всегда на связи. Напишите telegram.me/balashovia по любым вопросам и предложениям',
        reply_markup=keyboard
    )


@bot.message_handler(commands=['exchange'])
def exchange_command(message):
    keyboard = Keyboa(items=sorted(list(exchange.load_exchange().keys())), copy_text_to_callback=True,
                            items_in_row=5)
    bot.send_message(message.chat.id, 'Выберите валюту:', reply_markup=keyboard())


@bot.callback_query_handler(func=lambda c :True)
def inline(c):
    bot.send_message(
        c.message.chat.id,
        'По текущему курсу ЦБ РФ: \n\n' +
        f'{exchange.get_exchange(c.data)["Nominal"]} {exchange.get_exchange(c.data)["Name"]} = ' +
        f'{exchange.get_exchange(c.data)["Value"]} руб. \n\n' +
        'Предыдущий курс: \n\n' +
        f'{exchange.get_exchange(c.data)["Nominal"]} {exchange.get_exchange(c.data)["Name"]} = ' +
        f'{exchange.get_exchange(c.data)["Previous"]} руб. \n\n')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Курс валют к рублю':
        keyboard = Keyboa(items=sorted(list(exchange.load_exchange().keys())), copy_text_to_callback=True,
                                items_in_row=5)
        bot.send_message(message.chat.id, 'Выберите валюту:', reply_markup=keyboard())
    if message.text == 'Помощь':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(
            telebot.types.InlineKeyboardButton(
                'Message the developer', url='telegram.me/balashovia'
            )
        )
        bot.send_message(
            message.chat.id,
            '1) Чтобы увидеть список доступных валют, нажмите /exchange.\n' +
            '2) Нажмите на интересующую Вас валюту.\n' +
            '3) Вы получите информацию по продаже и покупке выбранной валюты по курсу ЦБ.\n' +
            '4) Нажмите “Update”, чтобы обновить текущую информацию по курсу.\n' +
            '5) Поддержка Бота всегда на связи. Напишите telegram.me/balashovia по любым вопросам и предложениям',
            reply_markup=keyboard
        )


if __name__ == "__main__":
    bot.infinity_polling()





