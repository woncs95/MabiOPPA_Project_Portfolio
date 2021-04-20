import discord
import os
import keep_alive
from dotenv import load_dotenv
import NewServer

client = discord.Client()


##emoji_db
healing=" <:Healing:832601159084015696> "





@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send(healing)

@client.event
async def receive_message():
  await NewServer.receive_message()
  if NewServer.receive_message() != "":
    await receive_message.channel.send(NewServer.receive_message())


load_dotenv('.env')
print(os.getenv('TOKEN'))
keep_alive.keep_alive()
client.run(os.getenv('TOKEN'))
