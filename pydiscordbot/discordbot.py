import discord
import random
import asyncio
from discord.ext import commands
from discord.ext import tasks
from time import gmtime, strftime
import time, threading, ast, copy
import datetime as dt

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

client = commands.Bot(command_prefix = '.')
descrip = ''
allpass = 0
greetings = ['Hello', 'How are you?', 'Hallo', 'Yo', 'Are you doing okay?', 'How is your day?', "G'day", "What's up", 'Heyo','Well well well.']
statuses = ['Try not to become a man of success, but rather become a man of value.',
            'A winner is a dreamer who never gives up.',
            "You’re off to great places, today is your day. Your mountain is waiting, so get on your way.",
            "You always pass failure on the way to success.",
            "No one is perfect - that’s why pencils have erasers.",
            "Winning doesn’t always mean being first. Winning means you’re doing better than you’ve done before.",
            "You’re braver than you believe, and stronger than you seem, and smarter than you think.",
            "It always seems impossible until it is done.",
            "Keep your face to the sunshine and you cannot see a shadow.",
            "Once you replace negative thoughts with positive ones, you’ll start having positive results.",
            "Positive thinking will let you do everything better than negative thinking will.",
            "In every day, there are 1,440 minutes. That means we have 1,440 daily opportunities to make a positive impact.",
            "The only time you fail is when you fall down and stay down.",
            "When you are enthusiastic about what you do, you feel this positive energy. It’s very simple.",
            "Positive anything is better than negative nothing.",
            "Winning is fun, but those moments that you can touch someone’s life in a very positive way are better.",
            "Virtually nothing is impossible in this world if you just put your mind to it and maintain a positive attitude.",
            "Optimism is a happiness magnet. If you stay positive good things and good people will be drawn to you.",
            "It makes a big difference in your life when you stay positive.",
            "If opportunity doesn’t knock, build a door.",
            "Happiness is an attitude. We either make ourselves miserable, or happy and strong. The amount of work is the same.",
            "You are never too old to set another goal or dream a new dream.",
            "The sun himself is weak when he first rises, and gathers strength and courage as the day gets on.",
            "Tough times never last, but tough people do",
            "It’s not whether you get knocked down, it’s whether you get up.",
            "The struggle you’re in today is developing the strength you need tomorrow.",
            "The way I see it, if you want the rainbow, you gotta put up with the rain.",
            "Every day may not be good... but there’s something good in every day.",
            "Hard work keeps the wrinkles out of the mind and spirit.",
            "The more you praise and celebrate your life, the more there is in life to celebrate.",
            "The difference between ordinary and extraordinary is that little extra.",
            "Be thankful for everything that happens in your life; it's all an experience",
            "Let your unique awesomeness and positive energy inspire confidence in others.",
            "Wherever you go, no matter what the weather, always bring your own sunshine.",
            "If you want light to come into your life, you need to stand where it is shining.",
            "Success is the sum of small efforts repeated day in and day out.",
            "Happiness is the only thing that multiplies when you share it.",
            "When we are open to new possibilities, we find them. Be open and skeptical of everything."]
message_ = ''
channelids = ['761255392969359390', '809500823243587594']
author_ = ''
colours = {
'DEFAULT': 0,
'AQUA': 1752220,
'GREEN': 3066993,
'BLUE': 3447003,
'PURPLE': 10181046,
'GOLD': 15844367,
'ORANGE': 15105570,
'RED': 15158332,
'GREY': 9807270,
'DARKER_GREY': 8359053,
'NAVY': 3426654,
'DARK_AQUA': 1146986,
'DARK_GREEN': 2067276,
'DARK_BLUE': 2123412,
'DARK_PURPLE': 7419530,
'DARK_GOLD': 12745742,
'DARK_ORANGE': 11027200,
'DARK_RED': 10038562,
'DARK_GREY': 9936031,
'LIGHT_GREY': 12370112,
'DARK_NAVY': 2899536,
'LUMINOUS_VIVID_PINK': 16580705,
'DARK_VIVID_PINK': 12320855
}

def convertExpr2Expression(Expr):
        Expr.lineno = 0
        Expr.col_offset = 0
        result = ast.Expression(Expr.value, lineno=0, col_offset = 0)

        return result
def execute(code):
    code_ast = ast.parse(code)

    init_ast = copy.deepcopy(code_ast)
    init_ast.body = code_ast.body[:-1]

    last_ast = copy.deepcopy(code_ast)
    last_ast.body = code_ast.body[-1:]

    exec(compile(init_ast, "<ast>", "exec"), globals())
    if type(last_ast.body[0]) == ast.Expr:
        return eval(compile(convertExpr2Expression(last_ast.body[0]), "<ast>", "eval"),globals())
    else:
        exec(compile(last_ast, "<ast>", "exec"),globals())

@client.event
async def onready():
    #school_alert.start()
    print('Bot is ready')

    

@client.event
async def on_message(message):
    global greetings, message_, author_, channelids
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"to the quote: "))
    id = client.get_guild(API_KEY)
    greeting = random.choice(greetings)
    message_ = message
    author_ = str(message.author)
    if str(message.channel.id) not in channelids:
        file = open('chatlogs.txt','a',encoding='utf-8') 
        file.write(f'{message.author} [{message.author.display_name}]: {message.content} [id: {str(message.id)}] in {message.channel} [id: {str(message.channel.id)}] at {str(message.created_at)}\n')
        file.close()
        embed = discord.Embed(
            timestamp = message.created_at,
            title = "[Message Sent]",
            color = 1752220
            ) 
        embed.set_author(name=f'{message.author.name}#{message.author.discriminator}', icon_url=message.author.avatar_url)
        embed.set_footer(text=f"Author ID:{message.author.id} • Message ID: {message.id}")
        embed.set_thumbnail(url = message.author.avatar_url)
        embed.add_field(name="Message Content:", value=message.content)
        embed.add_field(name="Message Channel:", value=f'{str(message.channel)}')
        channel = client.get_channel(809500823243587594)
        await channel.send(embed=embed)
    if message.content.find('!hello') != -1:
        await message.channel.send(greeting)
    elif message.content == 'hello':
        await message.channel.send(greeting)
    elif message.content == '.users':
        embed = discord.Embed(title=f"Members", description=f"Current Member Count:", color=1752220)
        embed.set_footer(text=f"{id.member_count}")
        await message.channel.send(embed=embed)
    await client.process_commands(message)
