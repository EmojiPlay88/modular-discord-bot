import sys
import os
import discord

def checkPermissions(user:discord.Member, perms:list):
    for role in user.roles:
        if str(role.id) in perms:
            return True
    return False