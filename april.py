import os
import random
import json

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
    
client = discord.Client()

@client.event
async def on_ready():
    guild = client.get_guild(GUILD)
    print(
        'Connection established\n'
        f'User name: {client.user.name}\n'
        f'User ID: {client.user.id}\n'
        f'Guild name: {guild.name}\n'
        f'Guild ID: {guild.id}'
    )

@client.event
async def on_message(message):
    guild = client.get_guild(GUILD)
    with open('user_dict.json', 'r') as USER_DICT_FILE:
        user_dict = json.load(USER_DICT_FILE)

    if message.author == client.user:
        return

    if message.content.startswith('~generate'):
        async with message.channel.typing():
            user_dict = {}
            for member in guild.members:
                user_dict[member.id] = (random.choice(guild.members).display_name, member.display_name)
    
            with open('user_dict.json', 'w') as USER_DICT_FILE:
                json.dump(user_dict, USER_DICT_FILE)
            await message.channel.send("All members have been assigned a random name; use ~rename to enable them and ~restore to disable them")

    if message.content.startswith('~rename'):
        async with message.channel.typing():
            for member in user_dict.keys():
                try:
                    await guild.get_member(int(member)).edit(nick=user_dict[member][0])
                    print(f'{guild.get_member(int(member))} renamed to {user_dict[member][0]}')
                except Exception as e:
                    print(e)
                    continue
            await message.channel.send("Members now have their new names")
    
    if message.content.startswith('~restore'):
        async with message.channel.typing():
            for member in user_dict.keys():
                try:
                    await guild.get_member(int(member)).edit(nick=user_dict[member][1])
                    print(f'{guild.get_member(int(member))} renamed to {user_dict[member][1]}')
                except Exception as e:
                    print(e)
                    continue
            await message.channel.send("Members now have their old names")

client.run(TOKEN)
