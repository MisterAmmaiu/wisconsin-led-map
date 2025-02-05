from PIL import Image
import os

### Global Variables ###

X_DIM, Y_DIM, = 10, 10 # Grid size (10x10 for 100 images)
IMAGE_WIDTH, IMAGE_HEIGHT = 1000, 1000 # Individual cell resolution
IMAGE_FOLDER = "output/"



### MAIN EXECUTION ###

# Create a new blank image with the combined size
combined_image = Image.new('RGB', (X_DIM * IMAGE_WIDTH, Y_DIM * IMAGE_HEIGHT))

# Paste all cells into image according to their coorindate
for y in range(Y_DIM):
    for x in range(X_DIM):
        img_path = IMAGE_FOLDER+f"{x}_{y}.png"
        img = Image.open(img_path)
        combined_image.paste(img, (x * IMAGE_WIDTH, y * IMAGE_HEIGHT))

# Save the final stitched image
combined_image.save('stitched_image.png')