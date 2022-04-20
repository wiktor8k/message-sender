import discord, asyncio
from discord.ext import commands
from datetime import timedelta, datetime

import os

intents = discord.Intents.all()


client = commands.Bot(intents = intents, fetch_offline_members = True, command_prefix = "")

guild = None

fabyn = None
fetardes = None

FABYN_ID = 334766583790567425
FETARDES_ID = 315048337612996608

@client.event
async def on_ready():
  global guild, fabyn, fetardes
  guild = client.guilds[0]

  for member in guild.members:
    if member.id == FABYN_ID:
      fabyn = member
    if member.id == FETARDES_ID:
      fetardes = member

    if fetardes != None and fabyn != None:
      break
      
      
  await fabyn.send("Ready!")
  print("Ready!")

  while True:
    await asyncio.sleep(1)
    now = datetime.now() + timedelta(hours = 2)
    
    if now.day == 15:
      await fetardes.send("https://youtu.be/t0k9SgCSWzQ")
      await fetardes.send("**TO TWOJE URODZINY DZIIIIŚ**")
      await fetardes.send("**ADAM**")
      await fetardes.send("**...**")
      await fetardes.send("**JA PRAWDOPODOBNIE TERA ŚPIE**")
      await fetardes.send("**...**")
      await fetardes.send("**ADAM**")
      
      await fabyn.send("**MISZYN AKOMPLISZT** bleee")
      break
    

@client.event
async def on_message(ctx):
  if "avatar" in ctx.content and client.id in [member.id for member in ctx.mentions]:
    for member in ctx.mentions:
      if member.id != client.id:
        await ctx.channel.send(member.avatar_url)
        
  
  if ctx.author.bot or not isinstance(ctx.channel, discord.channel.DMChannel):
    return

  global fabyn
  
  await ctx.channel.send("twoja mama bip bop")

  if fabyn != None:
    await fabyn.send(ctx.author.name + ": " + ctx.content)
    
    
token = "OTYzODUxMTcxMjA5MDE5Mzky." + "YlcGWg.J-ylJLO" + "YF7NphOfUZHiMZCpAbaQ"
client.run(token)

