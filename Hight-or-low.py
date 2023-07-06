from traceback import print_tb
from logo import logo,vs
import csv
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from requests import *#get()
import os
from scraper import *

global score 
score = 0 

# API_KEY = os.getenv('API_KEY')
API_KEY = '5699527558:AAGtfCXqGB5fDqcByRpNTq2rPZzcUbIh504'

dp = Bot(token=API_KEY)
bot = Dispatcher(dp)
kerboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("HIGHER!", "LOWER!")


acc = []
with open('out.csv', mode='r') as file:
    all = csv.reader(file)
    for i in all:
        acc.append(i)


def assign():
    a = (random.choice(acc) )
    z = (random.choice(acc) )
    while (a[1].isdigit()==False ):
         a = (random.choice(acc) )
    # this makes sure we only chose the once that are the actual accounts
    while (z[1].isdigit()==False or a==z):
         z = (random.choice(acc) )  
    print(a)
    print(z)  
    return a, z

a,z=assign()

#print(acc)

def compare(x):
    if x =="HIGHER!":
        if max(int(a[1]),int(z[1]) )==int(z[1]):
            #correct retur
            return True
            
        else:
            #emd amd display score
            return False
    elif x =="LOWER!":
        if min(int(a[1]),int(z[1]) )==int(z[1]):
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
    await message.reply(f'{a[2]} vs {z[2]}: {z[2]} is')

@bot.message_handler()
async def wel(message: types.Message):
    if message.text == "LOWER!" or message.text =="HIGHER!":
        if(compare(message.text)==True ):
            print( compare(message.text) )
            global score
            score += 1
            a,z=assign()
            await message.reply("correct" ,reply_markup=kerboard_reply)
            await message.reply(f'{a[2]} vs {z[2]}: {z[2]} is', reply_markup=kerboard_reply)
        else:
            print(compare(message.text))
            await message.reply(f'score:{score}')
            #global score
            score =0
            a,z=assign()
            await message.reply(logo, reply_markup=kerboard_reply)
            await message.reply(f'{a[2]} vs {z[2]}: {z[2]} is', reply_markup=kerboard_reply)
            
       
executor.start_polling(bot)