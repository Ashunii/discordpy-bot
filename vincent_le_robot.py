import discord
from discord.ext import commands
import asyncio
import random
import imghdr
bot = commands.Bot(command_prefix='µ')
TOKEN = 'NjgyMTUyNDMwNDQzNDI5ODg4.XlY2CA.0PTvxYeLRTFfRy2dxUpuLsWhSEg'

@bot.event
async def on_ready():
    print('Bot online !')

@bot.event
async def on_guild_join(guild):
    text_channels = guild.text_channels
    for i in text_channels:
        if i.name == 'general':
            general = i
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Hello {}!'.format(guild.name))
        await general.send('commands at µWhelp')

@bot.command()
async def Whelp(ctx):
    await ctx.author.send(whelp())
     
@bot.command()
async def Information(ctx):
    await ctx.send('the user {} first use discord on {}'.format(ctx.author.name,ctx.author.created_at))

@bot.command()
async def Challenge(ctx, members: commands.Greedy[discord.Member] ):
    challenge = members[0]
    await ctx.send('the user {} challenge {} !'.format(ctx.author.name,challenge.mention))

@bot.command()
async def Patate(ctx):
    x = random.randint(1,5)
    try:
        await ctx.channel.send(file=discord.File("patate/{}.jpg".format(x)))
    except:
        await ctx.channel.send(file=discord.File("patate/{}.png".format(x)))

def whelp():
    whelp  = 'µWhelp - return list of commands\n'
    whelp += 'µInformation - return user information in mp\n'
    whelp += 'µChallenge - return the challenge\n'
    return whelp

bot.run(TOKEN)