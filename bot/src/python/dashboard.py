print("Web dashboard is running")
"""
█▄░█ █░█ █░░ █░░   █░█░█ █▀▀ █▄▄   █▀▄ ▄▀█ █▀ █░█ █▄▄ █▀█ ▄▀█ █▀█ █▀▄
█░▀█ █▄█ █▄▄ █▄▄   ▀▄▀▄▀ ██▄ █▄█   █▄▀ █▀█ ▄█ █▀█ █▄█ █▄█ █▀█ █▀▄ █▄▀"""



#//imports
from quart import Quart, render_template, request, redirect
from quart.templating import render_template

app = Quart(__name__)

@app.route('/')
async def index():
    return await render_template('index.html', hello='world')

app.run(debug=True)
