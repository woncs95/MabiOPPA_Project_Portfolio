import discord
from discord.ext import commands,tasks
import os, sys
from os import system
from dotenv import load_dotenv
from threading import Thread
import SocketServer
import emojiset
import time
import asyncio

command_prefix='!'
bot = commands.Bot(command_prefix= command_prefix, description='{0.user}',help_command=None)
report_channel={'run_counter':'','recruitment':'','roster':''} ##init dic
run_count = report_channel['run_counter']


@bot.command()
async def get_txtchannels(ctx):
    text_channel_dic={}
    if len(list(text_channel_dic.keys()))==0:
        for channel in ctx.message.guild.channels:
            if str(channel.type)=="text":
                text_channel_dic[channel.name]=channel
        return text_channel_dic
    else:
        return text_channel_dic


@bot.command()
async def hello(ctx):
    await ctx.send(emojiset.healing)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title='OPPABot Commands', description='These are Commands for OPPABot', colour=discord.Colour.orange())
    embed.add_field(name=f'{command_prefix}set', value='set this Textchannel as an announcement channel for reports', inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def setcounter(ctx, *, text_channel):
    text_channel_dic= await get_txtchannels(ctx)
    if text_channel in list(text_channel_dic.keys()):
    #if ctx.user == ctx.guild.owner: ##Definition ctx user??
        embed = discord.Embed(title=None, description=f'Run Counter is set in {text_channel}',colour=discord.Colour.orange())
        await ctx.send(embed=embed)
        report_channel['run_counter'] = text_channel_dic[text_channel]
        run_counter=report_channel['run_counter']
        embed = discord.Embed(title=None, description=f'This channel is set as Run Counter',colour=discord.Colour.orange())
        await run_counter.send(embed=embed)
    else:
        embed = discord.Embed(title='', description='You gave a wrong channel name. Try again.', colour=discord.Colour.orange())
        await ctx.send(embed=embed)
        pass


@bot.command()
async def setrecruitment(ctx, *, text_channel):
    text_channel_dic = await get_txtchannels(ctx)
    if text_channel in list(text_channel_dic.keys()):
        embed = discord.Embed(title='', description=f'Recruitment is set in {text_channel}',colour=discord.Colour.orange())
        await ctx.send(embed=embed)
        report_channel['recruitment'] = text_channel_dic[text_channel]
    else:
        embed = discord.Embed(title='', description='You gave a wrong channel name. Try again.', colour=discord.Colour.orange())
        await ctx.send(embed=embed)
        pass


@bot.command()
async def setroster(ctx, *, text_channel):
    text_channel_dic = await get_txtchannels(ctx)
    if text_channel in list(text_channel_dic.keys()):
        report_channel['roster'] = text_channel_dic[text_channel]
        embed = discord.Embed(title='', description=f'Roster Maker is set in {text_channel}', colour=discord.Colour.orange())
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title='', description='You gave a wrong channel name. Try again.', colour=discord.Colour.orange())
        await ctx.send(embed=embed)
        pass

##standby-------
@bot.event
async def on_ready():
    show_message.start()
    print('We have logged in as {0.user}'.format(bot))

#Loop listening the messages the whole time-------------------------------
@tasks.loop(seconds=0.2)
async def show_message():

    if report_channel['run_counter']=='':
        print('no channel for message')

    #if report_channel['run_counter']=='' and result!=False:
        #run_count = report_channel['run_counter'] ##send a dm to a user that he needs to define a run counter

    else:
        result = SocketServer.receive_message()
        print("server received message"+time.ctime(time.time()))
        if result:
            await report_channel['run_counter'].send(result)
            print("sent runcounter in discord time" + time.ctime(time.time()))

#Loop listening the messages the whole time-----------------------------


bot.run('ODI0Njg5Mzg5MjY2NTM0NDEx.YFzB2A.sPox0gW2pkh_3L7Rsn73cQRiJJQ')