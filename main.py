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
import random

#lists
client = discord.Client()
client = commands.Bot(command_prefix = '%')

response_list = ['100% sure!', 'definitely not', 'no :(', 'yes :)', 'hmmmmmm, idk', 'maybe ask again', 'maybe ask someone else', "definitely!", "As I see it, yes!", "Yes!", "No!", "Very likely!", "Not even close!", "Maybe!", "Very unlikely!", "Ask again later!", "Better not tell you now!", " It is certain!", "My sources say no", "Outlook good!", "Very Doubtful!", "Without a doubt!", 'no:heart:']

anime_list = ["https://media1.tenor.com/images/c925511d32350cc04411756d623ebad6/tenor.gif?itemid=13462237", "https://media1.tenor.com/images/89289af19b7dab4e21f28f03ec0faaff/tenor.gif?itemid=12801687", "https://media1.tenor.com/images/e1f44b9d914ba61cc60efd8d3cf439a5/tenor.gif?itemid=9975267", "https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif", "https://media.tenor.com/images/8f711b12e00bc1816694bf51909f8b8f/tenor.gif", "https://media.tenor.com/images/84e609c97fc79323c572baa4e8486473/tenor.gif", "https://media.tenor.com/images/c67648bdadbece24eed182a401abf576/tenor.gif", "https://media.tenor.com/images/46a74ce6228e7bc535263e1464cce46b/tenor.gif", "https://media.tenor.com/images/a173f1c95d81855afd10d51f3fa277ab/tenor.gif", "https://media.tenor.com/images/e1c9ad053d4aa0471727fbf36c3a3868/tenor.gif", "https://media.tenor.com/images/3f6457f7235edf481d542b8074740401/tenor.gif"]

zerotwo_list = ['https://media.tenor.com/images/4632e943653b0ad278a1fa7b8f49d82c/tenor.gif', 'https://media.tenor.com/images/3e7d551f4edbc139f1372a494eccd01d/tenor.gif', 'https://media.tenor.com/images/e046bd4175889014749d008bef023f25/tenor.gif', 'https://media.tenor.com/images/500953247d7ddda4d87908fa0bb2c7bc/tenor.gif', 'https://media.tenor.com/images/2e094b3c1f5bf047698dea434416d080/tenor.gif', 'https://media.tenor.com/images/09df52e29a5506287cd76fb4abafa2cc/tenor.gif', 'https://media.tenor.com/images/4f5f2d78f721fc36e10f4e5e2c340f47/tenor.gif', 'https://media.tenor.com/images/7691590d6ac021b483c39dfa794e2a1c/tenor.gif', 'https://64.media.tumblr.com/d03212d8697607c82bb85db886ee92af/tumblr_p2z0hgMv3g1wd81ruo1_540.gifv']

ichigo_list = ['https://media.tenor.com/images/d1fc46f2d0fd52740711b80b80a3c081/tenor.gif', 'https://media.tenor.com/images/b7687ce05975ad1d5c7ed52717e62f09/tenor.gif', 'https://data.whicdn.com/images/325037756/original.gif']

todoroki_list = ['https://pa1.narvii.com/6894/c584fe56b8dde82ac901aeb8e359cb2e157c3bdfr1-533-300_hq.gif', 'https://media1.tenor.com/images/30638e057d7c84c963619c3f9ab2a3df/tenor.gif?itemid=18024441', 'https://img.wattpad.com/e366789b1d68a2190987c27b2378395b6c0c7d66/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f3152537645325f4f32366f6155673d3d2d3736373439353134382e313562376137353763303434343138363934363130373235393332302e676966?s=fit&w=720&h=720', 'https://i.pinimg.com/originals/2e/31/93/2e31935a326bdff0e6d1b91ae03d607f.gif', 'https://p.favim.com/orig/2018/08/01/boku-no-hero-academia-my-hero-academia-todoroki-shouto-Favim.com-6107451.gif']

headout_list = ['cya', 'peace out', 'stay safe', 'ttyl', 'have fun', 'see you later', 'be happy :)']

