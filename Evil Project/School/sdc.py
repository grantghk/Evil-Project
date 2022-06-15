import webbrowser
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="$", cas_insentive=True, help_command=None)
@bot.command()
async def play1(ctx):
        webbrowser.open('https://www.youtube.com/watch?v=rzTMS2xxLnQ')
        ctx.send("Play Track 1") 
@bot.command()
async def play2(ctx):
    webbrowser.open('https://www.youtube.com/watch?v=7Izwbh2fLn4')
    ctx.send("Play Track 2") 
@bot.command()
async def play3(ctx):
    webbrowser.open('https://www.youtube.com/watch?v=RQtPTSdWgH8')
    ctx.send("Play Track 3")       
bot.run('OTg2NjE1MDU4NTAxMDc0OTU0.GERvHO.gkh6UYCF6Kv7Cm1lsdZyXjzIQAQmBwntvtF2I8')