import telebot
import json
import time

# Cетим токен
bot = telebot.TeleBot('')

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message):
    # Самое первое сообщение
    bot.send_message(message.chat.id, 'Привет! Отправь мне свой JSON и я проверю его валидность.', parse_mode="Markdown")


@bot.message_handler()
def handle_text(message):
    user_json = message.text
    try:
        # Проверяем джейсон
        user_json = json.loads(user_json)
        beautify_json = json.dumps(user_json, indent=2, sort_keys=True, ensure_ascii=False)
        # Все ок
        bot.send_message(chat_id=message.chat.id, text=f'🟢 Все ок\n\n{beautify_json}')

    except json.JSONDecodeError as ex:
        #При ошибке валидации отправляем
        bot.send_message(chat_id=message.chat.id, text=f'🔴 При обработке произошла ошибка:\n\n{str(ex)}')

# Запускаем бота
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(2)
            print(e)