"""
Command that return a random cat image
"""

from command import Command
import json
import os
from discord import Embed
import requests
from discord.message import Message


class Cat(Command):

    async def on_triggered(self, message: Message):
        """
        Return a message an image of a cat
        :return:Embed message
        """
        image_url = self.get_cat_image_url()

        await message.channel.send(
                    embed=self.get_embed("Holis", image_url)
                )

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
