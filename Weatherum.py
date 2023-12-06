# подключаем модуль для Телеграмма
import telebot
import requests
import datetime

# указываем токен для доступа к боту
bot = telebot.TeleBot('6683573226:AAFtvtPm8LheGsWPdrj1tMajQBPP5arD5fk')

# обрабатываем старт бота
@bot.message_handler(commands=['start'])
def start(message):
    # получаем имя пользователя из объекта message
    username = message.from_user.first_name
    # выводим приветственное сообщение
    start_txt = f'Привет, {username}! \n\nОтправь мне название города, а я пришлю сводку погоды на текущий момент.'
    bot.send_message(message.from_user.id, start_txt, parse_mode='Markdown')

# обрабатываем любой текстовый запрос
@bot.message_handler(content_types=['text'])
def weather(message):
    # получаем город из сообщения пользователя
    city = message.text
    # формируем запрос
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    # отправляем запрос на сервер и сразу получаем результат
    weather_data = requests.get(url).json()
    # получаем данные о погоде
    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    code = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Drizzle": "🌧️",
        "Thunderstorm": "⛈️",
        "Snow": "🌨️",
        "Mist": "🌫️"
    }
    weather_main = weather_data['weather'][0]['main']
    weather_description = weather_data['weather'][0]['description']
    humidity = weather_data['main']['humidity']
    wind = weather_data['wind']['speed']
    pressure = weather_data['main']['pressure']
    visibility = weather_data['visibility']
    # получаем текущую дату и время
    current_time = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M")
    # формируем ответы
    w_now = (f'🌀️ {city}, {current_time}'
             f'\n\n    {str(code[weather_main])} {(str(weather_description)).capitalize()}'
             f'\n    🌡️ Температура: {str(temperature)}°C (по ощущениям {str(temperature_feels)}°C)'
             f'\n    💦 Влажность: {str(humidity)}%'
             f'\n    🍃 Ветер: {str(wind)} м/c'
             f'\n    📈 Давление: {str(pressure)} мм.рт.ст'
             f'\n    🔦 Видимость: {str(visibility)} м'
             f'\n\nХорошего дня!')
    # отправляем значения пользователю
    bot.send_message(message.from_user.id, w_now)

    if temperature > 28:
        bot.send_message(message.from_user.id, '⚠️ Жара! Носите легкую одежду, пейте достаточно воды, избегайте длительного нахождения на солнце.')
    elif temperature < -22:
        bot.send_message(message.from_user.id, '⚠️ Мороз! Носите теплую одежду и избегайте длительного пребывания на улице.')
    elif wind > 20:
        bot.send_message(message.from_user.id, '⚠️ Штормовой ветер! Избегайте открытых пространств и держитесь подальше от деревьев, рекламных щитов и других потенциально опасных объектов. По возможности не выходите на улицу.')
    elif visibility < 1000 or weather_main == 'Mist':
        bot.send_message(message.from_user.id, '⚠️ Плохая видимость! Будьте осторожны за рулем и на дорогах!')ТВ

# запускаем бота
if __name__ == '__main__':
    while True:
        # в бесконечном цикле постоянно опрашиваем бота — есть ли новые сообщения
        try:
            bot.polling(none_stop=True, interval=0)
        # если возникла ошибка — сообщаем про исключение и продолжаем работу
        except Exception as e:
            print('Ошибка!')