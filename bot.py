import discord
import random
import json
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "$")
os.chdir(r"C:\Users\willg\Desktop\starlight")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_connect():
    pass

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ["Fuck yeah baby",
                 "Definitely",
                 "For sure",
                 "Survey says 41% chance",
                 "Yeah",
                 "No doubt",
                 "Prob not chief :/",
                 "Sources are telling me... no",
                 "Nah",
                 "That's gonna be a no from me",
                 "No",
                 "Hell no"]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# @client.event
# async def on_member_join(member):
#     with open('users.join', 'r') as f:
#         users = json.load(f)
#
#     await update_data(users, member)
#
#
#     with open('users.json', 'w') as f:
#         json.dump(users, f)
#
# @client.event
# async def on_message(message):
#     with open('users.json', 'r') as f:
#         users = json.load(f)
#
#     await update_data(users, message.author)
#     await add_experience(users, message.author, 5)
#     await level_up(users, message.author, message.channel)
#
#
#     with open('users.json', 'w') as f:
#         json.dump(users, f)
#
# async def update_data(users, user):
#     if not user.id in users:
#         users[user.id] = {}
#         users[user.id]['experience'] = 0
#         users[user.id]['level'] = 1
#
# async def add_experience(users, user, exp):
#     users[user.id]['experience'] += exp
#
# async def level_up(users, user, channel):
#     experience = users[user.id]['experience']
#     lvl_start = users[user.id]['level']
#     lvl_end = int(experience ** (1/4))
#
#     if lvl_start < lvl_end:
#         await client.send_message(channel, '{} has leveled up to level {}'.format(user.mention, lvl_end))
#         users[user.id]['level'] = lvl_end

client.run("NjgzMTQ5MDI3NDk1MjQ3OTEy.XlncXA.a6LynwLi65C02p11fYJipxKGPpU")
