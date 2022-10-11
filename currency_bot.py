import telebot

import settings


class TrainAssistantBot:

    def __init__(self):
        self.token = settings.TOKEN
        self.bot = telebot.TeleBot(self.token)
        self.handler = Handler(self.bot)
        # self.cache_data = None
        # self.cache_currency = None
        # self.database = DBManager(user=settings.DB_USER,
        #                           password=settings.DB_PASSWORD,
        #                           database_name=settings.DB_NAME)
        # self.googlesheets = GoogleSheets(credentials=settings.CREDENTIALS_FILE,
        #                                  spreedsheet_id=settings.SPREADSHEET_ID)
        # self.exchangeman = ExchangeManager(api=settings.BANK_API,
        #                                    valute='USD')


    # def get_data_from_api(self):
    #     return self.googlesheets.unload(), self.exchangeman.load_exchange()
    #
    # def run(self):
    #     self.cache_data = self.database.get_data()  # формируем первоначальный кэш данных из нашей БД
    #     self.cache_currency = self.exchangeman.load_exchange()  # получаем первоначальный кэш данных курса USD
    #     # Далее запускаем цикл сравнения нашего кэша данных с данным из таблицы google
    #     # и кэша валют с текущим курсом
    #     while True:
    #         current_currency = self.exchangeman.load_exchange()  # получаем текущий курс валюты
    #         values_from_sheets = self.googlesheets.unload()  # выгружаем данные из таблицы google
    #         # Если текущий курс не совпадает с кэшем или данные из таблицы не совпадают с кэшем
    #         if self.cache_currency != current_currency or self.cache_data != values_from_sheets:
    #             # то записываем новые данные с учетом изменений в БД
    #             self.database.recording(values_from_sheets, current_currency)
    #             # и обновляем кэш
    #             self.cache_data = values_from_sheets
    #             self.cache_currency = current_currency
    #             print('Изменение')
    #         else:
    #             print('без изменений')
    #         time.sleep(settings.TIMING)


    def run(self):
        self.handler.handle()
        self.bot.polling(none_stop=True)



if __name__ == '__main__':
    bot = TrainAssistantBot()
    bot.run()




