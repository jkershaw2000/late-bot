from typing import DefaultDict
import asyncio
import configparser
import os.path

from discord.ext import commands
import texttable

import creds

config = configparser.ConfigParser()
if not os.path.exists("./stats.ini"):  
    with open("./stats.ini","w") as cfg:
        config.write(cfg)
config.read('./stats.ini')

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")
lateMessage = DefaultDict(bool)


@bot.command()
async def late(ctx, *args):
    global lateMessage
    print("late")
    for name in args:
        lateMessage[name] = True
        await ctx.send(f'{name} is running late...')
        if name not in config:
            config[name] = {"timesLate":int(1), "minsLate":int(0)}
        else:
            config[name]["timesLate"] = str(int(config[name]["timesLate"]) + 1)
            config[name]["minsLate"] = str(int(config[name]["minsLate"]) + 1)
    i = 1
    while True:
        count = 0
        await asyncio.sleep(5)
        for name in args:

            if lateMessage[name] == True:
                count += 1
                print(config[name]["minsLate"]  )
                config[name]["minsLate"] = str(int(config[name]["minsLate"]) + 1)
                await ctx.send(f'{name} is {i} minute(s) late...')
        if count == 0:
            break
        i += 1

@bot.command()
async def here(ctx, *args):
    global lateMessage
    print("Starting here")
    for name in args:
        if lateMessage[name]:
            await ctx.send(f"...And {name} is finally here!")
        lateMessage[name] = False
    with open("./stats.ini","w") as cfg:
        config.write(cfg)

@bot.command()
async def stats(ctx, *args):
    table = texttable.Texttable()
    table.add_row(["Name", "Times Late", "Minutes Late"])
    if len(args) == 0:
        for section in config.sections():
           table.add_row([section, config[section]["timesLate"], config[section]["minsLate"]]) 
    else:
        for name in args:
            if config.has_section(name):
                table.add_row([name, config[name]["timesLate"], config[name]["minsLate"]]) 
            else:
                table.add_row([name, 0, 0]) 

    await ctx.send(f"```{table.draw()}```")   

bot.run(creds.token)
