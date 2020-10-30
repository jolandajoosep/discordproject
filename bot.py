import discord
import os
from discord.utils import get
from discord.ext import commands

TOKEN = 'NzcwMjY3MjQ2NzYwNDI3NTcy.X5bFRg.ihdj_TfHA3-n7Ua5geBjAk2ZBw8'
client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("ROFL"))
    print('Logged in as')
    print(client.user)
    print('------')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.event
async def on_member_join(member):
    print(f'{member} has been connected to a server.')

@client.event
async def on_member_leave(member):
    print(f'{member} has been disconnected from a server.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Sorry, I am not able to understand your command. :3")


@client.event
async def on_message(message):
    if message.author.id == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f' {message.author.mention} HI!')

    if message.content.startswith('ВЫ ГОТОВЫ ДЕТИ?'):
        await message.channel.send(f' {message.author.mention} ДА, КАПИТАН')


client.run('NzcwMjY3MjQ2NzYwNDI3NTcy.X5bFRg.ihdj_TfHA3-n7Ua5geBjAk2ZBw8')


