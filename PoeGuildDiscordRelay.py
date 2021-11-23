#channelid 911288162662350909
#token: OTEyNzc2OTIwNzg4MjYyOTUy.YZ03wA.fKz-iMl24Y3fdZ1WwtcLdWllnYk

import discord 
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
import time
import pyperclip

client = discord.Client()
tk.Tk().withdraw() 
clienttxt = askopenfilename()


#define function for reading
def return_guild_message(clientfile):
    """A function that prints out the guild chat entries of client.txt."""
    f = open(clientfile, encoding='utf-8')
    f.seek(0,2)
    while True:
        line = f.readline()
        if "&" in line:
            line.encode(encoding='UTF-8', errors='replace')
            pyperclip.copy(line[52:])
            return pyperclip.paste()
        else:
            continue

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(911288162662350909)
    last_message = None
    while True:
        outputG = return_guild_message(clienttxt)
        if outputG != last_message:
            last_message = outputG
            await channel.send(outputG)
        else:
            time.sleep(0.1)
            continue








client.run('OTEyNzc2OTIwNzg4MjYyOTUy.YZ03wA.fKz-iMl24Y3fdZ1WwtcLdWllnYk')


