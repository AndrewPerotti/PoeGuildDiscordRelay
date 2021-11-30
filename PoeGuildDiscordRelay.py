import discord 
import tkinter as tk
from tkinter.filedialog import askopenfilename
import time

client = discord.Client()
clienttxt = 'C:/Program Files (x86)/Grinding Gear Games/Path of Exile/logs/Client.txt' #This is the path to your Client.txt.
guild_var = '&<guild> ' #this is not only your guild tag but is also used with the split method to format output, the space after the > is required

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(#here you need to input a channel id#, you'll need to figure that out on your own)
    last_message = None
    with open(clienttxt, encoding = 'utf-8') as f:
        f.seek(0,2)
        while True:
            line = f.readline()
            if guild_var in line:
                temp_string_list = line.split(guild_var)
                final_string = temp_string_list[1]
                await channel.send(final_string)
                print(final_string)
            else:
                time.sleep(0.1)
                continue

client.run('#this will be the token of your bot, and you need to keep the quotes')
