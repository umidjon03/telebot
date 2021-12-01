"""
This is translater bot, when 
input is less than 2 words it returns 
definitions and pronunciation of the 
word from Oxford dectionary, otherwise 
returns translation form from googletranslation
uz->eng or eng->uz regarding to situation
"""

import logging

from aiogram.types import audio
from Oxford import getdic
from google import detecter, self_translator

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2130218743:AAHwvtQICb_04zQasP4cjq0rw1Ax5VaWmOE'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start`
    """
    await message.reply("Hi!\nI'm EnglisherBot!\nPlease type word(s)\n\n\nSalom!\nMen EnglisherBot'man\nIltimos so'z(lar) kiriting")


@dp.message_handler(commands='help')
async def helper(message: types.Message):
    """This handler will be called when user sens `/help`"""

    await message.reply("How can I help you?\nPlease write to this address: @umidjon_shuxratov\n\n\nQanday yordam beraolishim mumkin?\nIltimos quyidagi manzilga murojaat qiling: @umidjon_shuxratov")



@dp.message_handler()
async def trans(message: types.Message):
    fin_translate = self_translator(message.text) #kiritilgan xabar ning tarjimasi
    dest = detecter(message.text) # ingilizcha yoki uzbekcha anilaydi
    await message.reply(f"Google Translation:\n{fin_translate}")
    
    def ox(string):
        '''biror so'zni Oxford dan pronunseshni va definishnini olib 
        beradigan funksiya yoq bolasa False qaytaradi'''
        nimadur = getdic(string)
        if nimadur:
            response = getdic(string)
        else:
            return False
        return response
    
    
    #bu shartda agar so'z uzbek tilida bo'lsa u ingilizchaga o'tkaziladi va oxforddan qidiriladi
    if dest=='uz':
        ox_out = ox(message.text)
    else:
        ox_out = ox(fin_translate)

    if ox_out.get('audio'):
        await message.answer_voice(ox_out['audio'])
    output = f"{ox_out['definitions']}" if ox_out else 'Bunday so\'z yo\'q!'
    await message.reply(f"Oxford Dictionary:\n{output}")
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)