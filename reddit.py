from utility import phraseInMessage, randomListElement, replace, search
from constants import ID, PASSWORD, PHRASES, SECRET, SUSES, USERNAME
import praw
from prawcore.exceptions import PrawcoreException
from time import sleep

reddit = praw.Reddit(
  client_id = ID,
  client_secret = SECRET,
  user_agent ='<console:when-the:1.0.0>',
  username = USERNAME,
  password = PASSWORD
)

ME = reddit.user.me()

subreddit = reddit.subreddit('all')

submissionStream = subreddit.stream.submissions(pause_after=-1)
commentStream = subreddit.stream.comments(pause_after=-1)

def doFunne(post, submission):
  phrase = phraseInMessage(PHRASES, post)
  if phrase != 'none':
    quote = search(post, phrase)
    highlightedQuote = replace(quote, phrase, f'*{phrase}*')
    
    sus = randomListElement(SUSES, [4])
    submission.reply(f'> {highlightedQuote}\n```{sus}```')
    print(submission.permalink)
    return True
  else:
    return False

def main():
  print('connected')
  while True:
    for submission in submissionStream:
      # Switch to comments
      if submission is None:
        break
      # check if replying to self
      if ME == getattr(submission.author, 'name', None):
        continue

      # funne in post title
      post = submission.title
      
      # funne in post body
      if doFunne(post, submission) == False and hasattr(submission, "selftext"):
        post = submission.selftext
        doFunne(post, submission)

    for comment in commentStream:
      # Switch to submissions
      if comment is None:
        break

      # check if replying to self
      if ME == getattr(comment.author, 'name', None):
        continue

      post = comment.body
      doFunne(post, comment)

def handleException(error):
  print(error)
  sleep(15 * 60)
  print('Sleeping for 15 minutes')
  main()

try:
  main()
except PrawcoreException as e:
  handleException()
except praw.exceptions.PRAWException as e:
  handleException()
except praw.exceptions.ClientException as e:
  handleException()
except praw.exceptions.APIException as e:
  handleException()
except KeyboardInterrupt:
  print('manually ended')
except Exception as e:
  print(e)
