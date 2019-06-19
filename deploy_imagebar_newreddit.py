"""Crop the images in the imagebar directory and add text"""

import json
import os
import textwrap

from PIL import Image, ImageDraw, ImageFont
import praw

# Load bot, expected to be simple json dict
#with open('bot_deets.json') as f:
#    bot_deets = json.load(f)
#subreddit = praw.Reddit(**bot_deets).subreddit(target_sub)

input_dir = 'assets/imagebar/'
output_dir = 'assets/imagebar/edited_for_newreddit'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
fnames = [f for f in os.listdir(input_dir) if f.endswith('.jpg')]
input_fnames = [os.path.join(input_dir, fname) for fname in fnames]
output_fnames = [os.path.join(output_dir, fname) for fname in fnames]

wrap_length = 30
x = 25 # padding-left
y = 8 # padding-top
font_size = 26
fill_color = 'white'
shadow_color = 'black'
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', font_size)

for input_fname, output_fname in zip(input_fnames, output_fnames):
    text = input(f'Enter the text for {input_fname}:\n')
    wrapped_text = textwrap.fill(text, wrap_length)

    img = Image.open(input_fname).crop((0, 0, 600, 112))
    draw = ImageDraw.Draw(img)
    # Shadow
    draw.text((x-2, y), wrapped_text, font=font, fill=shadow_color)
    draw.text((x+2, y), wrapped_text, font=font, fill=shadow_color)
    draw.text((x, y-2), wrapped_text, font=font, fill=shadow_color)
    draw.text((x, y+2), wrapped_text, font=font, fill=shadow_color)
    draw.text((x-2, y-2), wrapped_text, font=font, fill=shadow_color)
    draw.text((x+2, y-2), wrapped_text, font=font, fill=shadow_color)
    draw.text((x-2, y+2), wrapped_text, font=font, fill=shadow_color)
    draw.text((x+2, y+2), wrapped_text, font=font, fill=shadow_color)
    # Main wrapped_text
    draw.text((x, y), wrapped_text, font=font, fill=fill_color)

    img.save(output_fname)
