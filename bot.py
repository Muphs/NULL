
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
    async def avatar(client, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        


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
        embed=discord.Embed(title="I am currently on Development version 1.75 Open Beta!", color=(color))
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
#anime end

#slap
    if message.content.startswith((prefix) + "slap ") or message.content.startswith((prefix2) + 'slap'):
        lucky_num = random.randint(0,len(slap_list)-1)
        lucky_num = random.randint(0,len(slapresponse_list)-1)
        embed=discord.Embed(title=(slapresponse_list[lucky_num]), color=(color))
        embed.set_image(url=(slap_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#hug
    if message.content.startswith((prefix) + "hug ") or message.content.startswith((prefix2) + 'hug'):
        lucky_num = random.randint(0,len(hug_list)-1)
        lucky_num = random.randint(0,len(hugresponse_list)-1)
        embed=discord.Embed(title=(hugresponse_list[lucky_num]), color=(color))
        embed.set_image(url=(hug_list[lucky_num]))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

#kiss
    if message.content.startswith((prefix) + "kiss ") or message.content.startswith((prefix2) + 'kiss'):
        lucky_num = random.randint(0,len(kiss_list)-1)
        lucky_num = random.randint(0,len(kissresponse_list)-1)
        embed=discord.Embed(title=(kissresponse_list[lucky_num]), color=(color))
        embed.set_image(url=(kiss_list[lucky_num]))
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
    if message.content == ((prefix) + 'howsus') or message.content.startswith((prefix2) + 'howsus'):
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
    if message.content == ((prefix) + 'howgay') or message.content.startswith((prefix2) + 'howgay'):
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
    if message.content == ((prefix) + 'iq') or message.content.startswith((prefix2) + 'iq'):
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
        lucky_num = random.randint(0,len(facts_list)-1)
        embed=discord.Embed(title=(facts_list[lucky_num]), color=(color))
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


#help
    if message.content == (prefix) + 'help' or message.content == (prefix) + 'help ' or message.content == (prefix2) + 'help' or message.content == 'help ':
        embed=discord.Embed(title=("NULL. Help."), color=(color))
        embed.add_field(name="``Fun commands``", value="Use these commands when you're bored!", inline=False)
        embed.add_field(name="``Info``", value="Get miscelanious info on various topics!", inline=False)
        embed.add_field(name="To get commands use ``%help.fun`` or ``%help.info``", value="Commands are case sensitive and lowercase.", inline=False)
        embed.add_field(name="More commands coming soon!", value="|| Coded with :heart: by VOKSEL#8148 ||", inline=False)
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

    if message.content.startswith((prefix) + 'help.fun') or message.content.startswith((prefix2) + 'help.fun'):
        embed=discord.Embed(title=("NULL. Help: Fun commands."), color=(color))
        embed.add_field(name="%8ball (question)", value="Ask the magic 8ball!", inline=False)
        embed.add_field(name="%compliment", value="Feeling sad? <:apple_plead:812381767432536125> get a compliment from me!", inline=False)
        embed.add_field(name="%pickupline", value="Meeting someone new? say a pickup line :smirk:", inline=False)
        embed.add_field(name="%roast", value="Feeling good? imagine getting roasted by a bot :rofl:", inline=False)
        embed.add_field(name="%milkyeet", value="Pretty self explanatory :joy:", inline=False)
        embed.add_field(name="%slap", value="Slap someone else!", inline=False)
        embed.add_field(name="%hug", value="Hug someone with this command <:apple_plead:812381767432536125>", inline=False)
        embed.add_field(name="%kiss", value="I'm starting to feel lonely <:apple_plead:812381767432536125>", inline=False)
        embed.add_field(name="%headout", value="Use this command when you're leaving!", inline=False)
        embed.add_field(name="%howsus", value="How sus are you?", inline=False)
        embed.add_field(name="%howgay", value="How gay are you?", inline=False)
        embed.add_field(name="%inspire", value="Get an inspirational quote for when you're deeling sad!", inline=False)
        embed.add_field(name="%randomimage", value="Need visual inspiration? try this command", inline=False)
        embed.add_field(name="%frog", value="Cute frog images!", inline=False)
        embed.add_field(name="%randomfact", value="Random fun facts!", inline=False)
        embed.add_field(name="%hamster", value="cute hamsters <:apple_plead:812381767432536125>", inline=False)
        embed.add_field(name="%jdm", value="Random JDM car images :hot_face:", inline=False)
        embed.add_field(name="Notice:", value="Commands are case sensitive and lowercase.", inline=False)
        embed.add_field(name="More commands coming soon!", value="|| Coded with :heart: by VOKSEL#8148 ||", inline=False)
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)

    if message.content.startswith((prefix) + 'help.info') or message.content.startswith((prefix2) + 'help.info'):
        embed=discord.Embed(title=("NULL. Help: Info commands."), color=(color))
        embed.add_field(name="%ping", value="Tells you my current ping in miliseconds", inline=False)
        embed.add_field(name="%addbot", value="Add me to your server by running this command and clicking the link!", inline=False)
        embed.add_field(name="%joinserver", value="Join my official server by running this command and clicking the link!", inline=False)
        embed.add_field(name="%botver", value="Tells you my current Software version!", inline=False)
        embed.add_field(name="Notice:", value="Commands are case sensitive and lowercase.", inline=False)
        embed.add_field(name="More commands coming soon!", value="|| Coded with :heart: by VOKSEL#8148 ||", inline=False)
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)
#help end


response_list = ['100% sure!', 'definitely not', 'no :(', 'yes :)', 'hmmmmmm, idk', 'maybe ask again', 'maybe ask someone else', "definitely!", "As I see it, yes!", "Yes!", "No!", "Very likely!", "Not even close!", "Maybe!", "Very unlikely!", "Ask again later!", "Better not tell you now!", " It is certain!", "My sources say no", "Outlook good!", "Very Doubtful!", "Without a doubt!", 'no:heart:']

anime_list = ["https://media1.tenor.com/images/c925511d32350cc04411756d623ebad6/tenor.gif?itemid=13462237", "https://media1.tenor.com/images/89289af19b7dab4e21f28f03ec0faaff/tenor.gif?itemid=12801687", "https://media1.tenor.com/images/e1f44b9d914ba61cc60efd8d3cf439a5/tenor.gif?itemid=9975267", "https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif", "https://media.tenor.com/images/8f711b12e00bc1816694bf51909f8b8f/tenor.gif", "https://media.tenor.com/images/84e609c97fc79323c572baa4e8486473/tenor.gif", "https://media.tenor.com/images/c67648bdadbece24eed182a401abf576/tenor.gif", "https://media.tenor.com/images/46a74ce6228e7bc535263e1464cce46b/tenor.gif", "https://media.tenor.com/images/a173f1c95d81855afd10d51f3fa277ab/tenor.gif", "https://media.tenor.com/images/e1c9ad053d4aa0471727fbf36c3a3868/tenor.gif", "https://media.tenor.com/images/3f6457f7235edf481d542b8074740401/tenor.gif"]

zerotwo_list = ['https://media.tenor.com/images/4632e943653b0ad278a1fa7b8f49d82c/tenor.gif', 'https://media.tenor.com/images/3e7d551f4edbc139f1372a494eccd01d/tenor.gif', 'https://media.tenor.com/images/e046bd4175889014749d008bef023f25/tenor.gif', 'https://media.tenor.com/images/500953247d7ddda4d87908fa0bb2c7bc/tenor.gif', 'https://media.tenor.com/images/2e094b3c1f5bf047698dea434416d080/tenor.gif', 'https://media.tenor.com/images/09df52e29a5506287cd76fb4abafa2cc/tenor.gif', 'https://media.tenor.com/images/4f5f2d78f721fc36e10f4e5e2c340f47/tenor.gif', 'https://media.tenor.com/images/7691590d6ac021b483c39dfa794e2a1c/tenor.gif', 'https://64.media.tumblr.com/d03212d8697607c82bb85db886ee92af/tumblr_p2z0hgMv3g1wd81ruo1_540.gifv']

ichigo_list = ['https://media.tenor.com/images/d1fc46f2d0fd52740711b80b80a3c081/tenor.gif', 'https://media.tenor.com/images/b7687ce05975ad1d5c7ed52717e62f09/tenor.gif', 'https://data.whicdn.com/images/325037756/original.gif']

todoroki_list = ['https://pa1.narvii.com/6894/c584fe56b8dde82ac901aeb8e359cb2e157c3bdfr1-533-300_hq.gif', 'https://media1.tenor.com/images/30638e057d7c84c963619c3f9ab2a3df/tenor.gif?itemid=18024441', 'https://img.wattpad.com/e366789b1d68a2190987c27b2378395b6c0c7d66/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f3152537645325f4f32366f6155673d3d2d3736373439353134382e313562376137353763303434343138363934363130373235393332302e676966?s=fit&w=720&h=720', 'https://i.pinimg.com/originals/2e/31/93/2e31935a326bdff0e6d1b91ae03d607f.gif', 'https://p.favim.com/orig/2018/08/01/boku-no-hero-academia-my-hero-academia-todoroki-shouto-Favim.com-6107451.gif']

hamster_list = ['https://wallpaperaccess.com/full/1646379.jpg', 'https://i.pinimg.com/736x/f4/44/e7/f444e7650cfec94d5b4b8a3b4e5736f3.jpg', 'https://www.irishtimes.com/polopoly_fs/1.3521320.1528297311!/image/image.jpg_gen/derivatives/ratio_1x1_w1200/image.jpg', 'https://s7d2.scene7.com/is/image/PetSmart/5081325', 'https://www.vin.com/AppUtil/Image/handler.ashx?imgid=4476518&w=325&h=323', 'https://static.maskokotas.com/blog/wp-content/uploads/2020/01/hamster-cuidados-manejo.jpg', 'https://i.natgeofe.com/n/bc0b53c1-e57e-4708-b592-f11e6ef855c0/european-hamsters-1.jpg?w=636&h=424', 'https://www.wittemolen.com/sites/default/files/styles/full_width/public/slides/SLIDER-Hamster.jpg?itok=t7h_LCJE', 'https://i.pinimg.com/originals/7e/b7/45/7eb745f90461e87655b755eaea1c1d41.jpg', 'https://www.parksidevets.com/pets/wp-content/uploads/sites/2/2019/05/parksite-vets-Hamster-care.jpg', 'https://www.omlet.com/images/originals/Russian_winter_white_pouches.jpg', 'https://www.burgesspetcare.com/wp-content/uploads/2020/02/hamster-diets.jpg']

headout_list = ['cya', 'peace out', 'stay safe', 'ttyl', 'have fun', 'see you later', 'be happy :)']

roast_list = ['You’re the reason God created the middle finger.', 'You’re a grey sprinkle on a rainbow cupcake.', 'If your brain was dynamite, there wouldn’t be enough to blow your hat off.', 'You are more disappointing than an unsalted pretzel.', 'someday you’ll go far, stay there', 'Light travels faster than sound which is why you seemed bright until you spoke.', 'You have so many gaps in your teeth it looks like your tongue is in jail.', 'I wasn’t born with enough middle fingers to let you know how I feel about you', 'If I wanted to kill myself id climb your ego and jump to your IQ', 'Your face makes onions cry.', 'I would love to insult you, but I’m afraid I won’t do as well as nature did', 'If you’re going to be two-faced, at least make one of them pretty.', 'whenever you swim, you just add another piece of trash to the ocean', 'Zombies eat brains, you’re safe']

pickup_list = ["Even if there was no gravity, i'd still fall for you", "Do you like raisins? How do you feel about a date?", "If I could rearrange the alphabet, I’d put ‘U’ and ‘I’ together.", "If you were a Transformer… you’d be Optimus Fine.", "Are you a parking ticket? Because you’ve got FINE written all over you.", "I'm no photographer, but I can picture us together.", "Are you related to Jean-Claude Van Damme? Because Jean-Claude Van Damme you’re sexy!", "are you from Tenesse? cus you are the only 10 i see", "Baby, if you were words on a page, you’d be fine print.", "You must be a high test score, because I want to take you home and show you to my mother", "I was blinded by your beauty; I’m going to need your name and phone number for insurance purposes.", "I was wondering if you had an extra heart. Because mine was just stolen.", "Is your name Google? Because you have everything I’ve been searching for.", "You’re so gorgeous you made me forget what my pick up line was", "Im learning of important dates in history, wanna be one?", "i must be in a museum, because you are truly a work of art", "If you cant live without something, it should be free. I can't live without you, so, when are you free?"]

slap_list = []

slapresponse_list = ['oof, that must hurt', 'they must be dead', 'looks like someone got slapped lol']

hug_list = []

hugresponse_list = ['Awwwww, what a cute hug', 'i feel lonely <:apple_plead:812381767432536125>']

kiss_list = []

kissresponse_list = ['I feel lonely <:apple_plead:812381767432536125>', 'I really need a gf <:apple_plead:812381767432536125>']

compliment_list = ['You have the best laugh.', 'Our system of inside jokes is so advanced that only you and I get it. And I like that.', 'Your perspective is refreshing.', 'You deserve a hug right now.', 'You’re more helpful than you realize.', 'You have a great sense of humor.', 'On a scale from 1 to 10, you’re an 11.', 'You’re even more beautiful on the inside than you are on the outside.', 'If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.', 'Your ability to recall random factoids at just the right time is impressive.', 'You may dance like no one’s watching, but everyone’s watching because you’re an amazing dancer!', 'You’re more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)', 'Everyday is just BLAH when I don’t see you fr! ', 'If you were a box of crayons, you’d be the giant name-brand one with the built-in sharpener.', 'Everyone gets knocked down sometimes, but you always get back up and keep going.', 'You’re gorgeous — and that’s the least interesting thing about you, too.', 'If you were a scented candle they’d call it Perfectly Imperfect (and it would smell like summer).']

frog_list = ["https://ih1.redbubble.net/image.1448785672.7225/st,small,507x507-pad,600x600,f8f8f8.jpg", "https://media.istockphoto.com/vectors/cute-frog-cartoon-hand-drawn-style-vector-id1146849256", "https://reneelertzman.com/wp-content/uploads/2016/03/cute-little-green-frog-peeking-out-from-behind-PT9JUFJ.jpg", "https://ih1.redbubble.net/image.1490694325.8717/fposter,small,wall_texture,product,750x1000.jpg", "https://www.crushpixel.com/big-static12/preview4/cute-frog-seamless-pattern-background-1094038.jpg", "https://www.crushpixel.com/big-static12/preview4/cute-frog-seamless-pattern-background-1094038.jpg", "https://media.discordapp.net/attachments/791400172209963058/812447792114827274/IMG_20210217_180127_963.jpg", "http://onebigphoto.com/uploads/2014/09/hello-i-am-cute-frog.jpg", "https://imagesvc.meredithcorp.io/v3/mm/image?q=85&c=sc&poi=face&w=1503&h=1503&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F20%2F2020%2F01%2Ffrog-trio-6.jpg", "https://media.discordapp.net/attachments/791400172209963058/812448117622046720/2lqtt9abx4561.png?width=371&height=500", "https://i.pinimg.com/originals/5c/a6/18/5ca6189bfca950c74ad266c30e587bb9.jpg", "http://1.bp.blogspot.com/-BkUS1SGdmLA/TpEiyhFFC4I/AAAAAAAAB3c/91Rh3vtHNT8/s1600/Cute-Frog-1.jpg", "https://media.discordapp.net/attachments/791400172209963058/812449043791085598/8mi859yc14251.png"]

jdm_list = ['https://images-ext-1.discordapp.net/external/52h-vS9a2mw65Fl7ITo7TuD0wdiGeneuTi0WlqIKays/https/soymotor.com/sites/default/files/imagenes/noticia/toyota-supra.jpg', 'https://images-ext-2.discordapp.net/external/kDofouMxYFqVGrwlHX3ZSy8l1d1L28zyKD6evy-EFMA/https/besthqwallpapers.com/Uploads/16-11-2019/111977/thumb2-nissan-s30-nissan-fairlady-z-tuning-datsun-240z-japanese-cars.jpg', 'https://images-ext-2.discordapp.net/external/OvGDRXylwLmqiccdMXBuPB76YlNE3eEpCJIC33AfgJc/https/www.motorbiscuit.com/wp-content/uploads/2020/10/1986-JDM-Toyota-AE86-Sprinter-Trueno-GT-Apex.jpg', 'https://images-ext-1.discordapp.net/external/mWPXDCBHCJPP-BPzgy10u-hefrtGcwI6QoJg405nTD0/https/i.pinimg.com/originals/88/83/bd/8883bd844c3046df557c7381d0633626.jpg', 'https://images-ext-2.discordapp.net/external/XCCVt9Kwv25RQV68Ad_1F4QnvbsELNGPvxrv9jpI_20/https/i.pinimg.com/originals/67/ff/ea/67ffeab000d8e7033e60360ea0a3bcce.jpg', 'https://images-ext-1.discordapp.net/external/ymHMBTo2uS6Ujq3okVeB2MEN6HLMmaTF3CavIAhJkXA/https/frenomotor.com/files/2015/04/skyline-paul-walker.jpg']

greetings_list = ['Hi', 'Hey', 'Sup', 'Hello']

facts_list =     ["The name Wendy was made up for the book 'Peter Pan.'",
    "Barbie's full name is Barbara Millicent Roberts.",
    "Every time you lick a stamp, you consume 1/10 of a calorie.",
    "The average person falls asleep in seven minutes.",
    "Studies show that if a cat falls off the seventh floor of a building it has about thirty percent less chance of surviving than a cat that falls off the twentieth floor. It supposedly takes about eight floors for the cat to realize what is occurring, relax and correct itself.",
    "Your stomach has to produce a new layer of mucus every 2 weeks otherwise it will digest itself.",
    "The citrus soda 7-UP was created in 1929; '7' was selected after the original 7-ounce containers and 'UP' for the direction of the bubbles.",
    "101 Dalmatians, Peter Pan, Lady and the Tramp, and Mulan are the only Disney cartoons where both parents are present and don't die throughout the movie.",
    "A pig's orgasm lasts for 30 minutes.",
    "'Stewardesses' is the longest word that is typed with only the left hand.",
    "To escape the grip of a crocodile's jaws, push your thumbs into its eyeballs - it will let you go instantly.",
    "Reindeer like to eat bananas.",
    "No word in the English language rhymes with month, orange, silver and purple.",
    "The word 'samba' means 'to rub navels together.'",
    "Mel Blanc (the voice of Bugs Bunny) was allergic to carrots.",
    "The electric chair was invented by a dentist.",
    "The very first bomb dropped by the Allies on Berlin during World War II Killed the only elephant in the Berlin Zoo.",
    "More people are killed annually by donkeys than airplane crashes.",
    "A 'jiffy' is a unit of time for 1/100th of a second.", "A whale's penis is called a dork.",
    "Because of the rotation of the earth, an object can be thrown farther if it is thrown west.",
    "The average person spends 6 months of their life sitting at red lights.",
    "In 1912 a law passed in Nebraska where drivers in the country at night were required to stop every 150 yards, send up a skyrocket, wait eight minutes for the road to clear before proceeding cautiously, all the while blowing their horn and shooting off flares.",
    "More Monopoly money is printed in a year, than real money throughout the world.",
    "Caesar salad has nothing to do with any of the Caesars. It was first concocted in a bar in Tijuana, Mexico, in the 1920's.",
    "One quarter of the bones in your body are in your feet.",
    "Crocodiles and alligators are surprisingly fast on land.  Although they are rapid, they are not agile.  So, if being chased by one, run in a zigzag line to lose him or her.",
    "Seattle’s Fremont Bridge rises up and down more than any drawbridge in the world.",
    "Right-handed people live, on average; nine years longer than left handed people.",
    "Ten percent of the Russian government's income comes from the sale of vodka.",
    "In the United States, a pound of potato chips costs two hundred times more than a pound of potatoes.",
    "A giraffe can go without water longer than a camel.",
    "A person cannot taste food unless it is mixed with saliva. For example, if a strong-tasting substance like salt is placed on a dry tongue, the taste buds will not be able to taste it. As soon as a drop of saliva is added and the salt is dissolved, however, a definite taste sensation results. This is true for all foods.",
    "Nearly 80% of all animals on earth have six legs.",
    "In the marriage ceremony of the ancient Inca Indians of Peru, the couple was considered officially wed when they took off their sandals and handed them to each other.",
    "Ninety percent of all species that have become extinct have been birds.",
    "There is approximately one chicken for every human being in the world.",
    "Most collect calls are made on father's day.",
    "The first automobile race ever seen in the United States was held in Chicago in 1895. The track ran from Chicago to Evanston, Illinois. The winner was J. Frank Duryea, whose average speed was 71/2 miles per hour.",
    "Each of us generates about 3.5 pounds of rubbish a day, most of it paper.",
    "Women manage the money and pay the bills in  75% of all Americans households.",
    "A rainbow can be seen only in the morning or late afternoon. It can occur only when the sun is 40 degrees or less above the horizon.",
    "It has NEVER rained in Calama, a town in the Atacama Desert of Chile.",
    "It costs more to buy a new car today in the United States than it cost Christopher Columbus to equip and undertake three voyages to and from the New World.",
    "The plastic things on the end of shoelaces are called aglets.",
    "An eighteenth-century German named Matthew Birchinger, known as 'the little man of Nuremberg,' played four musical instruments including the bagpipes, was an expert calligrapher, and was the most famous stage magician of his day. He performed tricks with the cup and balls that have never been explained. Yet Birchinger had no hands, legs, or thighs, and was less than 29 inches tall.",
    "Daylight Saving Time is not observed in most of the state of Arizona and parts of Indiana.",
    "Ants closely resemble human manners:  When they wake, they stretch & appear to yawn in a human manner before taking up the tasks of the day.",
    "Bees have 5 eyes. There are 3 small eyes on the top of a bee's head and 2 larger ones in front.",
    "Count the number of cricket chirps in a 15-second period, add 37 to the total, and your result will be very close to the actual outdoor Fahrenheit temperature.",
    "One-fourth of the world's population lives on less than $200 a year.  Ninety million people survive on less than $75 a year.",
    "Butterflies taste with their hind feet.",
    "Only female mosquito’s' bite and most are attracted to the color blue twice as much as to any other color.",
    "If one places a tiny amount of liquor on a scorpion, it will instantly go mad and sting itself to death.",
    "It is illegal to hunt camels in the state of Arizona.",
    "In eighteenth-century English gambling dens, there was an employee whose only job was to swallow the dice if there was a police raid.",
    "There are no clocks in Las Vegas gambling casinos.",
    "The human tongue tastes bitter things with the taste buds toward the back. Salty and pungent flavors are tasted in the middle of the tongue, sweet flavors at the tip!",
    "The first product to have a bar code was Wrigley’s gum.",
    "When you sneeze, air and particles travel through the nostrils at speeds over100 mph.  During this time, all bodily functions stop, including your heart, contributing to the impossibility of keeping one's eyes open during a sneeze.",
    "Annual growth of WWW traffic is 314,000%",
    "%60 of all people using the Internet, use it for pornography.",
    "In 1778, fashionable women of Paris never went out in blustery weather without a lightning rod attached to their hats.",
    "Sex burns 360 calories per hour.",
    "A raisin dropped in a glass of fresh champagne will bounce up and down continually from the bottom of the glass to the top.",
    "Celery has negative calories! It takes more calories to eat a piece of celery than the celery has in it.",
    "The average lead pencil will draw a line 35 miles long or write approximately 50,000 English words.  More than 2 billion pencils are manufactured each year in the United States. If these were laid end to end they would circle the world nine times.",
    "The pop you hear when you crack your knuckles is actually a bubble of gas burning.",
    "A literal translation of a standard traffic sign in China: 'Give large space to the festive dog that makes sport in the roadway.'",
    "You burn more calories sleeping than you do watching TV.",
    "Larry Lewis ran the 100-yard dash in 17.8 seconds in 1969, thereby setting a new world's record for runners in the 100-years-or-older class. He was 101.",
    "In a lifetime the average human produces enough quarts of spit to fill 2 swimming pools.",
    "It's against the law to doze off under a hair dryer in Florida/against the law to slap an old friend on the back in Georgia/against the law to Play hopscotch on a Sunday in Missouri.",
    "Barbie's measurements, if she were life-size, would be 39-29-33.",
    "The human heart creates enough pressure to squirt blood 30ft.",
    "One third of all cancers are sun related.",
    "THE MOST UNUSUAL CANNONBALL: On two occasions, Miss 'Rita Thunderbird' remained inside the cannon despite a lot of gunpowder encouragement to do otherwise. She performed in a gold lamé bikini and on one of the two occasions (1977) Miss Thunderbird remained lodged in the cannon, while her bra was shot across the Thames River.",
    "It has been estimated that humans use only 10% of their brain.",
    "Valentine Tapley from Pike County, Missouri  grew chin whiskers attaining a length of twelve feet six inches from 1860 until his death 1910, protesting Abraham Lincoln's election to the presidency.",
    "Most Egyptians died by the time they were 30 about 300 years ago,",
    "For some time Frederic Chopin, the composer and pianist, wore a beard on only one side of his face, explaining: 'It does not matter, my audience sees only my right side.'",
    "1 in every 4 Americans has appeared someway or another on television.",
    "1 in 8 Americans has worked at a McDonalds restaurant.",
    "70% of all boats sold are used for fishing.",
    "Studies have shown that children laugh an average of 300 times/day and adults 17 times/day, making the average child more optimistic, curious, and creative than the adult.",
    "A pregnant goldfish is called a twit.",
    "The shortest war in history was between Zanzibar and England in 1896. Zanzibar surrendered after 38 minutes.",
    "You were born with 300 bones, but by the time you are an adult you will only have 206.",
    "If you go blind in one eye you only lose about one fifth of your vision but all your sense of depth.",
    "Women blink nearly twice as much as men.",
    "The strongest muscle (Relative to size) in the body is the tongue.",
    "A Boeing 747's wingspan is longer than the Wright brother's first flight.",
    "American Airlines saved $40,000 in 1987 by eliminating one olive from each salad served in first-class.",
    "Average life span of a major league baseball: 7 pitches.",
    "A palindrome is a sentence or group of sentences that reads the same backwards as it does forward: Ex:  'Red rum, sir, is murder.' 'Ma is as selfless as I am.' 'Nurse, I spy gypsies. Run!'  'A man, a plan, a canal - Panama.' 'He lived as a devil, eh?'",
    "The first CD pressed in the US was Bruce Springsteen's 'Born in the USA'",
    "In 1986 Congress & President Ronald Reagan signed Public Law 99-359, which changed Daylight Saving Time from the last Sunday in April to the first Sunday in April.  It was estimated to save the nation about 300,000 barrels of oil each year by adding most of the month April to D.S.T.",
    "The thumbnail grows the slowest, the middle nail the fastest, nearly 4 times faster than toenails.",
    "The Human eyes never grow, but nose and ears never stop growing.",
    "The 57 on Heinz ketchup bottles represents the number of varieties of pickles the company once had.",
    "Tom Sawyer was the first novel written on a typewriter.",
    "If Texas were a country, its GNP would be the fifth largest of any country in the world.",
    "There are 1 million ants for every human in the world.",
    "Odds of being killed by lightening? 1 in 2million/killed in a car crash? 1 in 5,000/killed by falling out of bed? 1 in 2million/killed in a plane crash? 1 in 25 million.",
    "Since 1978, 37 people have died by Vending Machine's falling on them.  13 people are killed annually.  All this while trying to shake merchandise out of them. 113 people have been injured.",
    "Half the foods eaten throughout the world today were developed by farmers in the Andes Mountains (including potatoes, maize, sweet potatoes, squash, all varieties of beans, peanuts, manioc, papayas, strawberries, mulberries and many others).",
    "The 'Golden Arches' of fast food chain McDonalds is more recognized worldwide than the religious cross of Christianity.",
    "Former basketball superstar Michael Jordan is the most recognized face in the world, more than the pope himself.",
    "The average talker sprays about 300 microscopic saliva droplets per minute, about 2.5 droplets per word.",
    "The Earth experiences 50,000 Earth quakes per year and is hit by Lightning 100 times a second.",
    "Every year 11,000 Americans injure themselves while trying out bizarre sexual positions.",
    "If we had the same mortality rate now as in 1900, more than half the people in the world today would not be alive.",
    "On average, Americans eat 18 acres of pizza everyday.",
    "Researchers at the Texas Department of Highways in Fort Worth determined the cow population of the U.S. burps some 50 million tons of valuable hydrocarbons into the atmosphere each year.  The accumulated burps of ten average cows could keep a small house adequately heated and its stove operating for a year.",
    "During a severe windstorm or rainstorm the Empire State Building sways several feet to either side.",
    "In the last 3,500 years, there have been approximately 230 years of peace throughout the civilized world.",
    "The Black Death reduced the population of Europe by one third in the period from 1347 to 1351.",
    "The average person spends about two years on the phone in a lifetime.",
    "Length of beard an average man would grow if he never shaved 27.5 feet",
    "Over 60% of all those who marry get divorced.", "400-quarter pounders can be made from 1 cow.",
    "A full-loaded supertanker traveling at normal speed takes at least 20 minutes to stop.",
    "Coca-Cola was originally green.", "Men can read smaller print than women; women can hear better.",
    "Hong Kong holds the most Rolls Royce’s per capita.",
    "Average number of days a West German goes without washing his underwear: 7",
    "WWII fighter pilots in the South Pacific armed their airplanes while stationed with .50 caliber machine gun ammo belts measuring 27 feet before being loaded into the fuselage. If the pilots fired all their ammo at a target, he went through 'the whole 9 yards', hence the term.",
    "Average number of people airborne over the US any given hour: 61,000.",
    "Intelligent people have more zinc and copper in their hair.",
    "Iceland consumes more Coca-Cola per capita than any other nation.",
    "In the early 1940s, the FCC assigned television's Channel 1 to mobile services (like two-way radios in taxis) but did not re-number the other channel assignments.",
    "The San Francisco Cable cars are the only mobile National Monuments.",
    "Firehouses have circular stairways originating from the old days when the engines were pulled by horses. The horses were stabled on the ground floor and figured out how to walk up straight staircases.",
    "The Main Library at Indiana University sinks over an inch every year because when it was built, engineers failed to take into account the weight of all the books that would occupy the building.",
    "111,111,111 x 111,111,111 = 12,345,678,987,654,321",
    "Statues in parks: If the horse has both front legs in the air, the person died in battle; if the horse has one front leg in the air, the person died as a result of wounds received in battle; if the horse has all four legs on the ground, the person died of natural causes.",
    "The expression 'to get fired' comes from long ago Clans that wanted to get rid of unwanted people, so they would burn their houses instead of killing them, creating the term 'Got fired'.",
    "'I am.' is the shortest complete sentence in the English language.",
    "Hershey's Kisses are called that because the machine that makes them looks like it's kissing the conveyor belt.",
    "The phrase 'rule of thumb' is derived from an old English law, which stated that you couldn't beat your wife with anything wider than your thumb.",
    "The longest recorded flight of a chicken is thirteen seconds.",
    "The Eisenhower interstate system requires that one mile in every five must be straight in case of war or emergency, they could be used as airstrips.",
    "The name Jeep came from the abbreviation used in the army. G.P. for 'General Purpose' vehicle.",
    "The Pentagon, in Arlington, Virginia, has twice as many bathrooms as is necessary, because when it was built in the 1940s, the state of Virginia still had segregation laws requiring separate toilet facilities for blacks and whites.",
    "The cruise liner, Queen Elizabeth II, moves only six inches for each gallon of diesel that it burns.",
    "If you have three quarters, four dimes, and four pennies, you have $1.19, the largest amount of money in coins without being able to make change for a dollar.",
    "In Aspen Colorado, you can have a maximum income of $104,000 and still receive government subsidized housing.",
    "Honking of car horns for a couple that just got married is an old superstition to insure great sex.",
    "Dr. Kellogg introduced Kellogg's Corn Flakes in hopes that it would reduce masturbation.",
    "The sperm of a mouse is actually longer than the sperm of an elephant.",
    "In medieval France, unfaithful wives were made to chase a chicken through town naked.",
    "The Black Widow spider eats her mate during or after sex.",
    "Napoleon's penis was sold to an American Urologist for $40,000.",
    "Eating the heart of a male Partridge was the cure for impotence in ancient Babylon.",
    "A bull can inseminate 300 cows from one single ejaculation.",
    "When a Hawaiian woman wears a flower over her left ear, it means that she is not available.",
    "The 'save' icon on Microsoft Word shows a floppy disk with the shutter on backwards.",
    "The only nation whose name begins with an 'A', but doesn't end in an 'A' is Afghanistan.",
    "The following sentence: 'A rough-coated, dough-faced, thoughtful ploughman strode through the streets of Scarborough; after falling into a slough, he coughed and hiccoughed.' Contains the nine different pronunciations of 'ough' in the English Language.",
    "The verb 'cleave' is the only English word with two synonyms which are antonyms of each other: adhere and separate.",
    "The only 15-letter word that can be spelled without repeating a letter is uncopyrightable.",
    "The shape of plant collenchyma’s cells and the shape of the bubbles in beer foam are the same - they are orthotetrachidecahedrons.",
    "Emus and kangaroos cannot walk backwards, and are on the Australian coat of arms for that reason.",
    "Cats have over one hundred vocal sounds, while dogs only have about ten.",
    "Blueberry Jelly Bellies were created especially for Ronald Reagan.",
    "PEZ candy even comes in a Coffee flavor.",
    "The first song played on Armed Forces Radio during operation Desert Shield was 'Rock the Casba' by the Clash.",
    "Non-dairy creamer is flammable.",
    "The airplane Buddy Holly died in was the 'American Pie.' (Thus the name of the Don McLean song.)",
    "Each king in a deck of playing cards represents a great king from history. Spades - King David, Clubs - Alexander the Great, Hearts - Charlemagne, and Diamonds - Julius Caesar.",
    "Golf courses cover 4% of North America.",
    "The average person will accidentally eat just under a pound of insects every year.",
    "Until 1994, world maps and globes sold in Albania only had Albania on them.",
    "The value of Pi will be officially 'rounded down' to 3.14 from 3.14159265359 on December 31, 1999.",
    "The Great Wall of China is the only man-made structure visible from space.",
    "A piece of paper can be folded no more then 9 times.",
    "The amount of computer Memory required to run WordPerfect for Win95 is 8 times the amount needed aboard the space shuttle.",
    "The average North American will eat 35,000 cookies during their life span.",
    "Between 25% and 33% of the population sneeze when exposed to light.",
    "The most common name in world is Mohammed.",
    "Mount Olympus Mons on Mars is three times the size of Mount Everest.",
    "Most toilets flush in E flat.",
    "2,000 pounds of space dust and other space debris fall on the Earth every day.",
    "Each month, there is at least one report of UFOs from each province of Canada.",
    "40,000 Americans are injured by toilets each year.",
    "You can be fined up to $1,000 for whistling on Sunday in Salt Lake City, Utah.",
    "It takes about 142.18 licks to reach the center of a Tootsie pop.",
    "The serial number of the first MAC ever produced was 2001.",
    "It is illegal to eat oranges while bathing in California.",
    "If done perfectly, a rubix cube combination can be solved in 17 turns.",
    "The average American butt is 14.9 inches long.",
    "More bullets were fired in 'Starship Troopers' than any other movie ever made.",
    "60% of electrocutions occur while talking on the telephone during a thunderstorm.",
    "The name of the girl on the statue of liberty is Mother of Exiles.",
    "3.6 cans of Spam are consumed each second.",
    "There's a systematic lull in conversation every 7 minutes.",
    "The buzz from an electric razor in America plays in the key of B flat; Key of G in England.",
    "There are 1,575 steps from the ground floor to the top of the Empire State building.",
    "The world's record for keeping a Lifesaver in the mouth with the hole intact is 7 hrs 10 min.",
    "There are 293 ways to make change for a dollar.",
    "The world record for spitting a watermelon seed is 65 feet 4 inches.",
    "In the Philippine jungle, the yo-yo was first used as a weapon.",
    "Dueling is legal in Paraguay as long as both parties are registered blood donors.",
    "Texas is also the only state that is allowed to fly its state flag at the same height as the U.S. flag.",
    "The three most recognized Western names in China are Jesus Christ, Richard Nixon, & Elvis Presley.",
    "There is a town in Newfoundland, Canada called Dildo.",
    "The Boston University Bridge (on Commonwealth Avenue, Boston, Massachusetts) is the only place in the world where a boat can sail under a train driving under a car driving under an airplane.",
    "All 50 states are listed across the top of the Lincoln Memorial on the back of the $5 bill.",
    "In space, astronauts are unable to cry, because there is no gravity and the tears won't flow.",
    "Chewing gum while peeling onions will keep you from crying.",
    "There are more plastic flamingos in the U.S that there are real ones.",
    "The crack of a whip is actually a tiny sonic boom, since the tip breaks the sound barrier.",
    "Jupiter is bigger than all the other planets in our solar system combined.",
    "Hot water is heavier than cold.",
    "The common idea that only 10% of the brain is used it not true as it is impossible to determine the actual percentage because of the complexity of the brain.",
    "Lawn darts are illegal in Canada.",
    "There are more psychoanalysts per capita in Buenos Aires than any other place in the world.",
    "Between 2 and 3 jockeys are killed each year in horse racing.",
    "5,840 people with pillow related injuries checked into U.S. emergency rooms in 1992.",
    "The average woman consumes 6 lbs of lipstick in her lifetime.",
    "Some individuals express concern sharing their soap, rightly so, considering 75% of all people wash from top to bottom.",
    "Conception occurs most in the month of December.",
    "CBS' '60 Minutes' is the only TV show without a theme song/music.",
    "Half of all Americans live within 50 miles of their birthplace.",
    "'Obsession' is the most popular boat name.", "On average, Americans' favorite smell is banana.",
    "If one spells out numbers, they would have to count to One Thousand before coming across the letter 'A'.",
    "Honey is the only food which does not spoil.", "3.9% of all women do not wear underwear.",
    "This common everyday occurrence composed of 59% nitrogen, 21% hydrogen, and 9% dioxide is called a 'fart'.",
    "'Evaluation and Parameterization of Stability and Safety Performance Characteristics of Two and Three Wheeled Vehicular Toys for Riding.' Title of a $230,000 research project proposed by the Department of Health, Education and Welfare, to study the various ways children fall off bicycles.",
    "Babies are born without kneecaps. They don't appear until the child reaches 2-6 years of age.",
    "Meteorologists claim they're right 85% of the time (think about that one!)",
    "In 1980, a Las Vegas hospital suspended workers for betting on when patients would die.",
    "Los Angeles' full name 'El Pueblo de Nuestra Senora la Reina de Los Angeles de Porciuncula' is reduced to 3.63% of its size in the abbreviation 'L.A.'.",
    "If you went out into space, you would explode before you suffocated because there's no air pressure.",
    "The only real person to ever to appear on a pez dispenser was Betsy Ross.",
    "Mike Nesmith's (the guitarist of The Monkeys) mom invented White Out.",
    "Only 6 people in the whole world have died from moshing.",
    "241.     In a test performed by Canadian scientists, using various different styles of music, it was determined that chickens lay the most eggs when pop music was played.",
    "The storage capacity of human brain exceeds 4 Terabytes.",
    "In Vermont, the ratio of cows to people is 10:1",
    "Any free-moving liquid in outer space will form itself into a sphere, because of its surface tension.",
    "The average American looks at eight houses before buying one.",
    "In the average lifetime, a person will walk the equivalent of 5 times around the equator.",
    "Koala is Aboriginal for 'no drink'.", "Shakespeare spelled his OWN name several different ways.",
    "The first contraceptive was crocodile dung used by the ancient Egyptians.",
    "A signature is called a John Hancock because he signed the Declaration of Independence. Only 2 people signed the declaration of independence on July 4. The Last person signed 2 years later.",
    "Arnold Schonberg suffered from triskaidecaphobia, the fear of the number 13.  He died at 13 minutes from midnight on Friday the 13th.",
    "Mozart wrote the nursery rhyme 'twinkle, twinkle, little star' at the age of 5.",
    "Weatherman Willard Scott was the first original Ronald McDonald.",
    "Virginia Woolf wrote all her books standing.",
    "Einstein couldn't speak fluently until after his ninth birthday. His parents thought he was mentally retarded.",
    "Al Capone's business card said he was a used furniture dealer.",
    "Deborah Winger did the voice of E.T.",
    "Kelsey Grammar sings and plays the piano for the theme song of Fraiser.",
    "Thomas Edison, acclaimed inventor of the light bulb, was afraid of the dark.",
    "In England, the Speaker of the House is not allowed to speak.",
    "You can sail all the way around the world at latitude 60 degrees south.",
    "The earth weighs around 6,588,000,000,000,000,000,000,000,000 tons.",
    "Peanuts are one of the ingredients of dynamite.", "Porcupines can float in water.",
    "The average person's left hand does 56% of the typing.",
    "A shark is the only fish that can blink with both eyes.",
    "The longest one-syllable word in the English language is 'screeched.'",
    "All of the clocks in the movie 'Pulp Fiction' are stuck on 4:20, a national pot-smokers hour.",
    "'Dreamt' is the only English word that ends in the letters 'mt.'",
    "Almonds are a member of the peach family.",
    "Winston Churchill was born in a ladies' room during a dance.",
    "Maine is the only state whose name is just one syllable.",
    "There are only four words in the English language which end in 'dous': tremendous, horrendous, stupendous, and  hazardous.",
    "Tigers not only have striped fur, they have striped skin!",
    "In most advertisements, including newspapers, the time displayed on a watch is 10:10.",
    "On the ground, a group of geese is a gaggle, in the sky it is a skein.",
    "To Ensure Promptness, one is expected to pay beyond the value of service – hence the later abbreviation: T.I.P.",
    "When the University of Nebraska Cornhuskers play football at home, the stadium becomes the state's third largest city.",
    "The characters Bert and Ernie on Sesame Street were named after Bert the cop and Ernie the taxi driver in Frank Capra's 'Its A Wonderful Life.'",
    "A dragonfly has a lifespan of 24 hours.", "A dime has 118 ridges around the edge.",
    "On an American one-dollar bill, there is an owl in the upper left-hand corner of the '1'encased in the 'shield' and a spider hidden in the front upper right-hand corner.",
    "The name for Oz in the 'Wizard of Oz' was thought up when the creator, Frank Baum, looked at his filing cabinet and saw A-N, and O-Z; hence the name 'OZ.'",
    "The microwave was invented after a researcher walked by a radar tube and a chocolate bar melted in his pocket.",
    "Mr. Rogers is an ordained minister.", "John Lennon's first girlfriend was named Thelma Pickles.",
    "There are 336 dimples on a regulation golf ball.",
    "The scene where Indiana Jones shoots the swordsman in Raider’s of the Lost Ark was Harrison Ford's idea so that he could take a bathroom break.",
    "A crocodile cannot stick its tongue out.", "A snail can sleep for three years.",
    "All polar bears are left-handed.", "China has more English speakers than the United States.",
    "Elephants are the only animals that can't jump.",
    "February 1865 is the only month in recorded history not to have a full moon.",
    "If the population of China walked past you in single file, the line would never end because of the rate of reproduction.",
    "If you yelled for 8 years, 7 months and 6 days, you will have produced enough sound energy to heat one cup of coffee.",
    "In the last 4000 years, no new animals have been domesticated.",
    "Leonardo Da Vinci invented the scissors.",
    "The word 'set' has more definitions than any other word in the English language.",
    "Nutmeg is extremely poisonous if injected intravenously.",
    "On average, people fear spiders more than they do death.",
    "One of the reasons marijuana is illegal today is because cotton growers in the 1930s lobbied against hemp farmers they saw it as competition.",
    "Shakespeare invented the word 'assassination' and 'bump'.", "Some lions mate over 50 times a day.",
    "Starfish haven't got brains.", "The ant always falls over on its right side when intoxicated.",
    "The name of all continents in the world end with the same letter that they start with.",
    "There are two credit cards for every person in the United States.",
    "The longest word comprised of one row on the keyboard is: TYPEWRITER",
    "You can't kill yourself by holding your breath. ",
    "The average person spends 12 weeks a year 'looking for things'.",
    "The symbol on the 'pound' key (#) is called an octothorpe.. ",
    "The dot over the letter 'i' is called a tittle. ", "Ingrown toenails are hereditary. ",
    "'Underground' is the only word in the English language that begins and ends with the letters 'und'",
    "The longest word in the English language, according to the Oxford English Dictionary, is: pneumonoultramicroscopicsilicovolcanoconiosis.. ",
    "The longest place-name still in use is: Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiakitnatahu, a New Zealand hill. ",
    "An ostrich's eye is bigger than its brain. ",
    "Alfred Hitchcock didn't have a belly button. It was eliminated when he was sewn up after surgery.",
    "Telly Savalas and Louis Armstrong died on their birthdays. ",
    "Donald Duck's middle name is Fauntleroy. ",
    "The muzzle of a lion is like a fingerprint - no two lions have the same pattern of whiskers. ",
    "Steely Dan got their name from a sexual device depicted in the book 'The Naked Lunch'. ",
    "The Ramses brand condom is named after the great pharoh Ramses II who fathered over 160 children.",
    "There is a seven letter word in the English language that contains ten words without rearranging any of its letters, 'therein': the, there, he, in, rein, her, here, ere, therein, herein. ",
    "A goldfish has a memory span of three seconds. ",
    "Cranberries are sorted for ripeness by bouncing them; a fully ripened cranberry can be dribbled like a basketball. ",
    "The male gypsy moth can 'smell' the virgin female gypsy moth from 1.8 miles away. ",
    "The letters KGB stand for Komitet Gosudarstvennoy Bezopasnosti. ",
    "The word 'dexter' whose meaning refers to the right hand is typed with only the left hand. ",
    "To 'testify' was based on men in the Roman court swearing to a statement made by swearing on their testicles. ",
    "Facetious and abstemious contain all the vowels in the correct order, as does arsenious, meaning 'containing arsenic.' ",
    "The word 'Checkmate' in chess comes from the Persian phrase 'Shah Mat,' which means 'the king is dead.'",
    "The first episode of 'Joanie Loves Chachi' was the highest rated American program in the history of Korean television, a country where 'Chachi' translates to 'penis'. ",
    "Rubber bands last longer when refrigerated. ",
    "The national anthem of Greece has 158 verses. No one in Greece has memorized all 158 verses. ",
    "Two-thirds of the world's eggplant is grown in New Jersey. ",
    "The giant squid has the largest eyes in the world.", "Giraffes have no vocal cords.",
    "The pupils of a goat's eyes are square.", "Van Gogh only sold one painting when he was alive.",
    "A standard slinky measures 87 feet when stretched out.",
    "The highest per capita Jell-O comsumption in the US is Des Moines.",
    "If a rooster can't fully extend its neck, it can't crow.",
    "There were always 56 curls in Shirley Temple's hair.",
    "The eyes of a donkey are positioned so that it can see all four feet at all times.",
    "Worcestershire sauce in essentially an Anchovy Ketchup.",
    "Rhode Island is the only state which the hammer throw is a legal high school sport.",
    "The average lifespan of an eyelash is five months.", "A spider has transparent blood.",
    "Every acre of American crops harvested contains 100 pounds of insects.",
    "Prince Charles is an avid collecter of toilet seats.",
    "The most common street name in the U.S. is Second Street.",
    "Tehran is the most expensive city on earth.",
    "The sweat drops drawn in cartoon comic strips are called pleuts.",
    "Babies are most likely to be born on Tuesdays.",
    "The HyperMart outside of Garland Texas has 58 check-outs.",
    "The Minneapolis phone book has 21 pages of Andersons.",
    "In the 1980's American migraines increased by 60%.",
    "Poland is the 'stolen car capital of the world'.",
    "Jefferson invented the dumbwaiter, the monetary system, and the folding attic ladder.",
    "The S in Harry S. Truman did not stand for anything.", "In Miconesia, coins are 12 feet across.",
    "A horse can look forward with one eye and back with the other.",
    "Shakespeare is quoted 33,150 times in the Oxford English dictionary.",
    "The word Pennsylvania is misspelled on the Liberty Bell.",
    "NBA superstar Michael Jordan was originally cut from his high school basketball team.",
    "You spend 7 years of your life in the bathroom.",
    "A family of 26 could go to the movies in Mexico city for the price of one in Tokyo.",
    "10,000 Dutch cows pass through the Amsterdam airport each year.",
    "Approximately every seven minutes of every day, someone in an aerobics class pulls their hamstring.",
    "Simplistic passwords contribute to over 80% of all computer password break-ins.",
    "The top 3 health-related searches on the Internet are (in this order): Depression, Allergies, & Cancer.",
    "Dentists have recommended that a toothbrush be kept at least 6 feet away from a toilet to avoid airborne particles resulting from the flush.",
    "Most dust particles in your house are made from dead skin.",
    "Venus is the only planet that rotates clockwise.",
    "Oak trees do not produce acorns until they are fifty years of age or older.",
    "The first owner of the Marlboro company died of lung cancer.",
    "All US Presidents have worn glasses; some just didn't like being seen wearing them in public.",
    "Mosquito repellents don't repel. They hide you. The spray blocks the mosquito's sensors so they don't know you're there.",
    "Walt Disney was afraid of mice.",
    "The site with the highest number of women visitors between the age of 35 and 44 years old: Alka-Seltzer.com",
    "The king of hearts is the only king without a mustache.", "Pearls melt in vinegar.",
    "It takes 3,000 cows to supply the NFL with enough leather for a year's supply of footballs.",
    "Thirty-five percent of people who use personal ads for dating are already married.",
    "The 3 most valuable brand names on earth are Marlboro, Coca-Cola, and Budweiser (in that order).",
    "Humans are the only primates that don't have pigment in the palms of their hands.",
    "Months that begin on a Sunday will always have a 'Friday the 13th'.",
    "The fingerprints of koala bears are virtually indistinguishable from those of humans, so much so that they can be easily confused at a crime scene.",
    "The mask worn by Michael Myers in the original 'Halloween' was actually a Captain Kirk mask painted white.",
    "The only two days of the year in which there are no professional sports games--MLB, NBA, NHL, or NFL--are the day before and the day after the Major League All-Star Game.",
    "Only one person in two billion will live to be 116 or older.",
    "When the French Academy was preparing its first dictionary, it defined 'crab' as, 'A small red fish, which walks backwards.' This definition was sent with a number of others to the naturalist Cuvier for his approval.  The scientist wrote back, 'Your definition, gentlemen, would be perfect, only for three exceptions. The crab is not a fish, it is not red and it does not walk backwards.'",
    "Dr. Jack Kevorkian first patient has Alzheimer's disease.",
    "Fictional/horror writer Stephen King sleeps with a nearby light on to calm his fear of the dark.",
    "It's possible to lead a cow upstairs but not downstairs.",
    "It was discovered on a space mission that a frog can throw up. The frog throws up its stomach first, so the stomach is dangling out of its mouth. Then the frog uses its forearms to dig out all of the stomach's contents and then swallows the stomach back down.",
    "The very first song played on MTV was 'Video Killed The Radio Star' by the Buggles.",
    "William Marston engineered one of the earliest forms of the polygraph in the early 1900's. Later he went on to create the comic strip Wonder Woman, a story about a displaced Amazon princess who forces anyone caught in her magic lasso to tell the truth",
    "Americans travel 1,144,721,000 miles by air every day",
    "The the U.S. you dial '911'. In Stockholm, Sweden you dial 90000",
    "38% of American men say they love their cars more than women",
    "The U.S. military operates 234 golf courses", "100% of lottery winners do gain weight",
    "Bullet proof vests, fire escapes, windshield wipers, and laser printers were all invented by women",
    "A cat has 32 muscles in each ear.", "A duck's quack doesn't echo, and no one knows why.",
    "Cats urine glows under a black light.", "In every episode of Seinfeld there is a Superman somewhere.",
    "Lorne Greene had one of his nipples bitten off by an alligator while he was host of 'Lorne Greene's Wild Kingdom.'",
    "Pamela Anderson Lee is Canada's Centennial Baby, being the first baby born on the centennial anniversary of Canada's independence.",
    "Pinocchio is Italian for 'pine head.'",
    "When possums are playing 'possum', they are not 'playing.' They actually pass out from sheer terror.",
    "Who's that playing the piano on the 'Mad About You' theme? Paul Reiser himself.",
    "Winston Churchill was born in a ladies' room during a dance.", "Most lipstick contains fish scales!",
    "Donald Duck comics were banned from Finland because he doesn't wear pants!",
    "There are more than 10 million bricks in the Empire State Building!",
    "Camels have three eyelids to protect themselves from blowing sand!",
    "The placement of a donkey's eyes in its' heads enables it to see all four feet at all times!",
    "The average American/Canadian will eat about 11.9 pounds of cereal per year!",
    "Over 1000 birds a year die from smashing into windows!",
    "The state of Florida is bigger than England!", "Dolphins sleep with one eye open!",
    "In the White House, there are 13,092 knives, forks and spoons!",
    "Recycling one glass jar, saves enough energy to watch T.V for 3 hours!",
    "Owls are one of the only birds who can see the color blue!",
    "Honeybees have a type of hair on their eyes!", "A jellyfish is 95 percent water!",
    "In Bangladesh, kids as young as 15 can be jailed for cheating on their finals!",
    "The katydid bug hears through holes in its hind legs!",
    "Q is the only letter in the alphabet that does not appear in the name of any of the United States!",
    "166,875,000,000 pieces of mail are delivered each year in the US",
    "Bats always turn left when exiting a cave",
    "The praying mantis is the only insect that can turn its head", "Daffy Duck's middle name is 'Dumas'",
    "In Disney's Fantasia, the Sorcerer's name is 'Yensid' (Disney backwards.)",
    "In The Empire Strikes Back there is a potato hidden in the asteroid field",
    "Walt Disney holds the world record for the most Academy Awards won by one person, he has won twenty statuettes, and twelve other plaques and certificates",
    "James Bond's car had three different license plates in Goldfinger",
    "Canada makes up 6.67 percent of the Earth's land area",
    "South Dakota is the only U.S state which shares no letters with the name of it's capital",
    "The KGB is headquartered at No. 2 Felix Dzerzhinsky Square, Moscow",
    "The Vatican city registered 0 births in 1983", "Spain leads the world in cork production",
    "There are 1,792 steps in the Eiffel Tower",
    "There are 269 steps to the top of the Leaning Tower of Pisa",
    "Leonardo da Vinci could write with one hand while drawing with the other",
    "Rubber bands last longer when refrigerated.", "Peanuts are one of the ingredients of dynamite.",
    "The national anthem of Greece has 158 verses. No one in Greece has memorized all 158 verses.",
    "There are 293 ways to make change for a dollar.",
    "The average secretary’s left hand does 56% of the typing.",
    "A shark is the only fish that can blink with both eyes.",
    "There are more chickens than people in the world (at least before that chicken-flu thing).",
    "Two-thirds of the world’s eggplant is grown in New Jersey.",
    "The longest one-syllable word in the English language is 'screeched.'",
    "All of the clocks in the movie Pulp Fiction are stuck on 4:20.",
    "No word in the English language rhymes with month, orange, silver or purple.",
    "'Dreamt' is the only English word that ends in the letters 'mt'.",
    "All 50 states are listed across the top of the Lincoln Memorial on the back of the $5 bill.",
    "Almonds are members of the peach family.",
    "Winston Churchill was born in a ladies’ room during a dance.",
    "Maine is the only state whose name is just one syllable.",
    "There are only four words in the English language which end in 'dous': tremendous, horrendous, stupendous, and hazardous.",
    "Los Angeles’s full name is 'El Pueblo de Nuestra Senora la Reina de los Angeles de Porciuncula'. And can be abbreviated to 3.63% of its size, 'L.A.'",
    "A cat has 32 muscles in each ear.", "An ostrich’s eye is bigger than it’s brain.",
    "Tigers have striped skin, not just striped fur.",
    "In most advertisements, including newspapers, the time displayed on a watch is 10:10.",
    "Al Capone’s business card said he was a used furniture dealer.",
    "The only real person to be a Pez head was Betsy Ross.",
    "When the University of Nebraska Cornhuskers plays football at home, the stadium becomes the state’s third largest city.",
    "The characters Bert and Ernie on Sesame Street were named after Bert the cop and Ernie the taxi driver in Frank Capra’s 'Its A Wonderful Life'",
    "A dragonfly has a lifespan of 24 hours.", "A goldfish has a memory span of three seconds.",
    "A goldfish has a memory span of three seconds.", "A dime has 118 ridges around the edge.",
    "On an American one-dollar bill, there is an owl in the upper left-hand corner of the '1' encased in the 'shield' and a spider hidden in the front upper right-hand corner.",
    "It’s impossible to sneeze with your eyes open.", "The giant squid has the largest eyes in the world.",
    "Who’s that playing the piano on the 'Mad About You' theme? Paul Reiser himself.",
    "The male gypsy moth can 'smell' the virgin female gypsy moth from 1.8 miles away (pretty good trick).",
    "In England, the Speaker of the House is not allowed to speak.",
    "The name for Oz in the 'Wizard of Oz' was thought up when the creator, Frank Baum, looked at his filing cabinet and saw A-N, and O-Z, hence 'Oz.'",
    "The microwave was invented after a researcher walked by a radar tube and a chocolate bar melted in his pocket.",
    "Mr. Rogers is an ordained minister.", "John Lennon’s first girlfriend was named Thelma Pickles.",
    "The average person falls asleep in seven minutes.",
    "There are 336 dimples on a regulation golf ball.",
    "'Stewardesses' is the longest word that is typed with only the left hand.",
    "The 'pound' key on your keyboard (#) is called an octotroph.",
    "The only domestic animal not mentioned in the Bible is the cat.",
    "The 'dot' over the letter 'i' is called a tittle.",
    "Table tennis balls have been known to travel off the paddle at speeds up to 160 km/hr.",
    "Pepsi originally contained pepsin, thus the name.",
    "The original story from 'Tales of 1001 Arabian Nights' begins, 'Aladdin was a little Chinese boy.'",
    "Nutmeg is extremely poisonous if injected intravenously.",
    "Honey is the only natural food that is made without destroying any kind of life. What about milk you say? A cow has to eat grass to produce milk and grass are living.",
    "Hawaiian alphabet only has 12 letters: A, E, I, O, U, H, K, L, M, N, P, W",
    "Honey is the only food that does not spoil.",
    "And one single teaspoon of honey represents the life work of 12 bees.",
    "Flamingos only can eat with their heads upside down.",
    "Lighter was invented ten years before the match was.",
    "It’s physically impossible for a pig to look up at the sky.",
    "The first internet domain name to ever be registered is Symbolics.com on March 15th, 1985.",
    "Humans are born with 350 bones in their body, but when reaching adulthood, we only 260.",
    "There are 150 verses in Greek national anthem which making it the longest national anthem in the world.",
    "This is impossible to tickle yourself.", "A typical pencil can draw a line that is 35 miles long.",
    "Astronauts get taller in space due to the lack of gravity.",
    "The total surface area of human lungs is 750 square feet. That’s roughly the same area as on-side of a tennis court.",
    "Mosquitos have contributed to more deaths than any animals on earth.",
    "An octopus has 3 hearts, 9 brains & blue blood.",
    "The hair on a polar bear is actually not white but clear. They appear white because it reflects light.",
    "A chameleon can move its eyes in two different directions at the same time.",
    "Buttermilk does not contain any butter and actually low in fat.",
    "A giraffe can go longer without water than a camel can.",
    "Australia has the biggest camel population in the world.", "Snails can sleep up to 3 years.",
    "Methane gases produced by cow products as much pollution as cars do.",
    "The majority of the duct in your house is made up from your own dead skin.",
    "Most lipstick contains fish scales.", "Most ice-cream contains pig skins (Gelatin).",
    "The Philippine island of Luzon contains a lake that contains an island that contains a lake that contains another island.",
    "Hudson Bay Area in Canada had less gravity than rest of the world and scientists do not know why.",
    "Only one to two percent of the entire world population are natural redheads.",
    "Sloppy handwriting has doctors kills more than 7,000 people and injures more than 1.5million people annually due to getting the wrong medication.",
    "Putting sugar on a wound or cut will greatly reduce pain and shorten healing process.",
    "Real diamonds do not show up in X-ray.",
    "Due to extreme pressure and weather conditions, it literally rains diamonds on Neptune and Uranus.",
    "There are 7 different kinds of twins: Identical, Fraternal, Half-Identical, Mirror Image Twins, Mixed Chromosome Twins, Superfecundation and Superfetation.",
    "Before the 17th century, carrots were actually purple. They didn’t get their orange color until mutation occupied.",
    "If the sun is scaled down to the size of a white blood cell, the Milky Way would be equal the size of the United States.",
    "A grammatical pedantry syndrome is a form of OCD in which suffers feel the need to correct every grammatical error that they see.",
    "Scorpions can hold their breath underwater for up to 6 days.",
    "In zero gravity, a candle’s flame is round and blue.",
    "Only 8 percent of the world’s money exists in physical form, the rest is in computers.",
    "Crows are able to recognize human faces and even hold grudges against ones that they don’t like.",
    "Your cellphone carries up to ten times more bacteria than a toilet seat.",
    "Humans and bananas share about 50 percent of the same DNA.",
    "Humans have fewer chromosomes than a potato.",
    "An American Pharmacist named John Pemberton invented Coca-Cola who advertises it as a nerve tonic for curing headaches and fatigue.",
    "Statistically, you are more likely to die on the way to buy a lottery ticket than you are to win the lottery itself.",
    "The word checkmate comes from the Arabic which means 'the king is dead.'",
    "Hot water turns to ice faster than cool water. This is known as the Mpemba effect.",
    "Apollo 7 Mission was the first 'astronaut ice cream' flew in space. However, it was so unpopular among astronauts and was retired from the menu after only one trip into space.",
    "Apollo 8 astronauts were the first to celebrate Christmas in space.",
    "IV Is The Roman Numeral designation for 4 everywhere. However, on the clock face, 4 is displayed as 'IIII'.",
    "The Apple Macintosh had the signatures Of its design team engraved inside its case.",
    "Japan has the most vending machines per capita, a staggering 1:23.",
    "A study by University Chicago in 1915, it concluded that the easiest color to spot at a distance is the color yellow. Which is why the most popular color for taxi cabs are yellow.",
    "Japanese police declare murders that they cannot solve as suicides, in order to save faces and keep crime rate artificially low.",
    "The smallest poisonous frogs only 10 millimeters (0.393701 inch) in length.",
    "Farting helps to reduce blood pressure and is good for your overall health.",
    "In 1994, the US Air Force did research on creating a gay bomb (are informal names for theoretical non-lethal chemical weapon) which is a non-lethal bomb containing very strong human sexual pheromones that would make the enemy forces attracted to each other.",
    "There are around 1,584 people in the United States named 'Seven'.",
    "The classic heart shape that we all know was meant to be two hearts fused together.",
    "The water we drink is older than the sun. The sun is 4.6 billion years old.",
    "The water on our planet is very old. The water we have now is the same water that existed hundreds of millions of year ago. The next time you drink a glass of water, you could be about to sip on dinosaur pee.",
    "Meanwhile, about 40% of Americans think humans and dinosaurs existed at the same time.",
    "Nobody knows who named our planet 'Earth'.",
    "Michael Nicholson from Michigan. He has one bachelor’s degree, two associate’s degrees, 22 master’s degrees, three specialist degrees and one doctoral degree, making him the most credentialed person in history.",
    "Practicing a kill in your head will make you better at it, but only if you’re already good at it.",
    "If two identical twins have children with another pair of identical twins, then their children will genetically be full siblings.",
    "In Biertan village (located in Transylvania, Romania) the church had a 'divorce-reconciliation room.' Couples that wanted to get a divorce had to live in a room for two weeks with one small bed, one chair, one table, one plate and one spoon. In 300 years, they only had one divorce.",
    "Killing a panda in China is a seriously crime. It is punishable by death.",
    "December 4th is the National Cookie Day!",
    "Beards can slow the aging process by stopping water from leaving the skin, keeping it moisturized.",
    "A survey found that 33% of men and 43% of women claimed that they had fallen in love with someone they did not initially find attractive.",
    "Most people dream in color, but those who grow up watching television in black and white are more likely to dream in black and white.",
    "Mixing your drinks with diet soda can get you drunk about 18% faster than regular soda. Hummm…",
    "The number of H2O molecules in 10 drops of water is roughly equal to the total amount of stars in the universe.",
    "Octopuses have copper-based blood instead of iron-based blood, which is why their blood is blue rather than red.",
    "Also, they have three hearts and nine brains",
    "The hormones responsible for your growth are only produced when you sleep.",
    "You touch your face an average of once every three minutes. And you properly touched your face after you read it.",
    "People who sleep less than six hours a night are 4.2 times more likely to catch a cold compared those who get more than seven hours of sleep.",
    "Dogs can make about 100 different facial expressions.",
    "Iceland has no army as is often recognized as the most peaceful country in the world.",
    "Shigeru Miyamoto – maker of Super Mario Bros. and Donkey Kong – is not allowed to bike to work because his safety is too important to Nintendo.",
    "Every year, women lose approximately 1.73 billion bobby pins.",
    "Dolphins give each other 'names' – Specific sounds that they use to call friends and family.",
    "Chimpanzee babies like to play with dolls – They’ll make dolls out of sticks and rocks for themselves.",
    "Squirrels plant thousands of trees every year, simply by forgetting where they put their acorns.",
    "Koalas can sleep for up to 20 hours a day.",
    "The average woman will spend one full year of her life trying to decide what to wear.",
    "The average woman owns eight times more makeup than she actually uses.",
    "Rainbows that appear at night are called 'moonbows.'",
    "100 million years ago, crocodiles had long legs and could gallop after their prey.",
    "The real Top Gun school give a $5 fine to any staff member that quotes the movie."]
#run client
client.run(os.getenv('BOT_TOKEN'))
