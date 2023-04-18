import discord
import random 
import asyncio
import re

class MyClient(discord.Client):

  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    # don't respond to ourselves
    if message.author == self.user:
      return

    # responses
    if re.search("^ping.*", message.content):
      await message.channel.send('pong')
    elif re.search("^pong.*", message.content):
        await message.channel.send('ping')  
    elif re.search("^(!!!){1}", message.content):
        await message.channel.send('so exciting! XD')
    elif re.search("^[Bb]eep.*", message.content):
      await message.channel.send("boop")
    elif re.search("^[Bb]oop ?.*", message.content):
      await message.channel.send('beep')
    elif re.search("^[Bb]ing.*", message.content):
      await message.channel.send("bong")
    elif re.search("^[Bb]ong ?.*", message.content):
      await message.channel.send('bing')
    elif re.search("^[Dd]ing.*", message.content):
      await message.channel.send("dong")
    elif re.search("^[Dd]ong ?.*", message.content):
      await message.channel.send('ding')

    if re.search("^[Hh]i ?.*", message.content):
      await message.channel.send('hello, friend!')
    elif re.search("^[Hh]ello ?.*", message.content):
        await message.channel.send('hey, friend!')
    elif re.search("^[Hh]ey ?.*", message.content):
        await message.channel.send('hi, friend!')
    elif re.search("^[Ww]hat\'s poppin ?.*", message.content):
        await message.channel.send('my boomchikapop sweet & salty kettle corn!')
    
    if re.search(" ?:\( ?.*", message.content):
      await message.channel.send("hugs*")
    elif re.search(" ?:\) ?.*", message.content):
      await message.channel.send("smiles! :)")  
    
    # guess number game  
    if message.content.startswith('$guess'):
      await message.channel.send('guess a number between 1 and 10')

      def is_correct(m):
          return m.author == message.author and m.content.isdigit()

      answer = random.randint(1, 10)

      try:
          guess = await self.wait_for('message', check=is_correct, timeout=5.0)
      except asyncio.TimeoutError:
          return await message.channel.send(f'sorry, you took too long it was {answer}')

      if int(guess.content) == answer:
          await message.channel.send('you are right! :D')
      else:
          await message.channel.send(f'oops it is actually {answer} :(')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
token = str(open("token.txt").read())
client.run(token)
