from traceback import print_tb
from logo import logo
import csv
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from requests import *#get()
import os



API_KEY = os.getenv('API_KEY')
dp = Bot(token=API_KEY)
bot = Dispatcher(dp)
kerboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("HIGHER!", "LOWER!")


acc = []
with open('highORlow.csv', mode='r') as file:
    all = csv.reader(file)
    for i in all:
        acc.append(i)


def assign():
    a = (random.choice(acc) )
    z = (random.choice(acc) )
    while (a[3].isdigit()==False ):
         a = (random.choice(acc) )
    while (z[3].isdigit()==False ):
         z = (random.choice(acc) )  
    print(a)
    print(z[3])  
    return a, z

a,z=assign()

#print(acc)

def compare(x):
    if x =="HIGHER!":
        if max(int(a[3]),int(z[3]) )==int(z[3]):
            #correct retur
            return True
            
        else:
            #emd amd display score
            return False
    elif x =="LOWER!":
        if min(int(a[3]),int(z[3]) )==int(z[3]):
            #correct 
            return True
        else:
            #emd amd display score
            return False
            
    else: 
        return "what"

@bot.message_handler(commands=['start', 'Start'])
async def welcome(message: types.Message):
    #score = 0
    await message.reply(logo, reply_markup=kerboard_reply)
    await message.reply(f'{a[1]} vs {z[1]}: {z[1]} is')

@bot.message_handler()
async def wel(message: types.Message):
    if message.text == "LOWER!" or message.text =="HIGHER!":
        if(compare(message.text)==True ):
            print( compare(message.text) )
            score += 1
            a,z=assign()
            await message.reply("correct" ,reply_markup=kerboard_reply)
            await message.reply(f'{a[1]} vs {z[1]}: {z[1]} is', reply_markup=kerboard_reply)
        else:
            print(compare(message.text))
            await message.reply(f'score:{score}')
            a,z=assign()
            await message.reply(f'{a[1]} vs {z[1]}: {z[1]} is', reply_markup=kerboard_reply)
            
score = 0        
executor.start_polling(bot)
