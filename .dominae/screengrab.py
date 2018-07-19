#Screengrabbot by Ewi OwO

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import datetime
from datetime import datetime
from os import path
import asyncio
import subprocess

client = commands.Bot(command_prefix='>')
cwd = path.abspath(path.curdir + "dominae")

@client.event
async def on_ready():
    print ("Bot Core Ready \n")

@client.event
async def on_message(message):
    channel = message.channel
    author = message.author

    # do things lol
    
    if message.content.startswith('sfull'):
        subprocess.check_output(cwd + "/sfull.sh")
        await channel.send(file=discord.File(cwd + "/sfull.png"))
        print ("Full Screenshot Uploaded ")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('swindow'):
        subprocess.check_output(cwd + "/swindow.sh")
        await channel.send(file=discord.File(cwd + "/swindow.png"))
        print ("Window Screenshot Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('sselect'):
        subprocess.check_output(cwd + "/sselect.sh")
        await channel.send(file=discord.File(cwd + "/sselect.png"))
        print ("Rectangle Select Screenshot Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('sweb'):
        subprocess.check_output(cwd + "/sweb.sh")
        await channel.send(file=discord.File(cwd + "/sweb.png"))
        print ("Webshot Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('smov'):
        await channel.send("Recording...Please wait 10s")
        subprocess.check_output(cwd + "/smov.sh")
        await channel.send(file=discord.File(cwd + "/smov.webm"))
        print ("Webm Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('sfortune'):
        subprocess.check_output(cwd + "/sfortune.sh")
        await channel.send(file=discord.File(cwd + "/sfortune.png"))
        print ("Fortune Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('ssay'):
        message = message.content
        f = open(cwd + '/ssay.txt','w')
        f.write(message.replace("ssay ",""))
        f.close()
        subprocess.check_output(cwd + "/ssay.sh")
        await channel.send(file=discord.File(cwd + '/ssay.png'))
        print ("Phrase Uploaded")
        print ("'" + message.replace("ssay ","") + "'")
        print ('by {} at {} \n'.format(author, str(datetime.now())))





















client.run("MzM3MjYzODE3ODExNjg5NDcz.Di7oUA.pbc_4b0UhBkDr-KC38VMFIvyAEE")