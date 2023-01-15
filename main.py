from telegram.ext import Updater,MessageHandler,CommandHandler, Filters
from threading import Thread
from getWeather import *
from getTemp import *
from lightControl import *
from runDHT11 import *
import logging
import RPi.GPIO as GPIO

# logger setting
logging.basicConfig(format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s',
                    datefmt ='%m/%d %I:%M:%S %p',
                    level=logging.DEBUG)

#using multithread for Loop DHT Sensor
Thread(target = runTempSensor).start() 
logging.info('Start DHT11 Sensor') 

# token, chat_id
with open("./token.txt") as f:
    lines = f.readlines()
    token = lines[0].strip()
    id = lines[1].strip()

# updater setting 
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

# polling setting
updater.start_polling()

# command handler
def help(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="/help 명령어 종류: 날씨,불켜줘,불꺼줘,집")
 
# message handler
def funcHandler(update, context):
    user_text = update.message.text
    if user_text == "날씨":
        todayWeather = weather.getWeather()
        logging.info('getWeather')
        context.bot.send_message(chat_id=id,text= todayWeather)
    elif user_text == "on" or user_text == "불켜줘":
        on = light.lightControl(1)
        logging.info('lightOn')
        context.bot.send_message(chat_id=id,text = on)
    elif user_text == "off" or user_text == "불꺼줘":
        off = light.lightControl(0)
        logging.info('lightOff')
        context.bot.send_message(chat_id=id,text = off)
    elif user_text == "집" or user_text == "상태":
        status = temp.Temprature()
        logging.info('homeStatus')
        context.bot.send_message(chat_id=id,text= status)
    else:
        logging.warning('emptyInput')
        context.bot.send_message(chat_id=id,text= "알 수 없는 명령이에요.\n /help를 통해 명령어를 확인하세요")

#drive handler
help_handler = CommandHandler('help',help)
dispatcher.add_handler(help_handler)
func_handler = MessageHandler(Filters.text, funcHandler)
dispatcher.add_handler(func_handler)
