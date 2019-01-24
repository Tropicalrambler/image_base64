# image_base64
Example Source and Destination scripts for converting images to base64 and back again

## Usage
Run the first script from the terminal with:
`python imgtobase64.py`

You will get the message:

Image was converted to base 64 and saved in file: imagebase64.txt

The file now contains the image in base64 format (a string of text) which you can encode or send as an argument with web methods.

To decode and save a new image from the base 64 format contained in the plain text file, run the second script from the terminal with:
`python base64toimg.py`

You will get the message:

Image was converted from base 64 and saved in file: converted_turtle.jpg

Open the image and you will see an exact copy of the original image.

Before running again, delete both the imagebase64.txt file and the converted_turtle.jpg file.

## Further learning

Try changing the image in the folder.
Modify the filename variable in the source and destination python files.
