import discord 
import tkinter as tk
from tkinter.filedialog import askopenfilename
import time

client = discord.Client()
tk.Tk().withdraw() 
clienttxt = askopenfilename()
guild_var = '&<something> ' #if you don't have a tag you'll just use '&' as far as i know, otherwise '&<something> ' is for the guild tag 'something' and the the space is included for formatting purposes of the output

#define function for reading
def return_guild_message(clientfile):
    """A function that prints out the guild chat entries of client.txt."""
    f = open(clientfile, encoding='utf-8')
    f.seek(0,2)
    while True:
        line = f.readline()
        if guild_var in line:
            temp_string_list = line.split(guild_var)
            final_string = temp_string_list[1]
            return final_string
        else:
            continue

#When the bot is up and running the terminal will have a print out, and then it runs a whle loop which checks against a global variable which our python script creates while reading Client.txt file.            
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel("""You'll have to get the specific channel's id, i guess you could have another command for this part, sorry I didn't include it""")
    last_message = None
    while True:
        outputG = return_guild_message(clienttxt)
        if outputG != last_message:
            last_message = outputG
            await channel.send(outputG)
        else:
            time.sleep(0.1)
            continue
         
#this runs the bot, need to pass in your bots token
client.run(' """Your bot token goes here, with the quotes""" ')