@client.event
#{message.author} [{message.author.display_name}]
#{message.author.name}#{message.author.discriminator}
async def on_message_delete(message):
    global channelids
    if str(message.channel.id) not in channelids:
        file = open('chatlogs.txt','a',encoding='utf-8') 
        file.write(f'Message Deleted: "{message.content}" , message owner: {message.author} [{message.author.display_name}] in {message.channel}\n')
        file.close()
    await client.process_commands(message)

    

@client.command(aliases = ['embed_builder', 'embed_build', 'build_embed', 'embedbuilder'])
async def embed(ctx, title, desc, colour, *,footer):
    if colour in colours and title != '' and desc != '' and colour != '' and footer != '':
        embed = discord.Embed(title=f"{title}", description=f"{desc}", color=colours[colour])
        embed.set_footer(text=f"{footer}")
        await ctx.send(embed=embed)
    else:
        await ctx.send('Syntax Error: .embed[args] args: title, description, colour and footer')

@client.command()
async def greet(ctx):
    global greetings
    greeting = random.choice(greetings)
    await ctx.send(f"{greeting}")

    
@client.command()
@commands.has_role('BAADev')
async def send_dm(ctx, member: discord.Member, *, content):
    if ctx.message.author == client.user:
        return
    channel = await member.create_dm()
    await channel.send(content)

@client.event
async def on_message_delete(message):
    global channelids
    if str(message.channel.id) not in channelids:
        embed = discord.Embed(
            timestamp = message.created_at,
            title = "[Message Deleted]",
            color = 1752220
            ) 
        embed.set_author(name=f'{message.author.name}#{message.author.discriminator}', icon_url=message.author.avatar_url)
        embed.set_footer(text=f"Author ID:{message.author.id} • Message ID: {message.id}")
        embed.set_thumbnail(url = message.author.avatar_url)
        embed.add_field(name="Message Content:", value=message.content)
        embed.add_field(name="Message Channel:", value=f'{str(message.channel)}')
        channel = client.get_channel(809500823243587594)
        await channel.send(embed=embed)
    await client.process_commands(message)
@client.event
async def status():
    await client.wait_until_ready()
    while True:
        status = random.choice(statuses)
        activityvar = discord.Activity(type=discord.ActivityType.listening,name = f'to the quote, {status}')
        embed = discord.Embed(
            title = "[Positive Quote]",
            description = '',
            color = 3066993
        )
        embed.set_footer(text='')
        embed.add_field(name="Quote:", value=status)
        channel = client.get_channel(829086658556461097)
        await channel.send(embed=embed)
        await client.change_presence(activity=activityvar)
        await asyncio.sleep(5)

said = False
savedtime = ''

async def school_alert():
    global said, savedtime
    await client.wait_until_ready()
    channel = client.get_channel(814558597978521683)
    times = {'08:55': 'First lesson alert! Get ready for lesson one <@&794532023796498451>', '09:00': 'First lesson alert! Your lesson has started get to it now! <@&794532023796498451>', '10:00': 'Your lesson one has ended! Time to go to your second lesson! <@&794532023796498451>', '11:00': 'Your lesson two has ended, you can have a small break now. <@&794532023796498451>', '11:25': 'Lesson three alert! Please get ready to get to your next lesson. <@&794532023796498451>', '12:30': 'Your lesson three has ended, please go get some food and get some exercise or rest. <@&794532023796498451>', '12:55': 'Lesson four alert! Please get ready to go to your fourth lesson. <@&794532023796498451>', '13:00': 'Lesson alert! Please get to your fourth lesson. (Last lesson if it is Thursday!) <@&794532023796498451>', '14:00': 'Your lesson four has ended, please get to your next lesson. (Have a nice day if it is Thursday!) <@&794532023796498451>', '15:00': 'End of the day! You have no more lesson cool! (Unless it is Thursday of course!)<@&794532023796498451>'}
    while True:
        await asyncio.sleep(1)
        if strftime('%H:%M') != savedtime and strftime('%H:%M') in times:
            said = False
        if strftime('%H:%M') in times:
            if said != True:
                said = True
                savedtime = strftime('%H:%M')
                #await client.send_message(discord.Object(id='814558597978521683'), 'hello')
                #await channel.send(times[strftime('%H:%M')])
@client.command()
async def runcode(ctx,*, content):
    #value = compile(content, '<string>', 'exec')
    value = execute(content)
    #exec(value)
    #b = ast.literal_eval(content)
    #print(value)
    channel = client.get_channel(829086658556461097)
    await channel.send(value)
    #await ctx.send(value)
    
#client.loop.create_task(school_alert())
#client.loop.create_task(status())


#print(strftime('%a, %d %b %Y %H:%M:%S', gmtime()))
#if strftime('%H:%M:', gmtime()) == '17:59':
#    print('ser')
#else:
#    print(strftime('%H:%M'))
    
#schedule.every(10).seconds.do(job)
#schedule.every().day.at("10:30").do(job)
client.run('NzYzMzQyODI3NjU2MTgzODE4.X32UaA.rFuOgmEVTp2D4gVA2d8CYOTbWTQ')
