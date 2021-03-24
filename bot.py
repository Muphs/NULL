#imports
import discord
from discord import user
from discord import embeds
from discord import message
from discord.ext import commands
import aiohttp
import asyncio
import logging
import time
from discord import ext
from discord.ext import tasks
from dotenv import load_dotenv
import os
import random
import json
import requests
from discord import member
from discord import Embed
from discord.utils import get
import string

#variables
load_dotenv('.env')
check = '☑️'
description = (os.getenv('DESCRIPTION'))
color = 0xff9efc
thumbnail = 'https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif'
thumbnail_small = 'https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif'
prefix = (os.getenv('PREFIX'))
prefix2 = (os.getenv('PREFIX2'))
#variables.env
#description = (os.getenv('DESCRIPTION'))
#color = (os.getenv('COLOR'))
#thumbnail = (os.getenv('THUMBNAIL'))
#thumbnail_small = (os.getenv('THUMBNAIL_SMALL'))
#prefix = (os.getenv('PREFIX'))
#prefix2 = (os.getenv('PREFIX2'))
#facts_list = (os.getenv('FACTS_LIST'))
#greetings_list = (os.getenv('GREETINGS_LIST'))
#response_list = (os.getenv('RESPONSE_LIST'))
#anime_list = (os.getenv('ANIME_LIST'))
#zerotwo_list = (os.getenv('ZEROTWO_LIST'))
#ichigo_list = (os.getenv('ICHIGO_LIST'))
#bunnygirl_list = (os.getenv('BUNNYGIRL_LIST'))
#todoroki_list = (os.getenv('TODOROKI_LIST'))
#hamster_list = (os.getenv('HAMSTER_LIST'))
#headout_list = (os.getenv('HEADOUT_LIST'))
#roast_list = (os.getenv('ROAST_LIST'))
#pickup_list = (os.getenv('PICKUP_LIST'))
#slap_list = (os.getenv('SLAP_LIST'))
#slapresponse_list = (os.getenv('SLAPRESPONSE_LIST'))
#hug_list = (os.getenv('HUG_LIST'))
#hugresponse_list = (os.getenv('HUGRESPONSE_LIST'))
#kiss_list = (os.getenv('KISS_LIST'))
#kissresponse_list = (os.getenv('KISSRESPONSE_LIST'))
#compliment_list = (os.getenv('COMPLIMENT_LIST'))
#frog_list = (os.getenv('FROG_LIST'))
#jdm_list = (os.getenv('JDM_LIST'))