roast_list = ['You’re the reason God created the middle finger.', 'You’re a grey sprinkle on a rainbow cupcake.', 'If your brain was dynamite, there wouldn’t be enough to blow your hat off.', 'You are more disappointing than an unsalted pretzel.', 'someday you’ll go far, stay there', 'Light travels faster than sound which is why you seemed bright until you spoke.', 'You have so many gaps in your teeth it looks like your tongue is in jail.', 'I wasn’t born with enough middle fingers to let you know how I feel about you', 'If I wanted to kill myself id climb your ego and jump to your IQ', 'Your face makes onions cry.', 'I would love to insult you, but I’m afraid I won’t do as well as nature did', 'If you’re going to be two-faced, at least make one of them pretty.', 'whenever you swim, you just add another piece of trash to the ocean', 'Zombies eat brains, you’re safe']

pickup_list = ["Even if there was no gravity, i'd still fall for you", "Do you like raisins? How do you feel about a date?", "If I could rearrange the alphabet, I’d put ‘U’ and ‘I’ together.", "If you were a Transformer… you’d be Optimus Fine.", "Are you a parking ticket? Because you’ve got FINE written all over you.", "I'm no photographer, but I can picture us together.", "Are you related to Jean-Claude Van Damme? Because Jean-Claude Van Damme you’re sexy!", "are you from Tenesse? cus you are the only 10 i see", "Baby, if you were words on a page, you’d be fine print.", "You must be a high test score, because I want to take you home and show you to my mother", "I was blinded by your beauty; I’m going to need your name and phone number for insurance purposes.", "I was wondering if you had an extra heart. Because mine was just stolen.", "Is your name Google? Because you have everything I’ve been searching for.", "You’re so gorgeous you made me forget what my pick up line was", "Im learning of important dates in history, wanna be one?", "i must be in a museum, because you are truly a work of art"]

