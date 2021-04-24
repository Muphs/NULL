#imports
import discord
from discord import user
from discord import embeds
from discord import message
from discord import reaction
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
from async_timeout import timeout
from functools import partial
import youtube_dl
from googleapiclient.discovery import build
import re
import parser
from youtubesearchpython import VideosSearch
from youtube_search import YoutubeSearch

#variables
load_dotenv('.env')
description = (os.getenv('DESCRIPTION'))
thumbnail = (os.getenv('THUMBNAIL'))
thumbnail_small = (os.getenv('THUMBNAIL_SMALL'))
prefix = (os.getenv('PREFIX'))
fapikey = (os.getenv('FAPI_KEY'))
ipapi_key = (os.getenv('IPAPI_KEY'))
color = 0xff9efc
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=(prefix), help_command=None, intents=intents, case_insensitive=True)
bot.remove_command('help')
client = discord.Client()
response_list = ['100% sure!', 'definitely not', 'no :(', 'yes :)', 'hmmmmmm, idk', 'maybe ask again', 'maybe ask someone else', "definitely!", "As I see it, yes!", "Yes!", "No!", "Very likely!", "Not even close!", "Maybe!", "Very unlikely!", "Ask again later!", "Better not tell you now!", " It is certain!", "My sources say no", "Outlook good!", "Very Doubtful!", "Without a doubt!", 'no:heart:']
anime_list = ["https://cdn.discordapp.com/emojis/814696607974031400.gif", "https://media1.tenor.com/images/c925511d32350cc04411756d623ebad6/tenor.gif?itemid=13462237", "https://media1.tenor.com/images/89289af19b7dab4e21f28f03ec0faaff/tenor.gif?itemid=12801687", "https://media1.tenor.com/images/e1f44b9d914ba61cc60efd8d3cf439a5/tenor.gif?itemid=9975267", "https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif", "https://media.tenor.com/images/8f711b12e00bc1816694bf51909f8b8f/tenor.gif", "https://media.tenor.com/images/84e609c97fc79323c572baa4e8486473/tenor.gif", "https://media.tenor.com/images/c67648bdadbece24eed182a401abf576/tenor.gif", "https://media.tenor.com/images/46a74ce6228e7bc535263e1464cce46b/tenor.gif", "https://media.tenor.com/images/a173f1c95d81855afd10d51f3fa277ab/tenor.gif", "https://media.tenor.com/images/e1c9ad053d4aa0471727fbf36c3a3868/tenor.gif", "https://media.tenor.com/images/3f6457f7235edf481d542b8074740401/tenor.gif"]
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
sigh_list = ['https://media1.tenor.com/images/34b67ecddde773b30dbe962d14ff27c7/tenor.gif?itemid=20668021', ]
clap_list = ['https://media1.tenor.com/images/7460a26a07ef24d696eaac0b0ff4d5bf/tenor.gif?itemid=16461487', 'https://media.tenor.com/images/ba246f4d3f2845cac07466ab3d013279/tenor.gif', 'https://media.tenor.com/images/657f0c243282921245c0b9f4b1525c1b/tenor.gif', 'https://media.tenor.com/images/2cf9843ed2489b97be6ca65acd40b55f/tenor.gif', 'https://media.tenor.com/images/07908bbd4b8336d826c733de9b2f2988/tenor.gif', 'https://media.tenor.com/images/18ae86fcb295c6d30028dedf7a946970/tenor.gif', 'https://media.tenor.com/images/9f94b89d628518c67808ebadba924306/tenor.gif', 'https://media.tenor.com/images/bd235c84724d5eb04b5cfe39028e936c/tenor.gif']
coin_list = ['Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!', 'Heads!', 'Tails!']
dababy_list = ['https://media.tenor.com/images/57440c61f7c098edcf19e89064fcbbf7/tenor.gif', 'https://media1.tenor.com/images/c8edfdc06ef1c0cd01f03eaa20d8f8b7/tenor.gif?itemid=20883016', 'https://media1.tenor.com/images/fb4990d28060529e74d53b24fa9fa012/tenor.gif?itemid=15748120', 'https://media1.tenor.com/images/44e37453e27d700edbae6f112b9acd41/tenor.gif?itemid=20757217', 'https://cdn.discordapp.com/emojis/818521259125112893.gif?v=1', 'https://media.tenor.com/images/57440c61f7c098edcf19e89064fcbbf7/tenor.gif', 'https://media1.tenor.com/images/c8edfdc06ef1c0cd01f03eaa20d8f8b7/tenor.gif?itemid=20883016', 'https://media1.tenor.com/images/fb4990d28060529e74d53b24fa9fa012/tenor.gif?itemid=15748120', 'https://media1.tenor.com/images/44e37453e27d700edbae6f112b9acd41/tenor.gif?itemid=20757217', 'https://cdn.discordapp.com/emojis/818521259125112893.gif?v=1', 'https://media.tenor.com/images/57440c61f7c098edcf19e89064fcbbf7/tenor.gif', 'https://media1.tenor.com/images/c8edfdc06ef1c0cd01f03eaa20d8f8b7/tenor.gif?itemid=20883016', 'https://media1.tenor.com/images/fb4990d28060529e74d53b24fa9fa012/tenor.gif?itemid=15748120', 'https://media1.tenor.com/images/44e37453e27d700edbae6f112b9acd41/tenor.gif?itemid=20757217', 'https://cdn.discordapp.com/emojis/818521259125112893.gif?v=1']
greetings_list = ['Hi', 'Hey!', 'Sup', 'Hello!', 'Hemlo :)', 'Hai', 'Hey, how are you? :)', "Hi, how are you doing?"]
rock_list = ['https://static.onecms.io/wp-content/uploads/sites/6/2016/11/dwayne-johnson.jpg', 'https://media.discordapp.net/attachments/791400172209963058/833880348143779840/Z.png', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNniGFdkhKMp8dqSGYjDtnHnoF7IwH2nDSOiGuvk3JHj-Wt_VehhGHqIoZ6OiMNBmuR1I&usqp=CAU', 'https://media.discordapp.net/attachments/791400172209963058/833880832317718538/xqkvbXm.png', 'https://i.redd.it/d1qb1dqby73z.jpg', 'https://pics.me.me/dwayne-the-block-johnson-it-ain%E2%80%99t-butter-but-it%E2%80%99s-hard-62078044.png', 'https://media.discordapp.net/attachments/791400172209963058/833881114120159282/image0.jpg', 'https://pics.me.me/dwayne-the-log-johnson-me-irl-22713272.png', 'https://media.discordapp.net/attachments/791400172209963058/833881332651524157/image0.jpg', 'https://i.redd.it/pyd4r36xhcd41.jpg', 'https://i.imgur.com/o3hJf5H.jpg', 'https://i.pinimg.com/originals/4e/04/62/4e04622da507fcf31886b1dbc4da339a.png', 'https://pics.me.me/dwane-the-bop-johnson-spiy-fltk-it-twist-very-funny-51837846.png', 'https://pics.onsizzle.com/144p-1080p-4k-evolution-of-the-rock-23053816.png', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTe2M5nD9tqjFtdRdi91LgW3wi9T8X-m-UJmg&usqp=CAU', 'https://i.pinimg.com/originals/6c/82/5d/6c825d1140b2e2e4f7129ac0a015e3b0.png']

#Print loged in as (bot name) and set stream status
@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Streaming(name='Back Online!', url=(os.getenv('STREAM_URL'))))
    time.sleep(5)
    await bot.change_presence(activity=discord.Streaming(name=(os.getenv('STREAM')), url=(os.getenv('STREAM_URL'))))

