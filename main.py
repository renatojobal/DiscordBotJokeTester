import os

import discord

import config
from keep_alive import keep_alive

client = discord.Client()


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

    if message.content.startswith(config.COMMAND_KEY):
        """
        We dont want the bot to be scanning other messages that do not start with the command
        """

        for command in config.registered_commands:
            if command.content == message.content or command.alt == message.content:
                await command.on_triggered(message)
                return

        # Handle here if the commando is not registered
        help_message = '```\nComandos disponibles:\n'
        for command in config.registered_commands:
            help_message += command.__str__()
        help_message += '```'

        await message.channel.send(
            help_message
        )


keep_alive()

token = os.environ['TOKEN']

client.run(token)
