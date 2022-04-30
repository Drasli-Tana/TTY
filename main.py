'''
Created on 24 avr. 2022

@author: Thomas
'''
import discord.ext.commands as DC
import src.commands.ls as SL
import json
import os

bot = DC.Bot("")

@bot.event
async def on_ready():
    print("All systems are up.")

bot.add_command(SL.Command_ls())

if not os.path.exists("root"):
    os.mkdir("root")

if not os.path.exists("data/directory.json"):
    with open("data/directory.json", mode="w") as file:
        json.dump(dict(), file, indent=4)

with open("data/settings.json") as file:
    bot.run(json.load(file).get("token"))
    