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
import pprint
import pandas as pd
from openpyxl import load_workbook
from GuildData import GuildData as guild_data

command_prefix='!'
bot = commands.Bot(command_prefix= command_prefix, description='{0.user}',help_command=None)
#guild_id={'Magus':'758433284131782656','MabiOPPA':'813416177861656596','SukjaTest':'844890188341051424'}
#MabiOPPA="<Guild id=813416177861656596 name='MabiOPPA' shard_id=None chunked=False member_count=8>"
#SukjaTest="<Guild id=844890188341051424 name='Sukja Test' shard_id=None chunked=False member_count=2>"

#report_channel1={'run_counter':'','recruitment':'','roster':''}
#report_channel2={'run_counter':'','recruitment':'','roster':''}
#report_channel3={'run_counter':'','recruitment':'','roster':''}     ##init dic
report_channel={'run_counter':'','recruitment':'','roster':''} ##init dic
run_count = report_channel['run_counter']
#text_channel_dic = {}

guild_data = {}
run_result = {'guild':'','author':'','channel':''}

command_datas = {'organization':'','RunCounter_channel_id':'','RunCounter_channel_name':'','RunCounter_command_enter':False,'RosterMaker_channel_id':'','RosterMaker_channel_name':'','RosterMaker_command_enter':False,'RaidCalendar_channel_id':'','RaidCalendar_channel_name':'','RaidCalendar_command_enter':False}

 #get data from runresult

@bot.command()
async def setDataSetCounter(ctx):
    # guild_data.guild_name = ctx.message.guild.name
    # guild_data.rco_channel_id = ctx.message.channel.id
    # guild_data.rco_channel_name = ctx.message.channel.name
    # guild_data.rco_command_enter = True

    command_datas['organization'] = ctx.message.guild.name
    command_datas['RunCounter_channel_id'] = ctx.message.channel.id
    command_datas['RunCounter_channel_name'] = ctx.message.channel.name
    command_datas['RunCounter_command_enter'] = True
    df1=pd.DataFrame(command_datas, index=[ctx.message.guild.id])
    df1.to_excel('test.xlsx')

@bot.command()
async def getDataSetRecruitment(ctx):
    guild_data.guild_name = ctx.message.guild.name
    guild_data.rca_channel_id = ctx.message.channel.id
    guild_data.rca_channel_name = ctx.message.channel.name
    guild_data.rca_command_enter = True

    # command_datas['organization'] = ctx.message.guild.name
    # command_datas['RaidCalendar_channel_id'] = ctx.message.channel.id
    # command_datas['RaidCalendar_channel_name'] = ctx.message.channel.name
    # command_datas['RaidCalendar_command_enter'] = True
@bot.command()
async def getDataSetRoster(ctx):
    guild_data.guild_name = ctx.message.guild.name
    guild_data.rm_channel_id = ctx.message.channel.id
    guild_data.rm_channel_name = ctx.message.channel.name
    guild_data.rm_command_enter = True
    # command_datas['organization'] = ctx.message.guild.name
    # command_datas['RosterMaker_channel_id'] = ctx.message.channel.id
    # command_datas['RosterMaker_channel_name'] = ctx.message.channel.name
    # command_datas['RosterMaker_command_enter'] = True

@bot.command()
async def hello(ctx):
    await ctx.send(emojiset.healing)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title='OPPABot Commands', description='These are Commands for OPPABot', colour=discord.Colour.orange())
    embed.add_field(name=f'{command_prefix}set', value='set this Textchannel as an announcement channel for reports', inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def setcounter(ctx, *, text_channel):
    guild = ctx.message.guild

    guild_txtchannel = await setDataSetCounter(ctx)
    #print(guild_txtchannel.index(0))
    text_channel_dic = guild_txtchannel[str(guild.name)]

    if text_channel in list(text_channel_dic.keys()):
    #if ctx.user == ctx.guild.owner: ##Definition ctx user??
        embed = discord.Embed(title='', description=f'Run Counter is set in {text_channel}',colour=discord.Colour.orange())
        await ctx.send(embed=embed)
        report_channel['run_counter'] = text_channel_dic[text_channel]
        run_counter = report_channel['run_counter']
        print(run_counter)
        # guild_report[guild.name] = report_channel
        # df = pd.DataFrame(guild_report)
        # df.to_excel('guild report.xlsx')
        embed = discord.Embed(title='', description=f'This channel is set as Run Counter',colour=discord.Colour.orange())
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
    # #if report_channel['run_counter']==''
    # #if report_channel['run_counter']=='' and result!=False:
    #     #run_count = report_channel['run_counter'] ##send a dm to a user that he needs to define a run counter
    #
    # #else:
    # result = SocketServer.receive_message()
    # print("server received message"+time.ctime(time.time()))
    # result = result.split('.') ##result is a list [type(runcounter,roster,recruitment),guildname,report]
    # guild_data=load_workbook('guild_data.xlsx')
    # if result[0] == "run_counter":
    #     report_guild = guild_data[result[1]]
    #     report_channel = guild_report[result[1]][result[0]]
    #     await report_guild.report_channel.send(result[2])
    #     print("sent runcounter in discord time" + time.ctime(time.time()))
    if report_channel['run_counter']=='':
        pass#print('no channel for message')

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