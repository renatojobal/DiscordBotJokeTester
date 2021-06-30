from discord import Embed

from command import Command
from discord.message import Message
import random

# Images of System Boys
custom_images = [
    'https://i.imgur.com/HzeRBwr.png',
    'https://i.imgur.com/l2jDnRw.jpg',
    'https://i.imgur.com/ABOL08M.png',
    'https://i.imgur.com/Cf9TzN3.png',
    'https://i.imgur.com/cUxuX0J.png',
    'https://i.imgur.com/ZWhlJV8.jpg',
    'https://i.imgur.com/uSwV1cK.jpg',
    'https://i.imgur.com/oterwxg.jpg',
    'https://i.imgur.com/mImivPA.png',
    'https://i.imgur.com/8QsMNnS.png',
    'https://i.imgur.com/YBtW1Lm.jpg',
    'https://i.imgur.com/avHVI2O.png',
    'https://i.imgur.com/tvCdLKH.png'
]


class Random_Sys_Image(Command):
    """
    Return a random image of the set custom_images
    """

    async def on_triggered(self, message: Message):
        embed = Embed(
            description='Random image')
        embed.set_image(url=random.choice(custom_images))

        await message.channel.send(
                    embed=embed
                )
