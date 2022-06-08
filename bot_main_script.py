import telebot
import yfinance as yf
import finvizTest
import secret

bot = telebot.TeleBot(secret.api_key)

@bot.message_handler(commands=['hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hello!")

def stock_request(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "price":
    return False
  else:
    return True

def chart_request(message):
  request = message.text.split()
  if len(request) < 2 or request[0].lower() not in "chart":
    return False
  else:
    return True

@bot.message_handler(func=stock_request)
def send_price(message):
  request = message.text.split()[1].upper()
  companyInfo = yf.Ticker(request)
  try:
    priceRequest = companyInfo.info["previousClose"]
    output = f"Previous closing price for ticker ${request}: ${priceRequest}."
    bot.send_message(message.chat.id, output)
  except KeyError:
    bot.send_message(message.chat.id, "No ticker found!")

@bot.message_handler(func=chart_request)
def send_price(message):
  request = message.text.split()[1].upper()
  try:
    chartRequest = finvizTest.chartUrl(request)
    output = f"{chartRequest}."
    bot.send_message(message.chat.id, output)
  except:
    bot.send_message(message.chat.id, "No ticker found!")

bot.polling()