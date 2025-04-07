import sys
import os
import discord

sys.path.append(os.path.abspath("../core"))
from core.configHandler import Config

config_path = os.path.abspath("./configs/main.cfg")
mainConfig = Config(config_path).returnConfig()

def checkPermissions(user:discord.Member):
    permsAvailable = False
    for role in user.roles:
        print(mainConfig['PERMISSIONS'].get(['setLanguagePerms']))
        if role.id in int(mainConfig['PERMISSIONS'].get(['setLanguagePerms'])):
            permsAvailable = True
    return permsAvailable