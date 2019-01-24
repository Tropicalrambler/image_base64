import os
import base64

imagename = 'turtle'
converted = 'converted'
imagextension = 'jpg'
filename = 'imagebase64'
filextension = 'txt'
dot = '.'
underscore = '_'
image_file_to_open = imagename + dot + imagextension
base64_file_to_save = filename + dot + filextension
image_file_to_save = converted + underscore + imagename + dot + imagextension
with open(image_file_to_open, "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    #print(str)

base64 = open(base64_file_to_save, "wb")
base64.write(str)
base64.close()
print('Image was converted to base 64 and saved in file: ' + base64_file_to_save)
