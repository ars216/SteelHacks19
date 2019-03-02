import io
import os
from gtts import gTTS
import pygame
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
        
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)  

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\spap9\OneDrive\Documents\SteelHacks\AudibleImage.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'idiotest.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)
img = pygame.image.load('idiotest.jpg')

crop('idiotest.jpg', (0, 0, (img.get_width()/2), (img.get_height()/2)), 'croppedTL.jpg')
crop('idiotest.jpg', ((img.get_width()/2), 0, img.get_width(), (img.get_height()/2)), 'croppedTR.jpg')
crop('idiotest.jpg', (0, (img.get_height()/2), (img.get_width()/2), (img.get_height())), 'croppedBL.jpg')
crop('idiotest.jpg', ((img.get_width()/2), (img.get_height()/2), img.get_width(), img.get_height()), 'croppedBR.jpg')