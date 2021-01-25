from logging import log
import re
import random

# https://stackoverflow.com/a/5833319/13837629
def search(text, phrase):
  '''Searches text for phrase and returns the phrase plus the two words on each side'''
  result = re.search(r'(?:\S+\s+){0,2}\S*' + phrase + r'\S*(?:\s+\S+){0,2}', text, flags=re.MULTILINE)
  return result.group()

def replace(text, replacee, replacer):
  return re.sub(replacee, replacer, text)

def phraseInMessage(listOfPhrases, message):
  for phrase in listOfPhrases:
    if phrase in message:
      return phrase
  return 'none'

# https://stackoverflow.com/a/3679747/13837629
def _weighted_choice(choices):
   total = sum(w for _, w in choices)
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices:
      if upto + w >= r:
         return c
      upto += w
   assert False, "Shouldn't get here"

def randomListElement(li, weights=[]):
  '''this can be weighted as well. Default weight is 1'''
  combinedList = []
  for i in range(0, len(li)):
    try:
      weight = weights[i]
    except:
      weight = 1
    combinedList.append((li[i], weight))
  return _weighted_choice(combinedList)

