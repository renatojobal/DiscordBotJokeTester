import os
from test_joke import Test_Joke
from random_sys_image import Random_Sys_Image
from cat import Cat


COMMAND_KEY = '%'

# Initialize your commands here
test_joke = Test_Joke(
  content='%test_joke',
                      alt='%t',
                      description='Devuelve una medición sobre el chiste anterior.'
                      )

random_sys_image = Random_Sys_Image(
    content='%random',
    alt='%r',
    description='Devuelve una imagen random de sistemas'
)

cat_image = Cat(
    content='%cat',
    alt='%c',
    description='Imagen de un gatito'
)


# Register your commands here
registered_commands = [
    test_joke,
    random_sys_image,
    cat_image
]

