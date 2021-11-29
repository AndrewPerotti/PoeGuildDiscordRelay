import discord 
import tkinter as tk
from tkinter.filedialog import askopenfilename
import time

client = discord.Client()
tk.Tk().withdraw() 
clienttxt = askopenfilename()
guild_var = '&<Jë§µs†> '

#define function for reading
def return_guild_message(clientfile):
    """A function that prints out the guild chat entries of client.txt."""
    with open(clientfile, encoding='utf-8') as f:
        f.seek(0,2)
        while True:
            line = f.readline()
            if guild_var in line:
                temp_string_list = line.split(guild_var)
                final_string = temp_string_list[1]
                return final_string
            else:
                continue

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel("""Channel ID""")
    last_message = None
    while True:
        outputG = return_guild_message(clienttxt)
        if outputG != last_message:
            last_message = outputG
            await channel.send(outputG)
        else:
            time.sleep(0.1)
            continue








client.run('"""bot token"""')


