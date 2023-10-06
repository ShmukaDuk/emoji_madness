from pilmoji import Pilmoji
from PIL import Image, ImageFont
import json

my_string = '🌊'
str2 = '😀'
str3 = '🌸'
my_list = ["😀"]
my_dict = []

def load_emojis(path):
    with open(path, 'r', encoding='utf-8') as emoji_file:
        for line in emoji_file:
            emoji = line.strip()  # Remove leading/trailing whitespace, including newline character
            if (len(emoji) == 1):
                my_list.append(emoji)       
            
            
def calc_average_rgb(image):
    w, h = image.size
    total_r, total_g, total_b = 0, 0, 0
    num_pixels = 0
    for x in range(w):
        for y in range(h):
            r, g, b, a = image.getpixel((x, y))  # Get RGBA values
            if a > 240:                
            # Ignore the alpha channel by not using 'a'
                total_r += r
                total_g += g
                total_b += b
                num_pixels += 1
    if num_pixels != 0:
        avg_r = total_r // num_pixels
        avg_g = total_g // num_pixels
        avg_b = total_b // num_pixels
        avg_color = (avg_r, avg_g, avg_b)
        return avg_color
    # new_image = Image.new('RGB', (w, h), avg_color)
    # new_image.show()
    return (0,0,0)

    # Save or display the new image

def convertEmojiToRGB(emoji):
    
    with Image.new('RGBA', (32, 32), (255, 255, 255, 0)) as image:  # Use 'RGBA' mode with a transparent background
        font = ImageFont.truetype('arial.ttf', 24)

        with Pilmoji(image) as pilmoji:
            pilmoji.text((0, 0), emoji.strip(), (0, 0, 0), font)
        # image.show()
        avg_color = calc_average_rgb(image)
        return avg_color, emoji

def save_lut(my_dict):    
    json_data = [{'Emoji': emoji, 'RGB Color': avg_color} for avg_color, emoji in my_dict]
    # Save the JSON data to a file
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

    
# load_emojis('emojibase')

# for str in my_list:
#     print(str)
#     my_dict.append(convertEmojiToRGB(str))

# for lut in my_dict:
#     print(lut)

# save_lut(my_dict)

# print(emoji_data)
    
# # Iterate through each frame in the GIF
# try:
#     while True:
#         current_frame = gif.copy()
#         # current_frame.show()  # Display or process the frame as needed
#         gif.seek(gif.tell() + 1)
# except EOFError:
#     pass

# # Close the GIF file
# gif.close()
# Open the GIF file
# gif_file = "data/carlton.gif"
# gif = Image.open(gif_file)
# width, height = gif.size
# print(f"Width: {width}px")
# print(f"Height: {height}px")