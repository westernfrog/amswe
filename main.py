import discord
from discord.ext import commands, tasks
import aiohttp
import os
import random
import asyncio


client = commands.Bot(command_prefix = "", intents = discord.Intents.all())

for folder in os.listdir("./programs"):
    if folder.endswith(".py"):
        client.load_extension(f'programs.{folder[:-3]}')


        
@tasks.loop(hours=7)
async def loop():
            async with aiohttp.ClientSession() as cs:
                animals = ["dog","cat","panda","koala","birb"]
                ani = random.choice(animals)
                async with cs.get("https://some-random-api.ml/img/"+ani) as r:
                    data = await r.json()
                    emoji = ["💞","💗","🧡","💛","💚","💙","💜","🤎","🖤","🤍","💓","💖","💟","💌","💝","💘","❣️"]
                    emo = random.choice(emoji)
                    embed = discord.Embed(title="this "+ani+" orders you to stay hydrated "+emo+emo,color=0x9b59b6)
                    embed.set_image(url=data['link'])
                    channel = client.get_channel(889003570890952737)
                    await asyncio.sleep(6800)
                    await channel.send(embed=embed)
                             
                
@client.event
async def on_connect():
  print("bot is online")
  await client.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name="swetha + aman = sweam"))
  loop.start()

@client.event
async def on_message(message):
  
  if message.content.startswith("i love you"):
    await message.add_reaction('💗')
  elif message.content.startswith("sorry"):
    msg = await message.channel.send("please forgive and forget it")
    await asyncio.sleep(5)
    await msg.delete()
  elif message.content.startswith("wel cum"):
    await message.add_reaction('💦')
  elif message.content.startswith("cum"):
    await message.add_reaction('🥵')
  elif message.content.startswith("swetha"):
    await message.add_reaction('💛')
    await message.add_reaction('💜')
    await message.add_reaction('💚')
    await message.add_reaction('❤️')
 

  await client.process_commands(message)
    
token = ""

client.run(token)