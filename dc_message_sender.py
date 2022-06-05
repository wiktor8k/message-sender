
import discord, asyncio
from discord.ext import commands
from datetime import timedelta, datetime

import os

intents = discord.Intents.all()

FABYN_ID = 334766583790567425

client = commands.Bot(intents = intents, fetch_offline_members = True, command_prefix = "")

guild = None

@client.event
async def on_ready():
  global guild
  guild = client.guilds[0]

  for member in guild.members:
   if member.id == FABYN_ID:
     fabyn = member

  await fabyn.send("Ready! Steady!")
  print("Ready! Steady!")

  while True:
    await asyncio.sleep(1)
    now = datetime.now() + timedelta(hours = 2)
    
    

@client.event
async def on_message(ctx):

# retrieve avatar command
  if "avatar" in ctx.content and client.id in [member.id for member in ctx.mentions]:
    for member in ctx.mentions:
      if member.id != client.id:
        await ctx.channel.send(member.avatar_url)
        
# other utilities
  if ctx.channel.id == 983107236693954561:
    if "gif" in ctx.content:
      await ctx.delete()
      
    else:
      counter = 0
      async for message in ctx.channel.history(limit=200):
        if message.author == ctx.author:
          counter += 1
        if counter == 2:
          await ctx.delete()
          break
    
token = "OTYzODUxMTcxMjA5MDE5Mzky." + "YlcGWg.J-ylJLO" + "YF7NphOfUZHiMZCpAbaQ"
client.run(token)

