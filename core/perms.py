import sys
import os
import discord

sys.path.append(os.path.abspath("../core"))
from core.configHandler import Config

mainConfig = Config('./configs/main.cfg').returnConfig()

def checkPermissions(user:discord.Member):
    permsAvailable = False
    for role in user.roles:
        if role.id in mainConfig['PERMISSIONS']['setLanguagePerms']:
            permsAvailable = True
    return permsAvailable