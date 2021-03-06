from threading import Thread

from flask import Flask

"""
This file is used as a trick to keep the bot running.
You don't need to modify it.
"""

app = Flask('')


@app.route('/')
def home():
    return "Hello. I am alive!"


def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
