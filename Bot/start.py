'''
Created on 03.11.2016

@author: Rikinya
'''
import discord
from discord.ext import commands
import asyncio
from discord.member import Member
import time
from pickle import APPEND

description = '''
'''
bot = commands.Bot(command_prefix='!', description=None)


    
@bot.event
async def on_member_update(after,member):
    server = member.server
    devserver = '112949095601094656'
    dev = '207351149521534976'
    memberserver = server.id
    if memberserver == devserver:
        def check_list(m):
            return m.content.startswith(member.mention)
        deleted = await bot.purge_from(channel=discord.Object(id=dev), limit=100, check=check_list)
        print('Deleted {} message(s)'.format(len(deleted)))
        try:
            if member.game.type == 1:
                y = str(member.game)
                z = str(member.game.url)
                await bot.send_message(destination=discord.Object(id=dev), content=' {0} is now live!\n```css\n{2}\n``` \n{1}'.format(member.mention,z,y))
                print('sent message')
                print(z) 
        except Exception:
            return
                
            
            
    pass
@bot.group(pass_context=True)
async def stream(ctx):
    if ctx.invoked_subcommand is None:
        inv_text = '''
Invalid subargument passed, try:\n
```css\n
!stream {subargument}
[help]        -    How can my Stream be posted.\n
[enable]      -    Currently not in use\n
[disable]     -    Currently not in use\n
[suggestions]\n
```
'''
        await bot.say(inv_text)
    
@stream.command()
async def help():
    stream_help ='''
```In order to have your stream link automatically posted whenever you go online, you need to have your discord (on PC) connected to your Twitch account.\n
The Option [Enable Streamer Mode] has to be enabled as well.\n
```\n
If you need help, please contact {0}
'''
    kek = (await bot.application_info()).owner
    await bot.say(stream_help.format(kek.mention))
    
@stream.command()   
async def enable():
    await bot.say('not implemented - maybe future feature')
@stream.command()
async def disable():
    await bot.say('not implemented - maybe future feature')
@stream.command()
async def suggestions():
    stream_suggestions = '''
You can state your suggestions by writing this user {0}
'''
    kek = (await bot.application_info()).owner
    await bot.say(stream_suggestions.format(kek.mention))        
    
    
@bot.command(hidden=True,pass_context=True)
async def info(self):
    await bot.say("I'm a useless bot")
    xyc = '{0.test}'
    
@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user)) 
    statusname = 'with my Owner'
    await bot.change_presence(game=discord.Game(name=statusname))
    print('Status: ' +statusname)  
    
bot.run('MjA3MzE0MjI0MTY1Mjg5OTg1.CnlE9g.f_VeCJDNr_d8xXHdpNrH1QrURUQ')