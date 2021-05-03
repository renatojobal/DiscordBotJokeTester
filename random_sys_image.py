from discord import Embed

from command import Command
from discord.message import Message
import random

# Images of System Boys
custom_images = [
    'https://scontent.floh1-1.fna.fbcdn.net/v/t1.6435-9/83398931_2538985876423421_2627695716503388160_n.jpg?_nc_cat=109&ccb=1-3&_nc_sid=09cbfe&_nc_ohc=sxT918ZJp44AX94jg7S&_nc_ht=scontent.floh1-1.fna&oh=cae3836519615d85537b209d799aac78&oe=60B16A57',
    'https://scontent.floh1-1.fna.fbcdn.net/v/t1.18169-9/12548850_930165383725735_8884847447759217784_n.jpg?_nc_cat=104&ccb=1-3&_nc_sid=174925&_nc_ohc=G14Gb4hgcokAX_aan6I&_nc_ht=scontent.floh1-1.fna&oh=11301e27945f2bbcb570ea2ea72a85d5&oe=60B16D23',
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
