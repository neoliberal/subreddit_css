from PIL import Image, ImageDraw, ImageFont

fname = "imagebar/zhao_ziyang_colorized.jpg"
fname_new = "imagebar/zhao_ziyang_colorized_processed.jpg"
text = "China's Forgotten Reformer"

padding_left = 10
padding_top = 8
font_size = 28
fill_color = 'white'
shadow_color = 'black'

img = Image.open(fname)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
draw = ImageDraw.Draw(img)

# Shadow
draw.text((x-1, y), text, font=font, fill=shadow_color)
draw.text((x+1, y), text, font=font, fill=shadow_color)
draw.text((x, y-1), text, font=font, fill=shadow_color)
draw.text((x, y+1), text, font=font, fill=shadow_color)
draw.text((x-1, y-1), text, font=font, fill=shadow_color)
draw.text((x+1, y-1), text, font=font, fill=shadow_color)
draw.text((x-1, y+1), text, font=font, fill=shadow_color)
draw.text((x+1, y+1), text, font=font, fill=shadow_color)

# Main text
draw.text((x, y), text, font=font, fill=fillcolor)

img.crop((0, 0, 600, 112))
img.save(fname_new)
