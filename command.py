from discord.message import Message

class Command():
    """
    Comands class.

    If you want to create a new command you should use this class
    """

    def __init__(self, content: str = None,
                 alt: str = '',
                 description: str = 'Sin descripción aún, pregúntale al develper chancado que lo creó'):
        """
        Init command
        """
        if content is None:
            raise Exception

        self.content = content
        self.description = description
        self.alt = alt

    async def on_triggered(self, message: Message):
        """
        This function should be overrated
        """
        print("This function should be overrated")
        pass

    def __str__(self):
        string = f"""\nComando: {self.content}\nDescripción: {self.description}\nAtajo: {self.alt}
        """
        return string
