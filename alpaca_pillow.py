from PIL import Image, ImageDraw, ImageFont
import sys
import glob, os
import json
import random

#get json file with words
with open('moods.json') as json_data:
    d = json.load(json_data)

#get the folder with images
os.chdir("images/")

def drawtext():
	for image in glob.glob("*.jpg"):
		print image

		im = Image.open(image)

		#pick random mood from the json file
		text = random.choice(d['moods'])

		#draw onto the image
		canvas = ImageDraw.Draw(im)
		fnt = ImageFont.truetype('/Users/rutakruliauskaite/Library/Fonts/LibreBaskerville-Bold.otf', 70)
		canvas.text((50, 170), text, font=fnt, fill=(255, 255, 255))

		# #choose a new directory
		# os.chdir("new_images/")

		#save
		im.save(image + '_pillowed.png')

drawtext()