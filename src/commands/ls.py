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
        self.help = ("Permet de lister le contenu du dossier spécifié, il " +
                     "n'y a pas d'options pour l'instant")
        
        self.usage = "[option...][chemin...]"
    
    async def ls(self, ctx):
        if ctx.message.author.dm_channel is None:
            await ctx.message.author.create_dm()
        
        if ctx.message.guild is not None:
            await ctx.message.author.dm_channel.send(
                "Ces commandes ne peuvent être utilisées que dans " + 
                "les messages privés")
            
        rootPath = f"root/{ctx.author.id}"
        joker = False
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
                if "*" in param:
                    param = param.replace("*", "")
                    joker = True
                pile.append(param)
        
        files = dict()
        if pile.isEmpty():
            with open("data/directory.json") as file:
                chemin = json.load(file).get(f"{ctx.author.id}", rootPath)
                files[chemin] = os.listdir(chemin)
        
        else:
            while not pile.isEmpty():
                chemin = pile.pop()
                if chemin.startswith("/"):
                    currentDir = rootPath
                
                else:
                    with open("data/directory.json") as file:
                        currentDir = json.load(file).get(
                            f"{ctx.author.id}", rootPath) + "/"
                        
                if not os.path.abspath(currentDir + chemin).startswith(
                    os.path.abspath(rootPath)):
                    #print("Chemin invalide")
                    currentDir = ""
                    chemin = rootPath
                
                if os.path.isfile(currentDir + chemin):
                    files["files"] = files.get("", list()) + [
                        (currentDir + chemin).replace(rootPath, "")]
                
                elif os.path.exists(currentDir + chemin):
                    files[chemin] = os.listdir(currentDir + chemin)
        
        if joker:
            await ctx.message.author.dm_channel.send(
                "Les jokers ne sont pas supportés pour l'instant, ils sont donc ignorés")
        
        if files:
            await ctx.message.author.dm_channel.send(
                "\n\n".join([chemin.replace(rootPath, "/") + 
                             ":\n" + "\n".join(files[chemin])
                           for chemin in files]))
        
        else:
            await ctx.message.author.dm_channel.send(
                "No files/directories to list.")
