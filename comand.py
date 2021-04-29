
class Command:
    """
    Comands class.

    If you want to create a new command you should use this class
    """

    def __init__(self, content:str = None, description:str = 'Sin descripción aún, pregúntale al develper chancado que lo creó'):
        """
        Init command
        """
        if content is None:
            raise Exception

        self.content = content
        self.description = description

    
    def on_triggered():
        """
        This function should be overrited
        """
        pass

    def __str__(self):
        string = f"""\nComando: {self.content}
        Descripción: {self.description}\n
        """
        return string
        




