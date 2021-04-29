import discord
import os
from decouple import config
from keep_alive import keep_alive
import random
import json

client = discord.Client()

jokes_answer = [
    'Mas o menos tu bromita 7/10',
    'Oigan todos! Mister bromas aqui presente',
    'Acaso aprendiste de Jucaritas? 10/10',
    'Uff +1000 lince',
    'Ban'
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
client.run(config('TOKEN'))