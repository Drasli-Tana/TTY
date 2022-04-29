"""
Created on 29 avr. 2022

@author: Thomas
"""
import discord.ext.commands as DC
import os
import json
import src.stack as ST

class Command_ls(DC.Command):
    options = {
        "-a": False,
        "-d": False,
        "-R": False,
        "-s": False}
    def __init__(self):
        super().__init__(self.ls)
        self.name = "ls"
        self.brief = "Liste le contenu du répertoire ciblé"
    
    async def ls(self, ctx):
        rootPath = f"root/{ctx.author.id}"
        if not os.path.exists(rootPath):
            os.mkdir(rootPath)
        
        pile = ST.Stack()
        options = dict()
        
        for param in reversed(ctx.message.content.split(" ")[1:]):
            if param in Command_ls.options:
                if Command_ls.options.get(param):
                    try:
                        options[param] = pile.pop()
                        
                    except IndexError:
                        print("Error, option requires argument.")
                    
                else:
                    options[param] = None
            
            else:
                pile.append(param)
        
        files = dict()
        while not pile.isEmpty():
            chemin = pile.pop()
            if chemin.startswith("/"):
                chemin = rootPath + chemin
            
            else:
                with open("data/directory.json") as file:
                    chemin = json.load(file).get(
                        f"{ctx.author.id}", rootPath) + f"/{chemin}"
            
            files[chemin] = os.listdir(chemin)
        
        else:
            with open("data/directory.json") as file:
                chemin = json.load(file).get(f"{ctx.author.id}", rootPath)
                files[chemin] = os.listdir(chemin)
        
        if ctx.message.author.dm_channel is None:
            ctx.author.create_dm()
        
        await ctx.author.message.dm_channel.send(
            "\n".join(["\t" + chemin + "\n" + "\n".join(files[chemin])
                       for chemin in files]))