#Hello command
@bot.command()
async def hello(ctx):
    lucky_num = random.randint(0,len(greetings_list) - 1)
    embed=discord.Embed(title=((greetings_list[lucky_num])), color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#say command
@bot.command()
async def say(ctx, *, arg):
    embed=discord.Embed(title=(arg), color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#ping command
@bot.command()
async def ping(ctx):
    embed=discord.Embed(title="Pong! :ping_pong:", color=(color), description=(f'Ponged back in `{round(bot.latency * 1000)}ms`'))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#add bot link
@bot.command()
async def addbot(ctx):
    embed=discord.Embed(title="Add me to your server by clicking this link!", color=(color))
    embed.add_field(name="https://bit.ly/null-bot-add", value="‎‎‎‎‎‎‎ ", inline=False)
    embed.add_field(name="Notice:", value="NULL. Is still in the development, which may cause commands to not work and the bot to be offline from now and then with no schedule.", inline=False)
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#join server link
@bot.command()
async def joinserver(ctx):
    embed=discord.Embed(title="Join my server by clicking this link", color=(color))
    embed.add_field(name="https://bit.ly/null-bot-join", value="‎‎‎‎‎‎‎ ", inline=False)
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#bot version
@bot.command()
async def botver(ctx):
    embed=discord.Embed(title="I am currently on Development version 2.5 Rewrite Open Beta!", color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#8ball
@bot.command()
async def m8b(ctx):
    lucky_num = random.randint(0,len(response_list)-1)
    embed=discord.Embed(title=(response_list[lucky_num]), color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#compliment command
@bot.command()
async def compliment(ctx):
    lucky_num = random.randint(0,len(compliment_list)-1)
    embed=discord.Embed(title=(compliment_list[lucky_num]), color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#pickup line
@bot.command()
async def pickupline(ctx):
    lucky_num = random.randint(0,len(pickup_list)-1)
    embed=discord.Embed(title=(pickup_list[lucky_num]), color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#roast
@bot.command()
async def roast(ctx):
    lucky_num = random.randint(0,len(roast_list)-1)
    embed=discord.Embed(title=(roast_list[lucky_num]), color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#mario judah
@bot.command()
async def milk(ctx):
    embed=discord.Embed(title='YEEEEEEEEEEEEEEEEEEEEET', color=(color))
    embed.set_image(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/mario-judah-throws-milk-_-m2WjP9Gx6yHOB0J1-w1370.gif')
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#mario judah
@bot.command()
async def milkyeet(ctx):
    embed=discord.Embed(title='YEEEEEEEEEEEEEEEEEEEEET', color=(color))
    embed.set_image(url='https://assets.zyrosite.com/YbNGxlQMyaf5ag5P/mario-judah-throws-milk-_-m2WjP9Gx6yHOB0J1-w1370.gif')
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#cute anime
@bot.command()
async def cuteanime(ctx):
    lucky_num = random.randint(0,len(anime_list)-1)
    embed=discord.Embed(title='Awww', color=(color))
    embed.set_image(url=(anime_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#zero two
@bot.command()
async def zerotwo(ctx):
    lucky_num = random.randint(0,len(zerotwo_list)-1)
    embed=discord.Embed(title='Boku no darling!', color=(color))
    embed.set_image(url=(zerotwo_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#todoroki
@bot.command()
async def todoroki(ctx):
    lucky_num = random.randint(0,len(todoroki_list)-1)
    embed=discord.Embed(title='Awww', color=(color))
    embed.set_image(url=(todoroki_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#ichigo
@bot.command()
async def ichigo(ctx):
    lucky_num = random.randint(0,len(ichigo_list)-1)
    embed=discord.Embed(title='Awww', color=(color))
    embed.set_image(url=(ichigo_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#bunny girl
@bot.command()
async def bunnygirl(ctx):
    lucky_num = random.randint(0,len(bunnygirl_list)-1)
    embed=discord.Embed(title='Awww', color=(color))
    embed.set_image(url=(bunnygirl_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#slap
@bot.command()
async def slap(ctx):
    lucky_num = random.randint(0,len(slap_list)-1)
    lucky_num = random.randint(0,len(slapresponse_list)-1)
    embed=discord.Embed(title=(slapresponse_list[lucky_num]), color=(color))
    embed.set_image(url=(slap_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#hug
@bot.command()
async def hug(ctx):
    lucky_num = random.randint(0,len(hug_list)-1)
    lucky_num = random.randint(0,len(hugresponse_list)-1)
    embed=discord.Embed(title=(hugresponse_list[lucky_num]), color=(color))
    embed.set_image(url=(hug_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#kiss
@bot.command()
async def kiss(ctx):
    lucky_num = random.randint(0,len(kiss_list)-1)
    lucky_num = random.randint(0,len(kissresponse_list)-1)
    embed=discord.Embed(title=(kissresponse_list[lucky_num]), color=(color))
    embed.set_image(url=(kiss_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#sigh
@bot.command()
async def sigh(ctx):
    lucky_num = random.randint(0,len(sigh_list)-1)
    embed=discord.Embed(title='`*sighs*`', color=(color))
    embed.set_image(url=(sigh_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#clap
@bot.command()
async def clap(ctx):
    lucky_num = random.randint(0,len(clap_list)-1)
    embed=discord.Embed(title='`*clap*` `*clap*` `*clap*`', color=(color))
    embed.set_image(url=(clap_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True) 

#head out
@bot.command()
async def headout(ctx):
    lucky_num = random.randint(0,len(headout_list)-1)
    embed=discord.Embed(title=(headout_list[lucky_num]), color=(color))
    embed.set_image(url='https://media1.tenor.com/images/c57c8725cfdb74251c392e0ca46753ba/tenor.gif?itemid=15194343')
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def dababy(ctx):
    lucky_num = random.randint(0,len(dababy_list)-1)
    embed=discord.Embed(title='LESSSS GOOOOO :smiling_imp: :cold_face: :hot_face: :exclamation::exclamation: ', color=(color))
    embed.set_image(url=(dababy_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#hamster
@bot.command()
async def hamster(ctx):
    lucky_num = random.randint(0,len(hamster_list)-1)
    embed=discord.Embed(title='Awww', color=(color))
    embed.set_image(url=(hamster_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#how sus
@bot.command()
async def howsus(ctx):
    sus = random.randint(0, 100)
    embed=discord.Embed(title=(str(sus)) + "% sus!", color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#how gay
@bot.command()
async def howgay(ctx):
    gay = random.randint(0, 100)
    embed=discord.Embed(title=(str(gay)) + "% gay :gay_pride_flag:", color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#iq
@bot.command()
async def iq(ctx):
    iq = random.randint(0, 1000)
    embed=discord.Embed(title=(str(iq)) + " IQ", color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#inspire
@bot.command()
async def inspire(ctx):
    def get_quote():
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return(quote)
    quote = get_quote()
    embed=discord.Embed(title=(quote), color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#frog
@bot.command()
async def frog(ctx):
    lucky_num = random.randint(0,len(frog_list)-1)
    embed=discord.Embed(title='Awww', color=(color))
    embed.set_image(url=(frog_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#jdm
@bot.command()
async def jdm(ctx):
    lucky_num = random.randint(0,len(jdm_list)-1)
    embed=discord.Embed(title=':smirk:', color=(color))
    embed.set_image(url=(jdm_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#random fact
@bot.command()
async def fact(ctx):
    factapi = requests.get('https://useless-facts.sameerkumar.website/api')
    json_data = json.loads(factapi.text)
    fact = json_data['data']
    embed=discord.Embed(title=(fact), color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#random commands
@bot.command()
async def rand(ctx, arg1, arg2, arg3):
    if arg1 == '-num' or arg1 == '-number' or arg1 == '-n':
        rng = random.randint((int(arg2)), (int(arg3)))
        embed=discord.Embed(title='Your random number is **' + (str(rng)) + '**', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)
    elif arg1 == '-img' or arg1 == '-image':
        picgen = random.randint(0, 999999999999999999999999999999999999999999999999999999)
        embed=discord.Embed(title=' ', color=(color))
        embed.set_image(url='https://picsum.photos/seed/' + (str(picgen)) + '/3840/2160')
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail_small))
        message = await ctx.reply(embed=embed, mention_author=True)

#covid
@bot.command()
async def covid(ctx):
    covid = requests.get('https://api.covid19api.com/world/total')
    json_data = json.loads(covid.text)
    CovidConfirmed = json_data['TotalConfirmed']
    CovidDeaths = json_data['TotalDeaths']
    CovidRecovered = json_data['TotalRecovered']
    embed=discord.Embed(title='COVID19 Info.', color=(color))
    embed.set_thumbnail(url=(thumbnail_small))
    embed.add_field(name=("{:,}".format(CovidConfirmed)), value="Confirmed cases.", inline=True)
    embed.add_field(name=("{:,}".format(CovidRecovered)), value="Recovered cases.", inline=True)
    embed.add_field(name=("{:,}".format(CovidDeaths)), value="Deaths.", inline=True)
    embed.set_footer(text=(description))
    message = await ctx.reply(embed=embed, mention_author=True)

#covid
@bot.command()
async def covid19(ctx):
    covid = requests.get('https://api.covid19api.com/world/total')
    json_data = json.loads(covid.text)
    CovidConfirmed = json_data['TotalConfirmed']
    CovidDeaths = json_data['TotalDeaths']
    CovidRecovered = json_data['TotalRecovered']
    embed=discord.Embed(title='COVID19 Info.', color=(color))
    embed.set_thumbnail(url=(thumbnail_small))
    embed.add_field(name=("{:,}".format(CovidConfirmed)), value="Confirmed cases.", inline=True)
    embed.add_field(name=("{:,}".format(CovidRecovered)), value="Recovered cases.", inline=True)
    embed.add_field(name=("{:,}".format(CovidDeaths)), value="Deaths.", inline=True)
    embed.set_footer(text=(description))
    message = await ctx.reply(embed=embed, mention_author=True)

#meme
@bot.command()
async def meme(ctx):
    meme = requests.get('https://meme-api.herokuapp.com/gimme')
    json_data = json.loads(meme.text)
    memeurl = json_data['url']
    memetitle = json_data['title']
    memensfw = json_data['nsfw']
    embed=discord.Embed(title=(memetitle), color=(color))
    embed.set_image(url=(memeurl))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)
    if memensfw == 'true':
        return    

#telcel
@bot.command()
async def telcel(ctx):
    embed=discord.Embed(title="Telcel :smiling_imp:", color=(color), description=':cloud_tornado:MARAVILLA:smiling_imp: DE ESA BOCA:flushed:ILUMINA :stuck_out_tongue:TODO:money_mouth: COMO :triumph:EL:hot_face:SOL:clown:UNA :sleepy:COSA:metal:LLEGA:heart_eyes:A OTRA:scream:Y:pleading_face:LA:no_mouth: VIDA :flag_mx:PINTA:thinking:MUCHO:neutral_face:MEJOR:nauseated_face:')
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#diceroll
@bot.command()
async def diceroll(ctx):
    dice = random.randint(1, 6)
    if (str(dice)) == '1':
        embed=discord.Embed(title='You rolled a ' + (str(dice)) + '!', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330739248005160.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif (str(dice)) == '2':
        embed=discord.Embed(title='You rolled a ' + (str(dice)) + '!', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330526671765504.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif (str(dice)) == '3':
        embed=discord.Embed(title='You rolled a ' + (str(dice)) + '!', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330652173729793.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif (str(dice)) == '4':
        embed=discord.Embed(title='You rolled a ' + (str(dice)) + '!', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330571408474112.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif (str(dice)) == '5':
        embed=discord.Embed(title='You rolled a ' + (str(dice)) + '!', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330607776759828.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)
    elif (str(dice)) == '6':
        embed=discord.Embed(title='You rolled a ' + (str(dice)) + '!', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/824330708973518918.png?size=64')
        message = await ctx.reply(embed=embed, mention_author=True)

#coin
@bot.command()
async def coinflip(ctx):
    lucky_num = random.randint(0,len(coin_list)-1)
    if (coin_list[lucky_num]) == 'Heads!':
        embed=discord.Embed(title=(coin_list[lucky_num]), color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/785926282696196106/824366377975414844/rsz_obverse.jpg')
        message = await ctx.reply(embed=embed, mention_author=True)
    if (coin_list[lucky_num]) == 'Tails!':
        embed=discord.Embed(title=(coin_list[lucky_num]), color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/785926282696196106/824366580204175370/rsz_reverse.jpg')
        message = await ctx.reply(embed=embed, mention_author=True)

#joke
@bot.command()
async def joke(ctx):
    dad_joke = requests.get('https://official-joke-api.appspot.com/random_joke')
    json_data = json.loads(dad_joke.text)
    dadjoke_buildup = json_data['setup']
    dadjoke_punchline = json_data['punchline']
    embed=discord.Embed(title=(dadjoke_buildup) + ' ' + (dadjoke_punchline),  color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#kanye
@bot.command()
async def kanye(ctx):
    kanye = requests.get('https://api.kanye.rest/')
    json_data = json.loads(kanye.text)
    kanye_quote = json_data['quote']
    embed=discord.Embed(title=(kanye_quote), description='- Kanye West',  color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#yomama
@bot.command()
async def yomama(ctx):
    yomama = requests.get('https://api.yomomma.info/')
    json_data = json.loads(yomama.text)
    yomama_joke = json_data['joke']
    embed=discord.Embed(title=(yomama_joke),  color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#stock
@bot.command()
async def stock(ctx, arg):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile"
    querystring = {"symbol":(arg)}
    headers = {'x-rapidapi-key': (fapikey),'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    json_data = json.loads(response.text)
    longName = json_data['price']['longName']
    stockPriceFmt = json_data['price']['regularMarketPrice']['fmt']
    stockPriceRaw = json_data['price']['regularMarketPrice']['raw']
    currencySymbol = json_data['price']['currencySymbol']
    embed=discord.Embed(title=(longName), color=(color))
    embed.add_field(name='Raw stock price', value=(currencySymbol) + (str(stockPriceRaw)), inline=True)
    embed.add_field(name='Stock price FMT', value=(currencySymbol) + (stockPriceFmt), inline=True)
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#mcskin command
@bot.command()
async def mcskin(ctx, arg):
    uuidAPI = requests.get('https://api.mojang.com/users/profiles/minecraft/' + (arg))
    uuidjson_data = json.loads(uuidAPI.text)
    uuid = uuidjson_data['id']
    name = uuidjson_data['name']
    embed=discord.Embed(title=(name), color=(color))
    embed.set_image(url='https://crafatar.com/renders/body/' + (uuid) + '?overlay=true&size=1920x1080')
    embed.set_footer(text=(description))
    embed.set_thumbnail(url='https://crafatar.com/renders/head/' + (uuid) + '?overlay=true&size=1080x1080')
    message = await ctx.reply(embed=embed, mention_author=True)

#avatar command
@bot.command()
async def avatar(ctx, *,  user: discord.Member=None):
    try:
        userAvatarUrl =  user.avatar_url
        embed=discord.Embed(title="Avatar", color=(color))
        embed.set_image(url=(userAvatarUrl))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail_small))
        message = await ctx.reply(embed=embed, mention_author=True)
    except:
        userAvatarUrl = ctx.author.avatar_url
        embed=discord.Embed(title="Avatar", color=(color))
        embed.set_image(url=(userAvatarUrl))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail_small))
        message = await ctx.reply(embed=embed, mention_author=True)

#datetime command
@bot.command()
async def datetime(ctx, arg):
    response = requests.get('http://worldclockapi.com/api/json/' + (arg) + '/now')
    json_data = json.loads(response.text)
    timeZoneName = json_data['timeZoneName']
    currentDateTime = json_data['currentDateTime']
    embed=discord.Embed(title=(timeZoneName), description=(currentDateTime),color=(color))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

#the rock
@bot.command()
async def therock(ctx):
    lucky_num = random.randint(0,len(rock_list)-1)
    embed=discord.Embed(title=':smirk:', color=(color))
    embed.set_image(url=(rock_list[lucky_num]))
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail_small))
    message = await ctx.reply(embed=embed, mention_author=True)

#weather command
@bot.command()
async def weather(ctx, arg):
    weatherapi = requests.get('https://api.weatherapi.com/v1/current.json?key=' + (os.getenv('API_KEY')) + '&q=' + (arg))
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
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)

@bot.command()
async def iplookup(ctx, arg):
    ip = requests.get('http://api.ipstack.com/' + (arg) + '?access_key=' + (ipapi_key))
    json_data = json.loads(ip.text)
    ipType = json_data['type']
    continent = json_data['continent_name']
    country = json_data['country_code']
    zipcode = json_data['zip']
    capital = json_data['location']['capital']
    embed=discord.Embed(title=(arg) + ' Lookup result.', color=(color))
    embed.add_field(name="IP address type:", value=(ipType), inline=True)
    embed.add_field(name="Continent:", value=(continent), inline=True)
    embed.add_field(name="Country:", value=':flag_' + (country) + ':', inline=True)
    embed.add_field(name="ZIP code:", value=(zipcode), inline=True)
    embed.add_field(name="Capital:", value=(capital), inline=True)
    embed.set_footer(text=(description))
    embed.set_thumbnail(url=(thumbnail))
    message = await ctx.reply(embed=embed, mention_author=True)


#youtube search command
@bot.command()
async def ytsearch(ctx, *, arg):
    results = YoutubeSearch((arg), max_results=1).to_dict()
    await ctx.reply('https://youtube.com' + (results[0]['url_suffix']))


#spotify cover command
@bot.command()
async def playlist(ctx, arg1, arg2):
    if arg1 == 'cover':
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer BQCtcJQjHtljGXaUlY8XJSyM4HPVkBmlngeiTngp0bpqchy0CgJTVLU6_p6mOkiOGMgt1wSemzkDFT-kiN3YwyFQ37WcRDqH7UbxunAJarJHBMa0lDNlWolY5xkzaRgUeCiWGrYaxajkoLwg9ItW6k493gYl5162VHAwSbA7mJEcJ_2PqG7m4R5bQdj6cH8G5hOI8m8VZG1OiIkxf_2ybqb2XlyYuT4Yn9B_TdpyLNQ7eoF8Z7hS4IIYP9EAILq6wPFDTPE5HiIgrXqM7RTvdH1fdjsE9SexzGqMU8he',}
        playlist_id = (arg2)[34:-20]
        response = requests.get('https://api.spotify.com/v1/playlists/' + (playlist_id) + '/images', headers=headers)
        json_data = json.loads(response.text)
        print(response.text)
        url = json_data[0]['url']
        embed=discord.Embed(title="Playlist Cover", color=(color))
        embed.set_image(url=(url))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail_small))
        message = await ctx.reply(embed=embed, mention_author=True)
    elif arg1 == 'user':
        embed=discord.Embed(title="You found a hidden command! We're still working on it though! :wink:", color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail_small))
        message = await ctx.reply(embed=embed, mention_author=True)
    else:
        embed=discord.Embed(title="Please specify the type of info you want, for now the only option is " + '"cover"', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail_small))
        message = await ctx.reply(embed=embed, mention_author=True)

#music command
# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

#yt dl formatting (used for video downloading)
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect(self_mute=False, self_deaf=True)

    @commands.command()
    async def play(self, ctx, *, arg):
        """Streams from a url (same as yt, but doesn't predownload)"""
        results = YoutubeSearch((arg), max_results=1).to_dict()
        async with ctx.typing():
            player = await YTDLSource.from_url(('https://youtube.com' + (results[0]['url_suffix'])), loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)
        embed=discord.Embed(title=f'Now playing: {player.title}', color=(color))
        embed.set_footer(text=(description))
        embed.set_image(url=(results[0]['thumbnails'][0]))
        embed.set_thumbnail(url=(thumbnail_small))
        message = await ctx.reply(embed=embed, mention_author=True)

    @commands.command()
    async def disconnect(self, ctx):
        """Stops and disconnects the bot from voice"""
        await ctx.voice_client.disconnect()
        embed=discord.Embed(title='Disconnected from voice channel.', color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
                embed=discord.Embed(title="Connected to voice channel!", color=(color))
                embed.set_footer(text=(description))
                embed.set_thumbnail(url=(thumbnail))
                message = await ctx.reply(embed=embed, mention_author=True)
            else:
                embed=discord.Embed(title="You aren't connected to a voice channel!", color=(color))
                embed.set_footer(text=(description))
                embed.set_thumbnail(url=(thumbnail))
                message = await ctx.reply(embed=embed, mention_author=True)
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

@bot.command()
async def help(ctx, *args):
    if not args:
        embed=discord.Embed(title='NULL Help Categories', color=(color))
        embed.add_field(name='Fun commands.', value='`' + (prefix) + 'help -fun`')
        embed.add_field(name='Info commands.', value='`' + (prefix) + 'help -info`')
        embed.add_field(name='Anime commands.', value='`' + (prefix) + 'help -anime`')
        embed.add_field(name='Utility commands.', value='`' + (prefix) + 'help -util`')
        embed.add_field(name='Fun commands.', value='`' + (prefix) + 'help -rand`')
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)
    elif args[0] == "-fun":
        embed=discord.Embed(title='NULL Help. Fun commands.', color=(color))
        embed.add_field(name=(prefix) + 'hello', value='Usually used as a test command ;)')
        embed.add_field(name=(prefix) + 'say', value='Make me say whatever you want!')
        embed.add_field(name=(prefix) + 'm8b', value='Magic 8 ball command.')
        embed.add_field(name=(prefix) + 'compliment', value='Feeling down?')
        embed.add_field(name=(prefix) + 'raost', value="Don't mean to hurt your feelings...")
        embed.add_field(name=(prefix) + 'milkyeet', value='Pretty self explanarory.')
        embed.add_field(name=(prefix) + 'slap', value='Domt you where just wanna slap someone?')
        embed.add_field(name=(prefix) + 'hug', value='<:apple_plead:812381767432536125>')
        embed.add_field(name=(prefix) + 'kiss', value='<:apple_plead:812381767432536125>')
        embed.add_field(name=(prefix) + 'sigh', value=':neutral_face')
        embed.add_field(name=(prefix) + 'clap', value='Proud of someone? Or just sarcastic?...')
        embed.add_field(name=(prefix) + 'headout', value='Going AFK?')
        embed.add_field(name=(prefix) + 'dababy', value='DaBaby lesss gooooo.')
        embed.add_field(name=(prefix) + 'hamster', value='Cute hasmter pictures.')
        embed.add_field(name=(prefix) + 'howsus', value='How sus are you? :flushed:')
        embed.add_field(name=(prefix) + 'howgay', value='How gay are you? (we suport you)')
        embed.add_field(name=(prefix) + 'iq', value="What's your IQ?")
        embed.add_field(name=(prefix) + 'frog', value="Cute frog images :)")
        embed.add_field(name=(prefix) + 'jdm', value="JDM Car images.")
        embed.add_field(name=(prefix) + 'fact', value="Random facts.")
        embed.add_field(name=(prefix) + 'meme', value="Memes from reddit.")
        embed.add_field(name=(prefix) + 'telcel', value="Default Telcel ringtone :smiling_imp:")
        embed.add_field(name=(prefix) + 'diceroll', value="Don't have a physical pair of dice?")
        embed.add_field(name=(prefix) + 'coinflip', value="I'll flip a coin for you ;)")
        embed.add_field(name=(prefix) + 'joke', value="Random dad joke.")
        embed.add_field(name=(prefix) + 'kanye', value="Random kanye west quote")
        embed.add_field(name=(prefix) + 'yomama', value="Random Yo Mama joke.")
        embed.add_field(name=(prefix) + 'mcskin', value="Minecraft head and skin of a player.")
        embed.add_field(name=(prefix) + 'avatar', value="Discord profile picture.")
        embed.add_field(name=(prefix) + 'therock', value="Random Dwayne Johnson memes.")
        embed.add_field(name=(prefix) + 'ytsearch', value="Search on youtube for a video.")
        #embed.add_field(name=(prefix) + 'playlist', value="Playlist cover command") #commented out - Reason: still a work in progress and api breaks frequently
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)
    elif args[0] == "-info":
        embed=discord.Embed(title='NULL Help. Info commands.', color=(color))
        embed.add_field(name=(prefix) + 'stock', value="Specific stock statistics.")
        embed.add_field(name=(prefix) + 'covid/covid19', value="COVID19 Statistics.")
        embed.add_field(name=(prefix) + 'ping', value="My current ping in milliseconds.")
        embed.add_field(name=(prefix) + 'datetime', value="Current date and time of a time zone.")
        embed.add_field(name=(prefix) + 'weather', value="Current weather of a specified city.")
        embed.add_field(name=(prefix) + 'iplookup', value="Get current data of an IP address.")
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)
    elif args[0] == "-rand":
        embed=discord.Embed(title='NULL Help. Random commands commands.', color=(color))
        embed.add_field(name=(prefix) + 'rand -num/number/n', value="Random number between specified limits.")
        embed.add_field(name=(prefix) + 'rand -img/image', value="Random 4k image fron Unsplash.")
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)
    elif args[0] == "-anime":
        embed=discord.Embed(title='NULL Help. Anime commands.', color=(color))
        embed.add_field(name=(prefix) + 'cuteanime', value='Cute anime gifs.')
        embed.add_field(name=(prefix) + 'zerotwo', value='Zero Two gifs.')
        embed.add_field(name=(prefix) + 'todoroki', value='Todoroki gifs.')
        embed.add_field(name=(prefix) + 'ichigo', value='Ichigo gifs.')
        embed.add_field(name=(prefix) + 'bunnygirl', value='Bunny Girl senpai gifs.')
        embed.add_field(name=(prefix) + 'slap', value='Domt you where just wanna slap someone?')
        embed.add_field(name=(prefix) + 'hug', value='<:apple_plead:812381767432536125>')
        embed.add_field(name=(prefix) + 'kiss', value='<:apple_plead:812381767432536125>')
        embed.add_field(name=(prefix) + 'sigh', value=':neutral_face')
        embed.add_field(name=(prefix) + 'clap', value='Proud of someone? Or just sarcastic?...')
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)
    elif args[0] == "-util":
        embed=discord.Embed(title='NULL Help. Utility commands.', color=(color))
        embed.add_field(name=(prefix) + 'inspire', value='Need an inspirational quote?')
        embed.add_field(name=(prefix) + 'rand', value='Random commands.')
        embed.add_field(name=(prefix) + 'stock', value="Specific stock statistics.")
        embed.add_field(name=(prefix) + 'covid/covid19', value="COVID19 Statistics.")
        embed.add_field(name=(prefix) + 'ping', value="My current ping in milliseconds.")
        embed.add_field(name=(prefix) + 'datetime', value="Current date and time of a time zone.")
        embed.add_field(name=(prefix) + 'iplookup', value="Get current data of an IP address.")
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)
    elif args[0] == "-help":
        embed=discord.Embed(title="HEY! This is an ilegal command, you shouldn't be seeing this...", color=(color))
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)
        time.sleep(2.5)
        await message.delete()
    else:
        embed=discord.Embed(title='NULL Help Categories', color=(color))
        embed.add_field(name='Fun commands.', value='`' + (prefix) + 'help -fun`')
        embed.add_field(name='Info commands.', value='`' + (prefix) + 'help -info`')
        embed.add_field(name='Anime commands.', value='`' + (prefix) + 'help -anime`')
        embed.add_field(name='Utility commands.', value='`' + (prefix) + 'help -util`')
        embed.add_field(name='Fun commands.', value='`' + (prefix) + 'help -rand`')
        embed.set_footer(text=(description))
        embed.set_thumbnail(url=(thumbnail))
        message = await ctx.reply(embed=embed, mention_author=True)

""" Embed template
embed=discord.Embed(title='Title Text', color=(color))
embed.set_image(url='https://image-url')
embed.set_footer(text=(description))
embed.set_thumbnail(url=(thumbnail))
message = await ctx.reply(embed=embed, mention_author=True)"""

#run client
bot.add_cog(Music(bot))
bot.run((os.getenv('BOT_TOKEN')))