#quote
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#client
client = discord.Client()
client = commands.Bot(command_prefix = '%%', case_insensitive=True)
bot = commands.Bot(command_prefix='%%', case_insensitive=True)
Bot = commands.Bot(command_prefix = '%%', case_insensitive=True)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Streaming(name=(os.getenv('STREAM')), url=(os.getenv('STREAM_URL'))))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#commands
#hello
    if message.content.startswith((prefix) + 'hello') or message.content.startswith((prefix2) + 'hello'):
        lucky_num = random.randint(0,len(greetings_list) - 1)
        embed=discord.Embed(title=((greetings_list[lucky_num]) + '!'), color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#info
#ping
    if message.content.startswith((prefix) + 'ping') or message.content.startswith((prefix2) + 'ping'):
        embed=discord.Embed(title="Pong! :ping_pong:", color=(color), description=(f'Ponged back in ``{round(client.latency * 1000)}ms``'))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#add bot
    if message.content.startswith((prefix) + 'addbot') or message.content.startswith((prefix2) + 'addbot'):
        embed=discord.Embed(title="Add me to your server by clicking this link!", color=(color))
        embed.add_field(name="https://bit.ly/null-bot-add", value="‎‎‎‎‎‎‎ ", inline=False)
        embed.add_field(name="Notice:", value="NULL. Is still in the development, which may cause commands to not work and the bot to be offline from now and then with no schedule.", inline=False)
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#join server
    if message.content.startswith((prefix) + 'joinserver') or message.content.startswith((prefix2) + 'joinserver'):
        embed=discord.Embed(title="Join my server by clicking this link", color=(color))
        embed.add_field(name="https://bit.ly/null-bot-join", value="‎‎‎‎‎‎‎ ", inline=False)
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#botver
    if message.content.startswith((prefix) + 'botver') or message.content.startswith((prefix2) + 'botver'):
        embed=discord.Embed(title="I am currently on Development version 2.0 Open Beta!", color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)
#info end


#8ball
    if message.content.startswith((prefix) + "8ball") or message.content.startswith((prefix2) + '8ball'):
        lucky_num = random.randint(0,len(response_list)-1)
        embed=discord.Embed(title=(response_list[lucky_num]), color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#compliment
    if message.content.startswith((prefix) + "compliment") or message.content.startswith((prefix2) + 'compliment'):
        lucky_num = random.randint(0,len(compliment_list)-1)
        embed=discord.Embed(title=(compliment_list[lucky_num]), color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#pickupline
    if message.content.startswith((prefix) + "pickupline") or message.content.startswith((prefix2) + 'pickupline'):
        lucky_num = random.randint(0,len(pickup_list)-1)
        embed=discord.Embed(title=(pickup_list[lucky_num]), color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#roast
    if message.content.startswith((prefix) + "roast") or message.content.startswith((prefix2) + 'roast'):
        lucky_num = random.randint(0,len(roast_list)-1)
        embed=discord.Embed(title=(roast_list[lucky_num]), color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#mario judah
    if message.content.startswith((prefix) + "milkyeet") or message.content.startswith((prefix2) + 'milkyeet'):
        embed=discord.Embed(title='YEEEEEEEEEEEEEEEEEEEEET', color=(color))
        embed.set_image(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/mario-judah-throws-milk-_-m2WjP9Gx6yHOB0J1-w1370.gif')
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#anime
#cuteanime
    if message.content.startswith((prefix) + "cuteanime") or message.content.startswith((prefix2) + 'cuteanime'):
        lucky_num = random.randint(0,len(anime_list)-1)
        embed=discord.Embed(title='Awww', color=(color))
        embed.set_image(url=(anime_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#zero two
    if message.content.startswith((prefix) + "zerotwo") or message.content.startswith((prefix2) + 'zerotwo'):
        lucky_num = random.randint(0,len(zerotwo_list)-1)
        embed=discord.Embed(title='Awww', color=(color))
        embed.set_image(url=(zerotwo_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#todoroki
    if message.content.startswith((prefix) + "todoroki") or message.content.startswith((prefix2) + 'todoroki'):
        lucky_num = random.randint(0,len(todoroki_list)-1)
        embed=discord.Embed(title='Awww', color=(color))
        embed.set_image(url=(todoroki_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#ichigo
    if message.content.startswith((prefix) + "ichigo") or message.content.startswith((prefix2) + 'ichigo'):
        lucky_num = random.randint(0,len(ichigo_list)-1)
        embed=discord.Embed(title='Awww', color=(color))
        embed.set_image(url=(ichigo_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#bunnygirl
    if message.content.startswith((prefix) + "bunnygirl") or message.content.startswith((prefix2) + 'bunnygirl'):
        lucky_num = random.randint(0,len(bunnygirl_list)-1)
        embed=discord.Embed(title='Awww', color=(color))
        embed.set_image(url=(bunnygirl_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)
#anime end

#slap
    if message.content.startswith((prefix) + "slap ") or message.content.startswith((prefix2) + 'slap '):
        lucky_num = random.randint(0,len(slap_list)-1)
        lucky_num = random.randint(0,len(slapresponse_list)-1)
        embed=discord.Embed(title=(slapresponse_list[lucky_num]), color=(color))
        embed.set_image(url=(slap_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#hug
    if message.content.startswith((prefix) + "hug ") or message.content.startswith((prefix2) + 'hug '):
        lucky_num = random.randint(0,len(hug_list)-1)
        lucky_num = random.randint(0,len(hugresponse_list)-1)
        embed=discord.Embed(title=(hugresponse_list[lucky_num]), color=(color))
        embed.set_image(url=(hug_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#kiss
    if message.content.startswith((prefix) + "kiss ") or message.content.startswith((prefix2) + 'kiss '):
        lucky_num = random.randint(0,len(kiss_list)-1)
        lucky_num = random.randint(0,len(kissresponse_list)-1)
        embed=discord.Embed(title=(kissresponse_list[lucky_num]), color=(color))
        embed.set_image(url=(kiss_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True) 

#shrug
    if message.content.startswith((prefix) + "shrug") or message.content.startswith((prefix2) + 'shrug'):
        lucky_num = random.randint(0,len(shrug_list)-1)
        embed=discord.Embed(title='`*shrugs*`', color=(color))
        embed.set_image(url=(shrug_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True) 

#clap
    if message.content.startswith((prefix) + "clap") or message.content.startswith((prefix2) + 'clap'):
        lucky_num = random.randint(0,len(clap_list)-1)
        embed=discord.Embed(title='`*clap*` `*clap*` `*clap*`', color=(color))
        embed.set_image(url=(clap_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True) 

#head out
    if message.content.startswith((prefix) + "headout") or message.content.startswith((prefix2) + 'headout'):
        lucky_num = random.randint(0,len(headout_list)-1)
        embed=discord.Embed(title=(headout_list[lucky_num]), color=(color))
        embed.set_image(url='https://media1.tenor.com/images/c57c8725cfdb74251c392e0ca46753ba/tenor.gif?itemid=15194343')
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#hamster
    if message.content.startswith((prefix) + "hamster") or message.content.startswith((prefix2) + 'hamster'):
        lucky_num = random.randint(0,len(hamster_list)-1)
        embed=discord.Embed(title='Awww', color=(color))
        embed.set_image(url=(hamster_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#how sus
    if message.content == ((prefix) + 'howsus') or message.content == ((prefix2) + 'howsus'):
          sus = random.randint(0, 100)
          embed=discord.Embed(title=(str(sus)) + "% sus!", color=(color))
          embed.set_footer(text=(description))
          embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
          await message.reply(embed=embed, mention_author=True)

    if message.content.startswith((prefix) + 'howsus ') or message.content.startswith((prefix2) + 'howsus '):
          sus = random.randint(30, 100)
          embed=discord.Embed(title=(str(sus)) + "% sus!", color=(color))
          embed.set_footer(text=(description))
          embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
          await message.reply(embed=embed, mention_author=True)

#how gay
    if message.content == ((prefix) + 'howgay') or message.content == ((prefix2) + 'howgay'):
          gay = random.randint(0, 100)
          embed=discord.Embed(title=(str(gay)) + "% gay :gay_pride_flag:", color=(color))
          embed.set_footer(text=(description))
          embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
          await message.reply(embed=embed, mention_author=True)

    if message.content.startswith((prefix) + 'howgay ')  or message.content.startswith((prefix2) + 'howgay '):
          gay = random.randint(30, 100)
          embed=discord.Embed(title=(str(gay)) + "% gay :gay_pride_flag:", color=(color))
          embed.set_footer(text=(description))
          embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
          await message.reply(embed=embed, mention_author=True)

#iq
    if message.content == ((prefix) + 'iq') or message.content == ((prefix2) + 'iq'):
          iq = random.randint(0, 1000)
          embed=discord.Embed(title=(str(iq)) + " IQ", color=(color))
          embed.set_footer(text=(description))
          embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
          await message.reply(embed=embed, mention_author=True)

    if message.content.startswith((prefix) + 'iq ') or message.content.startswith((prefix2) + 'iq '):
          iq = random.randint(0, 200)
          embed=discord.Embed(title=(str(iq)) + " IQ", color=(color))
          embed.set_footer(text=(description))
          embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
          await message.reply(embed=embed, mention_author=True)

#inspire
    if message.content.startswith((prefix) + "inspire") or message.content.startswith((prefix2) + 'inspire'):
        quote = get_quote()
        embed=discord.Embed(title=(quote), color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#randomimage
    if message.content.startswith((prefix) + "randomimage") or message.content.startswith((prefix2) + 'randomimage'):
        picgen = random.randint(0, 999999999999999999999999999999999999999999999999999999)
        embed=discord.Embed(title=' ', color=(color))
        embed.set_image(url='https://picsum.photos/seed/' + (str(picgen)) + '/3840/2160')
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#frog
    if message.content.startswith((prefix) + "frog") or message.content.startswith((prefix2) + 'frog'):
        lucky_num = random.randint(0,len(frog_list)-1)
        embed=discord.Embed(title='Awww', color=(color))
        embed.set_image(url=(frog_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#randomjdm
    if message.content.startswith((prefix) + "jdm") or message.content.startswith((prefix) + 'randomjdm') or message.content.startswith((prefix2) + 'jdm')  or message.content.startswith((prefix2) + 'randomjdm'):
        lucky_num = random.randint(0,len(jdm_list)-1)
        embed=discord.Embed(title=' ', color=(color))
        embed.set_image(url=(jdm_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#randomfact
    if message.content.startswith((prefix) + "randomfact") or message.content.startswith((prefix2) + 'randomfact'):
        factapi = requests.get('https://useless-facts.sameerkumar.website/api')
        json_data = json.loads(factapi.text)
        fact = json_data['data']
        embed=discord.Embed(title=(fact), color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#Covid
    if message.content.startswith((prefix) + "covid") or message.content.startswith((prefix2) + 'covid'):
        covid = requests.get('https://api.covid19api.com/world/total')
        json_data = json.loads(covid.text)
        CovidConfirmed = json_data['TotalConfirmed']
        CovidDeaths = json_data['TotalDeaths']
        CovidRecovered = json_data['TotalRecovered']
        embed=discord.Embed(title='COVID19 Info.', color=(color))
        embed.set_thumbnail(url=(thumbnail))
        embed.add_field(name=("{:,}".format(CovidConfirmed)), value="Confirmed cases.", inline=True)
        embed.add_field(name=("{:,}".format(CovidRecovered)), value="Recovered cases.", inline=True)
        embed.add_field(name=("{:,}".format(CovidDeaths)), value="Deaths.", inline=True)
        embed.set_footer(text=(description))
        await message.reply(embed=embed, mention_author=True)

#meme
    if message.content.startswith((prefix) + 'meme') or message.content.startswith((prefix2) + 'meme'):
        meme = requests.get('https://meme-api.herokuapp.com/gimme')
        json_data = json.loads(meme.text)
        memeurl = json_data['url']
        memetitle = json_data['title']
        memensfw = json_data['nsfw']
        embed=discord.Embed(title=(memetitle), color=(color))
        embed.set_image(url=(memeurl))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)
        if memensfw == 'true':
            return    

#weather
    if message.content.startswith((prefix) + 'weather') or message.content.startswith((prefix) + 'randomweather') or message.content.startswith((prefix2) + 'weather') or message.content.startswith((prefix2) + 'randomweather'):
        city_list = ['Mexico', 'London', 'Norway', 'Sydney', 'India', 'Shanghai', 'Tokyo', 'Dubai', 'Argentina', 'Ecuador', 'Egypt']
        lucky_num = random.randint(0,len(city_list) - 1)
        weatherapi = requests.get('https://api.weatherapi.com/v1/current.json?key=' + (os.getenv('API_KEY')) + '&q=' + (city_list[lucky_num]))# + '&aqi=yes'
        json_data = json.loads(weatherapi.text)
        temp_c = json_data['current']['temp_c']
        temp_f = json_data['current']['temp_f']
        condition = json_data['current']['condition']['text']
        icon = json_data['current']['condition']['icon']
        wind_mph = json_data['current']['wind_mph']
        wind_kph = json_data['current']['wind_kph']
        wind_degree = json_data['current']['wind_degree']
        wind_dir = json_data['current']['wind_dir']
        pressure_in = json_data['current']['pressure_in']
        precip_mm = json_data['current']['precip_mm']
        feelslike_c = json_data['current']['feelslike_c']
        feelslike_f = json_data['current']['feelslike_f']
        vis_km = json_data['current']['vis_km']
        vis_miles = json_data['current']['vis_miles']
        uv = json_data['current']['uv']
        tz = json_data['location']['tz_id']
        country = json_data['location']['country']
        city = json_data['location']['name']
        embed=discord.Embed(title=(city), color=(color))
        embed.add_field(name="Country", value=(country), inline=True)
        embed.add_field(name="Time Zone", value=(tz), inline=True)
        embed.add_field(name="Temperature °C", value=(temp_c), inline=True)
        embed.add_field(name="Temperature °F", value=(temp_f), inline=True)
        embed.add_field(name="Feels like °C", value=(feelslike_c), inline=True)
        embed.add_field(name="Feels like °F", value=(feelslike_f), inline=True)
        embed.add_field(name="Wind MPH", value=(wind_mph), inline=True)
        embed.add_field(name="Wind KMPH", value=(wind_kph), inline=True)
        embed.add_field(name="Wind Degree", value=(wind_degree), inline=True)
        embed.add_field(name="Wind Direction", value=(wind_dir), inline=True)
        embed.add_field(name="Pressure In", value=(pressure_in), inline=True)
        embed.add_field(name="Precipitation mm", value=(precip_mm), inline=True)
        embed.add_field(name="Visibility KM", value=(vis_km), inline=True)
        embed.add_field(name="Visibility Miles", value=(vis_miles), inline=True)
        embed.add_field(name="UV index", value=(uv), inline=True)
        embed.add_field(name="Condition", value=(condition), inline=False)
        embed.set_image(url='https:' + (icon))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

    if message.content.startswith((prefix) + 'help') or message.content.startswith((prefix2) + 'help'):
        embed=discord.Embed(title='NULL Help.', color=(color))
        embed.add_field(name='Go here for a list of all commands https://bit.ly/null-bot-help', value='‎‎‎‎‎‎‎Prefix: % or N.', inline=False)
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)



response_list = ['100% sure!', 'definitely not', 'no :(', 'yes :)', 'hmmmmmm, idk', 'maybe ask again', 'maybe ask someone else', "definitely!", "As I see it, yes!", "Yes!", "No!", "Very likely!", "Not even close!", "Maybe!", "Very unlikely!", "Ask again later!", "Better not tell you now!", " It is certain!", "My sources say no", "Outlook good!", "Very Doubtful!", "Without a doubt!", 'no:heart:']

anime_list = ["https://media1.tenor.com/images/c925511d32350cc04411756d623ebad6/tenor.gif?itemid=13462237", "https://media1.tenor.com/images/89289af19b7dab4e21f28f03ec0faaff/tenor.gif?itemid=12801687", "https://media1.tenor.com/images/e1f44b9d914ba61cc60efd8d3cf439a5/tenor.gif?itemid=9975267", "https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif", "https://media.tenor.com/images/8f711b12e00bc1816694bf51909f8b8f/tenor.gif", "https://media.tenor.com/images/84e609c97fc79323c572baa4e8486473/tenor.gif", "https://media.tenor.com/images/c67648bdadbece24eed182a401abf576/tenor.gif", "https://media.tenor.com/images/46a74ce6228e7bc535263e1464cce46b/tenor.gif", "https://media.tenor.com/images/a173f1c95d81855afd10d51f3fa277ab/tenor.gif", "https://media.tenor.com/images/e1c9ad053d4aa0471727fbf36c3a3868/tenor.gif", "https://media.tenor.com/images/3f6457f7235edf481d542b8074740401/tenor.gif"]

zerotwo_list = ['https://media.tenor.com/images/4632e943653b0ad278a1fa7b8f49d82c/tenor.gif', 'https://media.tenor.com/images/3e7d551f4edbc139f1372a494eccd01d/tenor.gif', 'https://media.tenor.com/images/e046bd4175889014749d008bef023f25/tenor.gif', 'https://media.tenor.com/images/500953247d7ddda4d87908fa0bb2c7bc/tenor.gif', 'https://media.tenor.com/images/2e094b3c1f5bf047698dea434416d080/tenor.gif', 'https://media.tenor.com/images/09df52e29a5506287cd76fb4abafa2cc/tenor.gif', 'https://media.tenor.com/images/4f5f2d78f721fc36e10f4e5e2c340f47/tenor.gif', 'https://media.tenor.com/images/7691590d6ac021b483c39dfa794e2a1c/tenor.gif', 'https://64.media.tumblr.com/d03212d8697607c82bb85db886ee92af/tumblr_p2z0hgMv3g1wd81ruo1_540.gifv']

ichigo_list = ['https://media.tenor.com/images/d1fc46f2d0fd52740711b80b80a3c081/tenor.gif', 'https://media.tenor.com/images/b7687ce05975ad1d5c7ed52717e62f09/tenor.gif', 'https://data.whicdn.com/images/325037756/original.gif']

bunnygirl_list = ['https://media1.tenor.com/images/be4bfaaa1458ec4d4231938851cf085b/tenor.gif?itemid=19678646', 'https://media1.tenor.com/images/37439858992a315486549b6136f8d74f/tenor.gif?itemid=17742393', 'https://media1.tenor.com/images/58a14f9ec0549c516134ab9940e871cd/tenor.gif?itemid=19611956', 'https://media1.tenor.com/images/567ba9e70f306c5ce6432377840437d3/tenor.gif?itemid=14746195', 'https://media1.tenor.com/images/24408dbd5bf503ba838e5b9a65bd14e7/tenor.gif?itemid=13458967', 'https://media1.tenor.com/images/5f3d0649a01125104a08894fa673af35/tenor.gif?itemid=15988113', 'https://media1.tenor.com/images/64b2de700d17667c45d3bf34e316a29c/tenor.gif?itemid=20119299', 'https://media1.tenor.com/images/d3b0bf5cda58616be62ec013ca75a38e/tenor.gif?itemid=15988109']

todoroki_list = ['https://pa1.narvii.com/6894/c584fe56b8dde82ac901aeb8e359cb2e157c3bdfr1-533-300_hq.gif', 'https://media1.tenor.com/images/30638e057d7c84c963619c3f9ab2a3df/tenor.gif?itemid=18024441', 'https://img.wattpad.com/e366789b1d68a2190987c27b2378395b6c0c7d66/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f3152537645325f4f32366f6155673d3d2d3736373439353134382e313562376137353763303434343138363934363130373235393332302e676966?s=fit&w=720&h=720', 'https://i.pinimg.com/originals/2e/31/93/2e31935a326bdff0e6d1b91ae03d607f.gif', 'https://p.favim.com/orig/2018/08/01/boku-no-hero-academia-my-hero-academia-todoroki-shouto-Favim.com-6107451.gif']

hamster_list = ['https://wallpaperaccess.com/full/1646379.jpg', 'https://i.pinimg.com/736x/f4/44/e7/f444e7650cfec94d5b4b8a3b4e5736f3.jpg', 'https://www.irishtimes.com/polopoly_fs/1.3521320.1528297311!/image/image.jpg_gen/derivatives/ratio_1x1_w1200/image.jpg', 'https://s7d2.scene7.com/is/image/PetSmart/5081325', 'https://www.vin.com/AppUtil/Image/handler.ashx?imgid=4476518&w=325&h=323', 'https://static.maskokotas.com/blog/wp-content/uploads/2020/01/hamster-cuidados-manejo.jpg', 'https://i.natgeofe.com/n/bc0b53c1-e57e-4708-b592-f11e6ef855c0/european-hamsters-1.jpg?w=636&h=424', 'https://www.wittemolen.com/sites/default/files/styles/full_width/public/slides/SLIDER-Hamster.jpg?itok=t7h_LCJE', 'https://i.pinimg.com/originals/7e/b7/45/7eb745f90461e87655b755eaea1c1d41.jpg', 'https://www.parksidevets.com/pets/wp-content/uploads/sites/2/2019/05/parksite-vets-Hamster-care.jpg', 'https://www.omlet.com/images/originals/Russian_winter_white_pouches.jpg', 'https://www.burgesspetcare.com/wp-content/uploads/2020/02/hamster-diets.jpg']

headout_list = ['cya', 'peace out', 'stay safe', 'ttyl', 'have fun', 'see you later', 'be happy :)']

roast_list = ['You’re the reason God created the middle finger.', 'You’re a grey sprinkle on a rainbow cupcake.', 'If your brain was dynamite, there wouldn’t be enough to blow your hat off.', 'You are more disappointing than an unsalted pretzel.', 'someday you’ll go far, stay there', 'Light travels faster than sound which is why you seemed bright until you spoke.', 'You have so many gaps in your teeth it looks like your tongue is in jail.', 'I wasn’t born with enough middle fingers to let you know how I feel about you', 'If I wanted to kill myself id climb your ego and jump to your IQ', 'Your face makes onions cry.', 'I would love to insult you, but I’m afraid I won’t do as well as nature did', 'If you’re going to be two-faced, at least make one of them pretty.', 'whenever you swim, you just add another piece of trash to the ocean', 'Zombies eat brains, you’re safe']

pickup_list = ["Even if there was no gravity, i'd still fall for you", "Do you like raisins? How do you feel about a date?", "If I could rearrange the alphabet, I’d put ‘U’ and ‘I’ together.", "If you were a Transformer… you’d be Optimus Fine.", "Are you a parking ticket? Because you’ve got FINE written all over you.", "I'm no photographer, but I can picture us together.", "Are you related to Jean-Claude Van Damme? Because Jean-Claude Van Damme you’re sexy!", "are you from Tenesse? cus you are the only 10 i see", "Baby, if you were words on a page, you’d be fine print.", "You must be a high test score, because I want to take you home and show you to my mother", "I was blinded by your beauty; I’m going to need your name and phone number for insurance purposes.", "I was wondering if you had an extra heart. Because mine was just stolen.", "Is your name Google? Because you have everything I’ve been searching for.", "You’re so gorgeous you made me forget what my pick up line was", "Im learning of important dates in history, wanna be one?", "i must be in a museum, because you are truly a work of art", "If you cant live without something, it should be free. I can't live without you, so, when are you free?"]

slap_list = ['https://media.tenor.com/images/1d8edce282f3e36abc6b730357d3cea2/tenor.gif', 'https://media.tenor.com/images/47698b115e4185036e95111f81baab45/tenor.gif', 'https://media.tenor.com/images/01cd05bde1ebcdd0efa9648db9c9e02b/tenor.gif', 'https://media.tenor.com/images/dc569ca06234b85e11177e4d5ac55e21/tenor.gif', 'https://media.tenor.com/images/4abceefdd1c6713471486ad4369f63e1/tenor.gif', 'https://media.tenor.com/images/39cf2806683782606bd6185528bf3fba/tenor.gif', 'https://media.tenor.com/images/daa9848169a4919967766555a8958fbb/tenor.gif', 'https://media.tenor.com/images/3d708f9789961e31a84aae0395361747/tenor.gif', 'https://media.tenor.com/images/ad8a2b661e5c9d69e90a46e587231f23/tenor.gif', 'https://media.tenor.com/images/1d65e3710ac1e73647dafebe2f4727d9/tenor.gif', 'https://media.tenor.com/images/5eaa11874c0cc46d4d6aeb929066766a/tenor.gif', 'https://media.tenor.com/images/d76151f7a50376264fe599165aea066d/tenor.gif', 'https://media.tenor.com/images/507022c3e5862960cc363f330b94d391/tenor.gif']

slapresponse_list = ['oof, that must hurt', 'they must be dead', 'looks like someone got slapped lol']

hug_list = ['https://media.tenor.com/images/bb67bef5f54d0191b7e2d3c1fd6e4bd3/tenor.gif', 'https://media.tenor.com/images/a9bb4d55724484be94d13dd94721a8d9/tenor.gif', 'https://media.tenor.com/images/a9730f44f28d959abb4c5b31edc77de8/tenor.gif', 'https://media.tenor.com/images/ca88f916b116711c60bb23b8eb608694/tenor.gif', 'https://media.tenor.com/images/1ca37ea5d3ec66ea08893d8679c04ae1/tenor.gif', 'https://media.tenor.com/images/9fe95432f2d10d7de2e279d5c10b9b51/tenor.gif', 'https://media.tenor.com/images/f2d41b50c49426ea42411f14779a7c1c/tenor.gif', 'https://media.tenor.com/images/8d33eeee359d0453de52c5779dd23c46/tenor.gif', 'https://media.tenor.com/images/2e1d34d002d73459b6119d57e6a795d6/tenor.gif', ]

hugresponse_list = ['Awwwww, what a cute hug', 'i feel lonely <:apple_plead:812381767432536125>']

kiss_list = ['https://media.tenor.com/images/6702ca08b5375a74b6b9805382021f73/tenor.gif', 'https://media.tenor.com/images/924c9665eeb727e21a6e6a401e60183b/tenor.gif', 'https://media.tenor.com/images/197df534507bd229ba790e8e1b5f63dc/tenor.gif', 'https://media.tenor.com/images/21fed1c94754d21acdbccd52adfb53d0/tenor.gif', 'https://media.tenor.com/images/7b50048d76f76a8e5b3d8fc5a3fc6a21/tenor.gif', 'https://media.tenor.com/images/1f9175e76488ebf226de305279151752/tenor.gif', 'https://media.tenor.com/images/29b22bb26ecc0943c95b9a1be81d3054/tenor.gif', 'https://media.tenor.com/images/25359520a0973f896b002689ed90db8d/tenor.gif', 'https://media.tenor.com/images/7e640ecfea0090dd0e29b998c625c642/tenor.gif', 'https://media.tenor.com/images/48963a8342fecf77d8eabfd2ab2e75c1/tenor.gif', 'https://media.tenor.com/images/45246226e54748be5175ab15206de1c5/tenor.gif', 'https://media.tenor.com/images/822b11c4ab7843229fdd4abf5ccadf61/tenor.gif', 'https://media.tenor.com/images/7fefdf515b268e92554654a115211ce3/tenor.gif']

kissresponse_list = ['I feel lonely <:apple_plead:812381767432536125>', 'I really need a gf <:apple_plead:812381767432536125>']

compliment_list = ['You have the best laugh.', 'Our system of inside jokes is so advanced that only you and I get it. And I like that.', 'Your perspective is refreshing.', 'You deserve a hug right now.', 'You’re more helpful than you realize.', 'You have a great sense of humor.', 'On a scale from 1 to 10, you’re an 11.', 'You’re even more beautiful on the inside than you are on the outside.', 'If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.', 'Your ability to recall random factoids at just the right time is impressive.', 'You may dance like no one’s watching, but everyone’s watching because you’re an amazing dancer!', 'You’re more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)', 'Everyday is just BLAH when I don’t see you fr! ', 'If you were a box of crayons, you’d be the giant name-brand one with the built-in sharpener.', 'Everyone gets knocked down sometimes, but you always get back up and keep going.', 'You’re gorgeous — and that’s the least interesting thing about you, too.', 'If you were a scented candle they’d call it Perfectly Imperfect (and it would smell like summer).']

frog_list = ["https://ih1.redbubble.net/image.1448785672.7225/st,small,507x507-pad,600x600,f8f8f8.jpg", "https://media.istockphoto.com/vectors/cute-frog-cartoon-hand-drawn-style-vector-id1146849256", "https://reneelertzman.com/wp-content/uploads/2016/03/cute-little-green-frog-peeking-out-from-behind-PT9JUFJ.jpg", "https://ih1.redbubble.net/image.1490694325.8717/fposter,small,wall_texture,product,750x1000.jpg", "https://www.crushpixel.com/big-static12/preview4/cute-frog-seamless-pattern-background-1094038.jpg", "https://www.crushpixel.com/big-static12/preview4/cute-frog-seamless-pattern-background-1094038.jpg", "https://media.discordapp.net/attachments/791400172209963058/812447792114827274/IMG_20210217_180127_963.jpg", "http://onebigphoto.com/uploads/2014/09/hello-i-am-cute-frog.jpg", "https://imagesvc.meredithcorp.io/v3/mm/image?q=85&c=sc&poi=face&w=1503&h=1503&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F20%2F2020%2F01%2Ffrog-trio-6.jpg", "https://media.discordapp.net/attachments/791400172209963058/812448117622046720/2lqtt9abx4561.png?width=371&height=500", "https://i.pinimg.com/originals/5c/a6/18/5ca6189bfca950c74ad266c30e587bb9.jpg", "http://1.bp.blogspot.com/-BkUS1SGdmLA/TpEiyhFFC4I/AAAAAAAAB3c/91Rh3vtHNT8/s1600/Cute-Frog-1.jpg", "https://media.discordapp.net/attachments/791400172209963058/812449043791085598/8mi859yc14251.png"]

jdm_list = ['https://images-ext-1.discordapp.net/external/52h-vS9a2mw65Fl7ITo7TuD0wdiGeneuTi0WlqIKays/https/soymotor.com/sites/default/files/imagenes/noticia/toyota-supra.jpg', 'https://images-ext-2.discordapp.net/external/kDofouMxYFqVGrwlHX3ZSy8l1d1L28zyKD6evy-EFMA/https/besthqwallpapers.com/Uploads/16-11-2019/111977/thumb2-nissan-s30-nissan-fairlady-z-tuning-datsun-240z-japanese-cars.jpg', 'https://images-ext-2.discordapp.net/external/OvGDRXylwLmqiccdMXBuPB76YlNE3eEpCJIC33AfgJc/https/www.motorbiscuit.com/wp-content/uploads/2020/10/1986-JDM-Toyota-AE86-Sprinter-Trueno-GT-Apex.jpg', 'https://images-ext-1.discordapp.net/external/mWPXDCBHCJPP-BPzgy10u-hefrtGcwI6QoJg405nTD0/https/i.pinimg.com/originals/88/83/bd/8883bd844c3046df557c7381d0633626.jpg', 'https://images-ext-2.discordapp.net/external/XCCVt9Kwv25RQV68Ad_1F4QnvbsELNGPvxrv9jpI_20/https/i.pinimg.com/originals/67/ff/ea/67ffeab000d8e7033e60360ea0a3bcce.jpg', 'https://images-ext-1.discordapp.net/external/ymHMBTo2uS6Ujq3okVeB2MEN6HLMmaTF3CavIAhJkXA/https/frenomotor.com/files/2015/04/skyline-paul-walker.jpg']

shrug_list = ['https://media1.tenor.com/images/34b67ecddde773b30dbe962d14ff27c7/tenor.gif?itemid=20668021', ]

clap_list = ['https://media1.tenor.com/images/7460a26a07ef24d696eaac0b0ff4d5bf/tenor.gif?itemid=16461487', 'https://media.tenor.com/images/ba246f4d3f2845cac07466ab3d013279/tenor.gif', 'https://media.tenor.com/images/657f0c243282921245c0b9f4b1525c1b/tenor.gif', 'https://media.tenor.com/images/2cf9843ed2489b97be6ca65acd40b55f/tenor.gif', 'https://media.tenor.com/images/07908bbd4b8336d826c733de9b2f2988/tenor.gif', 'https://media.tenor.com/images/18ae86fcb295c6d30028dedf7a946970/tenor.gif', 'https://media.tenor.com/images/9f94b89d628518c67808ebadba924306/tenor.gif', 'https://media.tenor.com/images/bd235c84724d5eb04b5cfe39028e936c/tenor.gif']

greetings_list = ['Hi', 'Hey', 'Sup', 'Hello']

#run client
client.run(os.getenv('BOT_TOKEN'))
