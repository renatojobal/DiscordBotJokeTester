import discord
import os
from keep_alive import keep_alive
import random
import json
import requests

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

# Images of Sistem Boys
custom_images = [
  'https://scontent.floh1-1.fna.fbcdn.net/v/t1.6435-9/83398931_2538985876423421_2627695716503388160_n.jpg?_nc_cat=109&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=sxT918ZJp44AX94jg7S&_nc_ht=scontent.floh1-1.fna&oh=cae3836519615d85537b209d799aac78&oe=60B16A57',
  'https://scontent.floh1-1.fna.fbcdn.net/v/t1.18169-9/12548850_930165383725735_8884847447759217784_n.jpg?_nc_cat=104&ccb=1-3&_nc_sid=174925&_nc_ohc=G14Gb4hgcokAX_aan6I&_nc_ht=scontent.floh1-1.fna&oh=11301e27945f2bbcb570ea2ea72a85d5&oe=60B16D23'
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

registered_commands = [
    
]


@client.event
async def on_ready():
    """
    Event triggered when bot is ready
    """
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    """
    Event triggered each time when a message is sent in a channel 
    when the bot has access
    """

    # This line prevent the bot to answer itself
    if message.author == client.user:
        return

    # Command $test_joke or %
    if message.content.startswith('$test_joke') or message.content=='%':

        answer = get_answer_to_joke()

        image_url = get_cat_image_url()

        await message.channel.send(
          embed=get_embed(answer, image_url)
        )
    
    if message.content == '%sistemas':
        await message.channel.send(
          embed=get_embed('Testing', random.choice(custom_images))
        )

    if message.content == '%help':
        await message.channel.send(
            "Working..."
        )




# keep_alive()

token = os.environ['TOKEN']


client.run(token)
