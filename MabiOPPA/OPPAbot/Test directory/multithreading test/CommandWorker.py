from discord.ext import commands
from threading import Thread
from ServerWorker import receive_message
import emojiset_t

# MabiOPPA="<Guild id=813416177861656596 name='MabiOPPA' shard_id=None chunked=False member_count=8>"


class myThread(Thread, commands.Bot):
   def __init__(self, threadID, name):
       Thread.__init__(self)
       self.threadID = threadID
       self.name = name


   def run(self):
       print('starting '+self.name)
       while True:
           data = receive_message()
           if data is not False:
               print('data is'+data)
               # channel = MabiOPPA
               # channel.send(data)


command_prefix='!'
token=''
bot = commands.Bot(command_prefix=command_prefix, description='{0.user}', help_command=None)


@bot.command()
async def hello(ctx):
    await ctx.send(emojiset_t.healing)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


thread1 = myThread(1, 'Server-Thread')
thread1.start()
bot.run(token)




