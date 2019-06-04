import json
import glob
import os

from PIL import Image
import praw


prompt = """
Which sub would you like to deploy to?

1 - wumbotarian
2 - neoliberal

"""

# Prompt for target sub (wumbotarian or neoliberal)
target_sub = None
while target_sub is None:
    sub_indicator = input(prompt)
    if sub_indicator == '1':
        target_sub = 'wumbotarian'
    elif sub_indicator == '2':
        target_sub = 'neoliberal'

# Load bot, expected to be simple json dict
with open('bot_deets.json') as f:
    bot_deets = json.load(f)
subreddit = praw.Reddit(**bot_deets).subreddit(target_sub)

# Get flairs from assets/flairs directory
subreddit_css_directory = os.path.dirname(os.path.realpath(__file__))
flair_directory = os.path.join(subreddit_css_directory, 'assets/flairs')
flair_filenames = glob.glob(flair_directory + '/**/_*.png')
flair_names = [os.path.basename(flair)[1:-4] for flair in flair_filenames]

#Safety checks -- no duplicate names, correct size
duplicates = list(set([x for x in flair_names if flair_names.count(x) > 1]))
if duplicates:
    raise Exception('Duplicate flair name(s): {}'.format(duplicates))
for flair_filename in flair_filenames:
    img = Image.open(flair_filename)
    if img.size[0] > 128 or img.size[1] > 128:
        raise Exception('{} is too big (>128x128)'.format(flair_filename))

# Add any missing emojis
subreddit_emojis = [emoji.name for emoji in subreddit.emoji]
for idx, flair in enumerate(flair_names):
    if flair not in subreddit_emojis:
        print('adding {}'.format(flair))
