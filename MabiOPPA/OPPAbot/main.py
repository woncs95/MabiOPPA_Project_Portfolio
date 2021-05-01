import discord
import os
import keep_alive
from dotenv import load_dotenv
from discord.ext import commands
from threading import Thread
import SocketServer

client = discord.Client()


##emoji_db
healing=" <:Healing:832601159084015696> "



##send message from socketserver to discord ##mch=selected channel
async def show_message(mch):
  while True:
    data=SocketServer.receive_message()
    if data != False:
      await mch.send(data)


##standby
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg=message.content
  channel=message.channel

  if msg.startswith('$help'):
    embed = discord.Embed(
      title='OPPABot Commands',
      description='These are Commands for OPPABot',
      colour=discord.Colour.orange()
    )
    embed.add_field(name='$setannounce', value='set this Textchannel as'
                                               ' an announcement channel '
                                               'for reports', inline=True)
    await channel.send(embed=embed)

  if msg.startswith('$hello'):
    await channel.send(healing)


  if msg.startswith('$setannounce'):
    mch = channel  ##speicher
    embed = discord.Embed(
      title='',
      description='This channel is set as an announcement channel',
      colour=discord.Colour.orange()
    )
    await mch.send(embed=embed)
    await show_message(mch)



#load_dotenv('.env')
keep_alive.keep_alive()
client.run('ODI0Njg5Mzg5MjY2NTM0NDEx.YFzB2A.4799gnltRw31iUBwcdo08bRQVWc')
Thread(target = SocketServer.receive_message()).start()