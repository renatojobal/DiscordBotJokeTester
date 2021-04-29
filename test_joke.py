from command import Command
import random
import json
import os
from discord import Embed
import requests

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


class Test_Joke(Command):

    def on_triggered(self):
        """
        Return a message of a joke and a image of a cat
        :return:Embed message
        """

    def get_answer_to_joke(self):
        return random.choice(jokes_answer)

    def get_cat_image_url(self):
        url = "https://api.thecatapi.com/v1/images/search?mime_types=png"

        headers = {'x-api-key': os.environ['CAT_API_KEY']}

        response = json.loads(requests.request("GET", url, headers=headers).text)

        image_url = response[0]['url']

        return image_url

    def get_embed(self, answer: str, image_url: str):
        embed = Embed(
            title=answer,
            message=answer,
            description="Un gatito :3")
        embed.set_image(url=image_url)
        return embed
