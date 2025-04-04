import discord

def checkPermissions(user:discord.Member, permissions:li>
    roles = user.roles
    for role in roles:
        if role.permissions.value & permissions:
            return True
    return False
