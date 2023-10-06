from pilmoji import Pilmoji
from PIL import Image, ImageFont, ImageSequence
import json
import math
import os

my_string = '🌊'
str2 = '😀'
str3 = '🌸'
my_list = ["😀"]
my_dict = []
data = []
gif_w = 50
gif_h = 50

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


def calculate_distance(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

target_rgb = (11, 101, 11)


def loadJson(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        return data

def findEmojiFromPixel(data, target_rgb):
    # print(data)
    closest_color = None
    closest_distance = float('inf')
    for item in data:
        emoji_rgb = item["RGB Color"]
        # print(emoji_rgb, target_rgb)
        distance = calculate_distance(target_rgb, emoji_rgb)
        # print(distance)
        if distance < closest_distance:
            closest_distance = distance
            closest_color = emoji_rgb
            closest_emoji = item["Emoji"]
            # print(f"Closest RGB Color: {closest_color}")
            # print(f"Closest Emoji: {closest_emoji}")
    return closest_emoji

def prepImage(input_image_path, data):
    with Image.open(input_image_path) as img:
        gif_as_txt= []
        gif_frames = [frame.copy() for frame in ImageSequence.Iterator(img)]

        for frame in gif_frames:
            resized_img = frame.resize((gif_w, gif_h))
            resized_img = resized_img.convert('RGBA')
            # resized_img.show()
            emoj_line = ""
            for x in range(gif_h):
                for y in range(gif_w):
                    r, g, b, a = resized_img.getpixel((y, x))  # Get RGBA values
                    found_emoji = findEmojiFromPixel(data, (r, g, b))
                    # print(r,g,b)
                    emoj_line += found_emoji
                
                emoj_line += "\n"
            # print(emoj_line)
            gif_as_txt.append(emoj_line)
    return gif_as_txt
                
data = loadJson('output.json')
gif_as_txt = prepImage("carlton.gif", data)
while 1:
    for txt in gif_as_txt:
        print(txt)
        # os.system('cls' if os.name == 'nt' else 'clear')
# emoji = findEmojiFromPixel(data, target_rgb)



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