import os
import base64

imagename = 'converted_turtle'
imagextension = 'jpg'
filename = 'imagebase64'
filextension = 'txt'
dot = '.'
image_file_to_save = imagename + dot + imagextension
base64_file_to_open = filename + dot + filextension
# Open the file containing image as base64
with open(base64_file_to_open, "rb") as base64imageFile:
    decoded_str = base64imageFile.read()
    #print(str)

new_image = open(image_file_to_save, "wb")
new_image.write(base64.b64decode(decoded_str))
new_image.close()
print('Image was converted from base 64 and saved in file: ' + image_file_to_save)