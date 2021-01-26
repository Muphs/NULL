#imports
import discord
from discord.ext import commands
import aiohttp
import asyncio
import logging
import time
from discord import ext
from discord.ext import tasks
from dotenv import load_dotenv
import os
#imports end

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))


@client.event

async def on_message(message):
    if message.author == client.user:
        return


#hello
    if message.content.startswith('%hello'):
        embed=discord.Embed(title="Hello!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/null-logo-AMqGP9bxMlCn3xXy-w1370.jpg')
        await message.channel.send(embed=embed)


#add bot
    if message.content.startswith('%addbot'):
        embed=discord.Embed(title="Add me to your server by clicking this link", color=0xff9efc)
        embed.add_field(name="https://bit.ly/null-bot-add", value="‎‎‎‎‎‎‎ ", inline=False)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/null-logo-AMqGP9bxMlCn3xXy-w1370.jpg')
        await message.channel.send(embed=embed)


#botver
    if message.content.startswith('%botver'):
        embed=discord.Embed(title="I am currently on Development version 0.22!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/null-logo-AMqGP9bxMlCn3xXy-w1370.jpg')
        await message.channel.send(embed=embed)


#icy
    if message.content.startswith('%is Icy the best and cutest in the world?'):
        embed=discord.Embed(title="I HOPE SO!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/null-logo-AMqGP9bxMlCn3xXy-w1370.jpg')
        await message.channel.send(embed=embed)

#icy
    if message.content.startswith("%will Icy be Muphs' boo?"):
        embed=discord.Embed(title="OF COURSE SHE IS!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/null-logo-AMqGP9bxMlCn3xXy-w1370.jpg')
        await message.channel.send(embed=embed)


#icy
    if message.content.startswith("%should i rethink my life?"):
        embed=discord.Embed(title="Yes!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/null-logo-AMqGP9bxMlCn3xXy-w1370.jpg')
        await message.channel.send(embed=embed)


#help
    if message.content.startswith('%help'):
        embed=discord.Embed(title="NULL.™ Help", color=0xff9efc)
        #hello
        embed.add_field(name="%hello", value="You're greeted by me!", inline=False)
        #add bot
        embed.add_field(name="%addbot", value="Add me to your server!", inline=False)
        #bot version
        embed.add_field(name="%botver", value="Get to know my current software version!", inline=False)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/null-logo-AMqGP9bxMlCn3xXy-w1370.jpg')
        await message.channel.send(embed=embed)



#credentials
load_dotenv('.env')
#credentials end

#run client
client.run(os.getenv('BOT_TOKEN'))
#run cliend end