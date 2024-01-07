from PIL import Image
import os

folder_path = r"folder/where/your/spritesheets/are"
output_folder_path = folder_path + r"/output/folder/path"
ICON_WIDTH = 148
ICON_HEIGHT = 125

# This is an optional setting used to determine how far up and down you should scan for the 
# leftmost edge of a sprite from the top of the image. In addition to improving performace, 
# it also helps prevent you from running into any other sprites further down the sheet. 
# I usually set it equal to the size of each "row" on my spritesheets. 
use_scan_height = True
SCAN_HEIGHT = 64

def crop_all_files():
    
        for filename in os.listdir(folder_path):
            try:
                # Load the image
                image = Image.open(folder_path + "\\" + filename).convert('RGBA')

                # Find the first non-transparent pixel in the top left
                top = find_top_non_transparent_pixel(image)
                left = find_left_non_transparent_pixel(image, top[0])
                if top is None or left is None:
                    print('No non-transparent pixels found in the image.')
                else:
                    # Find the borders of the non-transparent object
                    top_left = (left[0], top[1])
                    borders = find_object_borders(image, top_left)

                    # Create a separate image with the non-transparent object
                    object_image = resize_canvas(create_object_image(image, borders))
                    new_name = output_folder_path + filename
                    object_image.save(new_name)
                    print('Object image saved as ', new_name)

            except Exception as e: 
                print("FAILED to get icon for " + filename + ". Error: " + str(e))

def find_top_non_transparent_pixel(image):
    width, height = image.size
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            if pixel[3] != 0:  # Check if alpha channel is not transparent
                return x, y
    print("Could not find top transparent pixel.")
    return None

def find_left_non_transparent_pixel(image, highest_x_value):
    width, height = image.size
    if use_scan_height :
        height = SCAN_HEIGHT
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel[3] != 0:  # Check if alpha channel is not transparent
                return x, y
    print("Could not find leftmost transparent pixel.")
    return None

def find_object_borders(image, top_left): 

    width, height = image.size
    left, top = top_left
    right, bottom = top_left
    
    for y in range(top, height):
        transparent = True
        for x in range(width):
            pixel = image.getpixel((x, y))
            if pixel[3] != 0:  # Check the alpha channel value
                transparent = False
                break

        if transparent:
            bottom = y
            break

    for x in range(left + 1, width):
        transparent = True
        for y in range(top, bottom):
            pixel = image.getpixel((x, y))
            if pixel[3] != 0:  # Check the alpha channel value
                transparent = False
                break

        if transparent:
            right = x
            break

    return left, top, right, bottom

def create_object_image(image, borders):
    left, top, right, bottom = borders
    object_image = image.crop((left, top, right, bottom))
    return object_image

def resize_canvas(image):
    new_image = Image.new("RGBA", (ICON_WIDTH, ICON_HEIGHT), (255, 255, 255, 0))
    x = int((ICON_WIDTH - image.width) / 2)
    y = int((ICON_HEIGHT - image.height) / 2)
    new_image.paste(image, (x, y))
    return new_image

crop_all_files()