"""
Created on 30 avr. 2022

@author: Thomas
"""
import discord.ext.commands as DC

class Command_mkdir(DC.Command):
    options = {
        "-p": False}
    def __init__(self, params):
        super().__init__(self.mkdir)
        self.name = "mkdir"
        self.brief = "Permet de créer un ou plusieurs dossiers"
        self.usage = "[OPTION...] <Dossier>"
        self.help = ("Crée un ou plusieurs dossiers\nL'option p permet de créer " +
                     "toute arborescence nécessaire")
        
        