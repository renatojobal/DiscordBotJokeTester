from command import Command
import random
from discord import Embed
from discord.message import Message

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

    async def on_triggered(self, message: Message):
        """
        Return a message of a joke
        :return:Embed message
        """
        answer = self.get_answer_to_joke()


        await message.channel.send(
                    embed=self.get_embed(answer)
                )

    def get_answer_to_joke(self):
        return random.choice(jokes_answer)


    def get_embed(self, answer: str):
        embed = Embed(
            title=answer,
            message=answer,
            description="Un gatito :3")
        return embed
