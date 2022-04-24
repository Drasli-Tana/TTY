"""
Created on 24 avr. 2022

@author: Thomas
"""
import discord.ext.commands as DC
import os

class TTYBot(DC.Bot):
    commands = {
        "ls": None,
        "mkdir": None,
        "cd": None}
    
    async def on_message(self, message):
        DC.Bot.on_message(self, message)
        
        
        