nickwilde_list = ['https://fsa.zobj.net/crop.php?r=o-a4ILNuzRn8YwRkD-QM0H7an2GTrabiOjyMpROxtpiArleiFVaF6Fpmob4McDSJ93q3TqqQ00x3OoXqbLBl8bvMDwrnfI1wp7C_KNhsJGGAN-oQ3ZfRsouuic-dUowmbZU5cwncc1AETh4L', 'https://static.wikia.nocookie.net/zootropolis/images/6/6e/Nick_Wilde.png/revision/latest/scale-to-width-down/340?cb=20160326155400','https://pm1.narvii.com/6359/f79784f115daa6a84fda688b535c8330e0afd678_00.jpg', 'https://www.seekpng.com/png/detail/158-1582917_report-abuse-nick-wilde.png', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ80pNZPfmU6xPQIQnrRDfOYKLD-Xd0LykY4g&usqp=CAU']

slap_list = ['https://image.myanimelist.net/ui/BQM6jEZ-UJLgGUuvrNkYUFk2Ae92E1tAeAfjk_pGLpKnHfWiikue5-m1fMe8_1TjRXlLKNwbrQTs1EfUN5ol3A', 'https://i.pinimg.com/originals/cd/13/ad/cd13adaeb8b4208db2270d7c94963101.gif', 'https://i.pinimg.com/originals/fe/39/cf/fe39cfc3be04e3cbd7ffdcabb2e1837b.gif', 'https://i.imgur.com/fm49srQ.gif', 'https://steamuserimages-a.akamaihd.net/ugc/850473950842117246/8C83635F86CE09C683D511622D7ED2B85BAD3ADD/', 'https://static.fjcdn.com/gifs/Mm_966fc2_1916375.gif', 'https://hosting.photobucket.com/images/b292/Animeniac206/e078aebe-6803-436b-9ffd-9c9f223c849b-original.gif?width=450&height=278&fit=bounds&crop=fill', 'https://i.gifer.com/7zBH.gif', 'https://i.pinimg.com/originals/b6/e3/9e/b6e39e693be3968d212b0fe5754f85db.gif', 'https://i.gifer.com/CXfX.gif', 'https://i.pinimg.com/originals/b0/a7/8b/b0a78b527317430cee98d326c85d1572.gif', 'https://static.fjcdn.com/gifs/Epic++slap_325276_4981364.gif', 'https://media1.tenor.com/images/419415702d1d29724279e5e8bfc68742/tenor.gif?itemid=18043240']

slapresponse_list = ['oof, that must hurt', 'they must be dead', 'looks like someone got slapped hehe']

hug_list = ['https://media0.giphy.com/media/PHZ7v9tfQu0o0/200w.gif?cid=ecf05e47lagiw826g9lr1a60d6a1frd11f6bh5cnt3samaxd&rid=200w.gif', '']

compliment_list = ['You have the best laugh.', 'Our system of inside jokes is so advanced that only you and I get it. And I like that.', 'Your perspective is refreshing.', 'You deserve a hug right now.', 'You’re more helpful than you realize.', 'You have a great sense of humor.', 'On a scale from 1 to 10, you’re an 11.', 'You’re even more beautiful on the inside than you are on the outside.', 'If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now.', 'Your ability to recall random factoids at just the right time is impressive.', 'You may dance like no one’s watching, but everyone’s watching because you’re an amazing dancer!', 'You’re more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)', 'Everyday is just BLAH when I don’t see you fr! ', 'If you were a box of crayons, you’d be the giant name-brand one with the built-in sharpener.', 'Everyone gets knocked down sometimes, but you always get back up and keep going.', 'You’re gorgeous — and that’s the least interesting thing about you, too.', 'If you were a scented candle they’d call it Perfectly Imperfect (and it would smell like summer).']

kiss_list = ['https://image.myanimelist.net/ui/7TVWLJ4cRvwHjFyWCI7sZ5Zm3qFTI-ckzFGm08U0toC8AOuDQONqmz3hltQtOr1CDb1-nuL9gmMlBJ7hZ5GtaqGKS9iHtgy3XBAVTSl2ytf2eHAsrbSK1opFqEiwMOmz', '']

#client
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    #status
    await client.change_presence(status=discord.Status.online, activity=discord.Game('with your heart'))




@client.event

async def on_message(message):
    if message.author == client.user:
        return
#commands

#await client.send_message(message.channel, "I'm in " + str(len(client.servers)) + " servers!")


    if client.user.mention in message.content.split():
        await message.reply('You mentioned me!', mention_author=True)


#hello
    if message.content.startswith('%hello'):
        embed=discord.Embed(title="Hello!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#hepl
    if message.content.startswith('%hepl'):
        embed=discord.Embed(title="BRUH, U cant even spell...", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#add bot
    if message.content.startswith('%addbot'):
        embed=discord.Embed(title="Add me to your server by clicking this link", color=0xff9efc)
        embed.add_field(name="https://bit.ly/null-bot-add", value="‎‎‎‎‎‎‎ ", inline=False)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#join server
    if message.content.startswith('%joinserver'):
        embed=discord.Embed(title="Join my server by clicking this link", color=0xff9efc)
        embed.add_field(name="https://bit.ly/null-bot-join", value="‎‎‎‎‎‎‎ ", inline=False)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#botver
    if message.content.startswith('%botver'):
        embed=discord.Embed(title="I am currently on Development version 0.50!", color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#8ball
    if message.content.startswith("%8ball"):
        lucky_num = random.randint(0,len(response_list) - 1)
        embed=discord.Embed(title=(response_list[lucky_num]), color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#compliment
    if message.content.startswith("%compliment"):
        lucky_num = random.randint(0,len(compliment_list) - 1)
        embed=discord.Embed(title=(compliment_list[lucky_num]), color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#pickupline
    if message.content.startswith("%pickupline"):
        lucky_num = random.randint(0,len(pickup_list) - 1)
        embed=discord.Embed(title=(pickup_list[lucky_num]), color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#roast
    if message.content.startswith("%roast"):
        lucky_num = random.randint(0,len(roast_list) - 1)
        embed=discord.Embed(title=(roast_list[lucky_num]), color=0xff9efc)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#cuteanime
    if message.content.startswith("%cuteanime"):
        lucky_num = random.randint(0,len(anime_list) - 1)
        embed=discord.Embed(title='Awww', color=0xff9efc)
        embed.set_image(url=(anime_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#zero two
    if message.content.startswith("%zerotwo"):
        lucky_num = random.randint(0,len(zerotwo_list) - 1)
        embed=discord.Embed(title='Awww', color=0xff9efc)
        embed.set_image(url=(zerotwo_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#todoroki
    if message.content.startswith("%todoroki"):
        lucky_num = random.randint(0,len(todoroki_list) - 1)
        embed=discord.Embed(title='Awww', color=0xff9efc)
        embed.set_image(url=(todoroki_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#ichigo
    if message.content.startswith("%ichigo"):
        lucky_num = random.randint(0,len(ichigo_list) - 1)
        embed=discord.Embed(title='Awww', color=0xff9efc)
        embed.set_image(url=(ichigo_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#slap
    if message.content.startswith("%slap "):
        lucky_num = random.randint(0,len(slap_list) - 1)
        lucky_num = random.randint(0,len(slapresponse_list) - 1)
        embed=discord.Embed(title=(slapresponse_list[lucky_num]), color=0xff9efc)
        embed.set_image(url=(slap_list[lucky_num]))
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)
        

#head out
    if message.content.startswith("%headout"):
        lucky_num = random.randint(0,len(headout_list) - 1)
        embed=discord.Embed(title=(headout_list[lucky_num]), color=0xff9efc)
        embed.set_image(url='https://media1.tenor.com/images/c57c8725cfdb74251c392e0ca46753ba/tenor.gif?itemid=15194343')
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-AMqGqMLEBnFQkD3l-w1370.gif')
        await message.reply(embed=embed, mention_author=True)


#help
    if message.content.startswith('%help'):
        embed=discord.Embed(title="NULL.™ Help", color=0xff9efc)
        #hello
        embed.add_field(name="%hello", value="You're greeted by me!", inline=False)
        #bot version
        embed.add_field(name="%botver", value="Get to know my current software version!", inline=False)
        #8ball
        embed.add_field(name="%8ball(your question)", value="Magic 8ball :O", inline=False)
        #pick
        #embed.add_field(name="%pick", value="I pick from a list (separated by commas and spaces)", inline=False)
        #ping
        #embed.add_field(name="%ping", value="Lists current ping in miliseconds!", inline=False)
        #repeat
        #embed.add_field(name="%repeat", value="I repeat after you!", inline=False)
        #cute anime
        embed.add_field(name="%cuteanime", value="Cute anime gifs", inline=False)
        #head out
        embed.add_field(name="%headout", value="Cya, Have fun", inline=False)
        #roast
        embed.add_field(name="%roast", value="Let me roast you...", inline=False)
        #pickup line
        embed.add_field(name="%pickupline", value="Let me give you a pickup line :smirk:", inline=False)
        #compliment
        embed.add_field(name="%compliment", value="Sweet compliments :)", inline=False)
        #website
        embed.add_field(name="Check out the official website here!", value="http://bit.ly/null-discord", inline=False)
        #server
        embed.add_field(name="Join the official server here!", value="http://bit.ly/null-bot-join", inline=False)
        #add bot
        embed.add_field(name="Add me to your server here!", value="http://bit.ly/null-bot-add", inline=False)
        #easter eggs
        embed.add_field(name="easter eggs :smirk:", value="Read the code on Muphs' Github to find out :smirk:", inline=False)
        #github
        embed.add_field(name="Check out the source code here!", value="http://bit.ly/null-bot-source-code", inline=False)
        embed.set_footer(text="NULL.™")
        embed.set_thumbnail(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/ezgif-com-gif-maker-mePBN4Q8D4Cb9WZE-w1370.gif')
        await message.reply(embed=embed, mention_author=True)



#credentials
load_dotenv('.env')

#run client
client.run(os.getenv('BOT_TOKEN'))
