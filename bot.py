import discord
from utility import phraseInMessage, randomListElement, search, replace
from constants import PHRASES, SUSES, TOKEN
import random

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user.name} discord is logged in to')

@client.event
async def on_message(msg):
  # So there's no infinite loops
  if msg.author == client.user:
    return

  message = msg.content
  phrase = phraseInMessage(PHRASES, message, includePartial=True)
  if phrase == 'none':
    return

  quote = search(message, phrase)
  highlightedQuote = replace(quote, phrase, f'*{phrase}*')

  if random.randint(0, 1) == 1:
    sus = randomListElement(SUSES, [4])
    await msg.reply(f'> {highlightedQuote}\n```{sus}```')
  else:
    await msg.reply('> ' + highlightedQuote, file=discord.File('sus.jpg'))

client.run(TOKEN)
