import discord
import os
from decouple import config
from keep_alive import keep_alive
import random
import json
import requests
import io
from PIL import Image

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

def get_cat_image_url():
    url = "https://api.thecatapi.com/v1/images/search?mime_types=png"

    headers = {'x-api-key': os.environ['CAT_API_KEY']}

    response = json.loads(requests.request("GET", url, headers=headers).text)

    image_url = response[0]['url']

    return image_url

def get_embed(answer : str, image_url : str):
  embed = discord.Embed(
    title= answer, 
    message=answer, 
    description="Un gatito :3")
  embed.set_image(url=image_url)
  return embed

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$test_joke'):

        answer = get_answer_to_joke()

        image_url = get_cat_image_url()

        await message.channel.send(
          embed=get_embed(answer, image_url)
        )


keep_alive()

token = os.environ['TOKEN']
# token = config('TOKEN') using local enviroment with decouple


client.run(token)
