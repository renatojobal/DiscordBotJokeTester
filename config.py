import os
from test_joke import Test_Joke
from random_sys_image import Random_Sys_Image
from help_command import HelpCommand

COMMAND_KEY = '%'

# Initialize your commands here
help_command = HelpCommand(
    content='½help',
    alt='%h',
    description='Ayuda'
)
test_joke = Test_Joke(content='%test_joke',
                      alt='%t',
                      description='Devuelve una medición sobre el chiste anterior y una imagen de un gatito')

random_sys_image = Random_Sys_Image(
    content='%random',
    alt='%r',
    description='Devuelve una imagen random de sistemas'
)


# Register your commands here
registered_commands = [
    test_joke,
    random_sys_image,
    help_command
]

