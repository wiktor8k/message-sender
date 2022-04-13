import discord
from discord.ext import commands
from datetime import timedelta, datetime

import os

intents = discord.Intents.all()


client = commands.Bot(intents = intents, fetch_offline_members = True, command_prefix = "")

guild = None

fabyn = None
fetardes = None

FABYN_ID = 334766583790567425
FETARDES_ID = 334766583790567425

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

  while True:
    now = datetime.now() + timedelta(hours = 2)
    
    await fabyn.send(f"{now.day}d {now.hour}h {now.minute}m {now.second}s")

    if now.day == 14 or now.minute == 21:
      await fetardes.send("https://youtu.be/t0k9SgCSWzQ")
      await fetardes.send("**TO TWOJE URODZINY DZIIIIŚ**")
      await fetardes.send("**ADAM**")
      await fetardes.send("**...**")
      await fetardes.send("**JA PRAWDOPODOBNIE TERA ŚPIE**")
      await fetardes.send("**...**")
      await fetardes.send("**ADAM**")
      break
    

@client.event
async def on_message(ctx):
  if ctx.author.bot:
    return

  global fabyn
  
  await ctx.channel.send("twoja mama bip bop")

  if fabyn != None:
    await fabyn.send(ctx.author.name + ": " + ctx.content)
    
    
token = "OTYzODUxMTcxMjA5MDE5Mzky.YlcGWg.IjhKQM9cpt79GNZJ_j6rVMz8Kf4"
client.run(token)
