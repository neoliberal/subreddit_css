import json
import glob
import os

from PIL import Image
import praw


# Load bot
with open('bot_deets.json') as f:
    bot_deets = json.load(f)
wumbotarian = praw.Reddit(**bot_deets).subreddit('wumbotarian')

# Get flairs from assets/flairs directory
subreddit_css_directory = os.path.dirname(os.path.realpath(__file__))
flair_directory = os.path.join(subreddit_css_directory, 'assets/flairs')
flair_filenames = glob.glob(flair_directory + '/**/_*.png')
flair_names = [
    os.path.basename(flair)[1:-4]
    for flair 
    in flair_filenames
]

#Safety checks -- no duplicate names, correct size
duplicates = list(set([x for x in flair_names if flair_names.count(x) > 1]))
if duplicates:
    raise Exception('Duplicate flair name(s): {}'.format(duplicates))
for flair_filename in flair_filenames:
    img = Image.open(flair_filename)
    if img.size[0] > 128 or img.size[1] > 128:
        raise Exception('{} is too big (>128x128)'.format(flair_filename))

# Add any missing emojis
subreddit_emojis = [emoji.name for emoji in wumbotarian.emoji]
for idx, flair in enumerate(flair_names):
    if flair not in subreddit_emojis:
        print('adding {}'.format(flair))

# add emojis to userflairs
for flair in wumbotarian.flair():
    user = flair['user'].name
    flair_css = flair['flair_css_class']
    flair_text = flair['flair_text']
    if flair_css is not None:
        # Identify image in user flair css
        for flair_name in flair_names:
            if flair_name+' ' in flair_css:
                flair_image = flair_name
        emojus = ':'+flair_image+':'
        if emojus not in flair_text:
            print('Adding emoji to {}'.format(user))
            wumbotarian.flair.update([user], emojus+' '+flair_text, flair_css)
