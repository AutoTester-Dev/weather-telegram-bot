import telebot
import requests

# Insert your Telegram Bot Token here
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# OpenWeatherMap API key
API_KEY = "08c04f9cc801e28cbcb4be4f5cf8018a"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Enter the city name, and I will tell you the weather.")

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city = message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        bot.reply_to(message, f"📍 City: {city.capitalize()}\n🌡 Temperature: {temp}°C\n☁️ Condition: {weather_desc}")
    else:
        bot.reply_to(message, "❌ Error: City not found or API issue.")

bot.infinity_polling()
