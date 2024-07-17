import random
from PIL import Image
import time

# Set the size of the image
width = 1000
height = 200

# Create a blank image with a white background
image = Image.new('RGB', (width, height), (255, 255, 255))

# Get the image's pixels as a 2D list
pixels = image.load()

# Set the starting and ending colors for the gradient
start_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
end_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Set the pixel colors for each pixel in the image using a color gradient
for i in range(width):
    # Calculate the color for this pixel using a linear gradient
    r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / width))
    g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / width))
    b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / width))
    color = (r, g, b)
    
    for j in range(height):
        pixels[i, j] = color

# Save the image to a file
image.save(f'gradient_{str(time.time()).replace(".", "")}.png')
