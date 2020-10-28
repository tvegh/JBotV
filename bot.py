import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

import markovify

import re

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='jbot ')
messages = []


jbv = open('jbv.txt', encoding='utf-16').read()
whymans = open('whymans.txt', encoding='utf-16').read()
trump = open('trump.txt', encoding='utf-8').read()
# atomic = open('atomic.txt', encoding='utf-16').read()
# helly = open('helly.txt', encoding='utf-16').read()
# tbj = open('tbj.txt', encoding='utf-16').read()
jbvModel = markovify.Text(jbv)
whymansModel = markovify.Text(whymans)
trumpModel = markovify.Text(trump)
# atomicModel = markovify.Text(atomic)
# hellyModel = markovify.Text(helly)
# tbjModel = markovify.Text(tbj)


@bot.command(name='leave')
async def leave(ctx):
    await bot.close()

@bot.command(name='retrieve')
async def retrieve(ctx):
    print('retrieving')
    guild = ctx.guild
    genChat = discord.utils.get(guild.channels, name='general')
    async for message in genChat.history(limit=50000):
        if message.author.name == 'jaybeeveee':
            if '<@!' in message.content:
                print('yes')
                reString = re.sub(r'<@![0-9]*>', r'', message.content)
                messages.append(reString)
            elif '<@' in message.content:
                print('yes2')
                reString = re.sub(r'<@[0-9]*>', r'', message.content)
                messages.append(reString)
            else:
                print('no')
                messages.append(message.content)
    with open('jbv.txt', 'w', encoding='utf-16') as file:
        for x in messages:
            file.write(x)
            file.write('\n')
    print('retrieve successful')

# @bot.command(name='retrieveAtomic')
# async def retrieve(ctx):
#     print('retrieving')
#     guild = ctx.guild
#     genChat = discord.utils.get(guild.channels, name='general')
#     async for message in genChat.history(limit=50000):
#         if message.author.name == 'Atomic':
#             if '<@!' in message.content:
#                 print('yes')
#                 reString = re.sub(r'<@![0-9]*>', r'', message.content)
#                 messages.append(reString)
#             elif '<@' in message.content:
#                 print('yes2')
#                 reString = re.sub(r'<@[0-9]*>', r'', message.content)
#                 messages.append(reString)
#             else:
#                 print('no')
#                 messages.append(message.content)
#     with open('atomic.txt', 'w', encoding='utf-16') as file:
#         for x in messages:
#             file.write(x)
#             file.write('\n')
#     print('retrieve successful')

# @bot.command(name='retrieveHelly')
# async def retrieve(ctx):
#     print('retrieving')
#     guild = ctx.guild
#     genChat = discord.utils.get(guild.channels, name='general')
#     async for message in genChat.history(limit=50000):
#         if message.author.name == 'Hellyaman':
#             if '<@!' in message.content:
#                 print('yes')
#                 reString = re.sub(r'<@![0-9]*>', r'', message.content)
#                 messages.append(reString)
#             elif '<@' in message.content:
#                 print('yes2')
#                 reString = re.sub(r'<@[0-9]*>', r'', message.content)
#                 messages.append(reString)
#             else:
#                 print('no')
#                 messages.append(message.content)
#     with open('helly.txt', 'w', encoding='utf-16') as file:
#         for x in messages:
#             file.write(x)
#             file.write('\n')
#     print('retrieve successful')

# @bot.command(name='retrieveTbj')
# async def retrieve(ctx):
#     print('retrieving')
#     guild = ctx.guild
#     genChat = discord.utils.get(guild.channels, name='general')
#     async for message in genChat.history(limit=50000):
#         if message.author.name == 'TeaBoneJones':
#             if '<@!' in message.content:
#                 print('yes')
#                 reString = re.sub(r'<@![0-9]*>', r'', message.content)
#                 messages.append(reString)
#             elif '<@' in message.content:
#                 print('yes2')
#                 reString = re.sub(r'<@[0-9]*>', r'', message.content)
#                 messages.append(reString)
#             else:
#                 print('no')
#                 messages.append(message.content)
#     with open('tbj.txt', 'w', encoding='utf-16') as file:
#         for x in messages:
#             file.write(x)
#             file.write('\n')
#     print('retrieve successful')

@bot.command(name='all')
async def all(ctx):
    print('retrieving')
    guild = ctx.guild
    genChat = discord.utils.get(guild.channels, name='general')
    async for message in genChat.history(limit=50000):
        if '<@!' in message.content:
                print('yes')
                reString = re.sub(r'<@![0-9]*>', r'', message.content)
                messages.append(reString)
        elif '<@' in message.content:
                print('yes2')
                reString = re.sub(r'<@[0-9]*>', r'', message.content)
                messages.append(reString)
        else:
            print('no')
            messages.append(message.content)
    with open('whymans.txt', 'w', encoding='utf-16') as file:
        for x in messages:
            file.write(x)
            file.write('\n')
    print('retrieve successful')

@bot.command(name='brother')
async def brother(ctx):
    await ctx.send(jbvModel.make_sentence())

# @bot.command(name='atomic')
# async def atomic(ctx):
#     await ctx.send(atomicModel.make_sentence())

# @bot.command(name='helly')
# async def helly(ctx):
#     await ctx.send(hellyModel.make_sentence())

# @bot.command(name='tbj')
# async def tbj(ctx):
#     await ctx.send(tbjModel.make_sentence())

@bot.command(name='whymans')
async def whymans(ctx):
    await ctx.send(whymansModel.make_sentence())
  
@bot.command(name='trump')
async def trump(ctx):
    await ctx.send(trumpModel.make_sentence())

bot.run(token)