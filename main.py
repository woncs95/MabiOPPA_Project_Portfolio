import server
import discord
import os
import keep_alive


client = discord.Client()

##server received => chat room
  #if server.receive_message():
    #await message.channel.send()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))
