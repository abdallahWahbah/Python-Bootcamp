"""
# npm install pillow
pillow is a fork from PIL, so we import Image from PIL not pillow
"""

from PIL import Image

oldMacintosh = Image.open('./images/example.jpg')

# oldMacintosh.show() # opens the pictures application as if you are browsing your pc and opening a random image
print(oldMacintosh.size, oldMacintosh.filename, oldMacintosh.format_description) # (1993, 1257) C:\Users\abdow\OneDrive\Desktop\My Python stuff\14-images-pillow\images\example.jpg JPEG (ISO 10918)


## crop

pencils = Image.open('images/pencils.jpg')
pencilsWidth, pencilsHeight = pencils.size

x = 0
y = 0
width = pencilsWidth / 3
height = pencilsHeight / 10
pencils.crop((x, y, width, height)).show() # think of (x, y) as starting point >>> (width, height) as end point (in x, y coordinates)


## copy, resize, rotate, save
## copy pincels and put the image on the top left of macintosh image
croppedPincels = pencils.crop((0, 0, pencilsWidth / 3, pencilsHeight)).resize((300, 300)).rotate(90)
oldMacintosh.paste(im=croppedPincels, box=(0, 0))
oldMacintosh.show()

oldMacintosh.save('mixed_image.jpg') # new image name




######## Exercise (masking, changing opacity, pasting, resizing)

words = Image.open('images/word_matrix.png')
mask = Image.open("images/mask.png")
wordsWidth, wordsHeight = words.size
mask = mask.resize((wordsWidth, wordsHeight))
mask.putalpha(200) # opacity for mask (rgb(a))
words.paste(mask,(0,0),mask)
words.show()