import discord
from utility import phraseInMessage, randomListElement, search, replace
from constants import PHRASES, SUSES, TOKEN

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
  phrase = phraseInMessage(PHRASES, message)
  if phrase == 'none':
    return

  quote = search(message, phrase)
  highlightedQuote = replace(quote, phrase, f'*{phrase}*')

  sus = randomListElement(SUSES, [4])

  await msg.reply(f'> {highlightedQuote}{sus}')

client.run(TOKEN)
