import discord
import os
from decouple import config
from keep_alive import keep_alive
import random
import json

client = discord.Client()

jokes_answer = [
    'Mas o menos tu bromita 7/10',
    '¡Oigan todos! Master bromas aqui presente',
    '¿Acaso aprendiste de Jucaritas? 10/10',
    'Uff +1000 lince',
    'Se te cayeron tus zapatos de payaso',
    '¿Fue chiste? Pa reirme',
    'Bangaran',
    'Tatai guambra mushpa',
    'Me alegraste el día',
    '¡Tu Joke-Fu es realmente impresionante!',
    '¿Sacas tus chiste del libreto de Auron Play?',
    'No entendí esa referencfia',
    'Don comediante'
]


def get_answer_to_joke():
    return random.choice(jokes_answer)



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test_joke'):

        answer = get_answer_to_joke()

        await message.channel.send(answer)


keep_alive()

token = os.environ['TOKEN']
# token = config('TOKEN') using local enviroment with decouple


client.run(token)
