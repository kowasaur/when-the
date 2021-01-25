from utility import phraseInMessage, replace, search
from constants import ID, PASSWORD, PHRASES, SECRET, USERNAME
import praw

reddit = praw.Reddit(
  client_id = ID,
  client_secret = SECRET,
  user_agent ='<console:when-the:1.0.0>',
  username = USERNAME,
  password = PASSWORD
)

subreddit = reddit.subreddit('all')

def doFunne(post, phrase):
  print('poggers')
  print(submission.permalink)
  quote = search(post, phrase)
  highlightedQuote = replace(quote, phrase, f'*{phrase}*')
  print(highlightedQuote)

print('connected')
for submission in subreddit.stream.submissions():
  # funne in post title
  post = submission.title
  phrase = phraseInMessage(PHRASES, post)
  if phrase != 'none':
    doFunne(post, phrase)
  # funne in post body
  else:
    post = submission.selftext
    if hasattr(submission, "selftext"):
      phrase = phraseInMessage(PHRASES, post)
      if phrase != 'none':
        doFunne(post, phrase)
  
  # ! I realised that this will not get any new comments
  # * maybe look into this https://stackoverflow.com/questions/18864859/python-executing-multiple-functions-simultaneously
  # funne in comments
  # for comment in submission.comments:
  #   if hasattr(comment, "body"):
  #     phrase = phraseInMessage(PHRASES, comment.body)
  #     if phrase != 'none':
  #       print('poggers')
  #       print(comment.permalink)
