from PIL import Image, ImageDraw, ImageFont
import sys
import colorama
from colorama import Fore, Back, init

colorama.init(autoreset=True)

ascii_art_generator ="   _____    _________________ .___.___\n  /  _  \  /   _____\_   ___ \|   |   |\n /  /_\  \ \_____  \/    \  \/|   |   |  \n/    |    \/        \     \___|   |   |  \n\____|__  /_______  /\______  |___|___|  \n        \/        \/        \/                 \n   _____          __    ________                                   __  \n  /  _  \________/  |_ /  _____/  ____   ____   ________________ _/  |_ ___________   \n /  /_\  \_  __ \   __/   \  ____/ __ \ /    \_/ __ \_  __ \__  \\    __/  _ \_  __ \    \n/    |    |  | \/|  | \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  |(  <_> |  | \/  \n\____|__  |__|   |__|  \______  /\___  |___|  /\___  |__|  (____  |__| \____/|__|     \n        \/                    \/     \/     \/     \/           \/                  "

#ascii_chars = " .-~+=*#%$@"
#ascii_chars = " .,'-~:;=+^*>!\)]#&$%@"
ascii_chars = " .,-~:;=+^*>!\#$&%@"
#ascii_chars = " .,-~+*#$%@"

# width = 100

# image = Image.open("galaxy.jpg")
# image = Image.open("luffy.jpg")
# image = Image.open("spiderman.png")
# image = Image.open("eldenring.jpg")
# image = Image.open("ds.jpg")
# image = Image.open("dww.jpg")
# image = Image.open("mando.jpg")
# image = Image.open("deathstar.jpg")
# image = Image.open("ag2.jpg")
# image = Image.open("ag3.jpg")
# image = Image.open("ag4.jpg")

# height = height - 60

# Resizing input image

def print_err():
    print(" ")
    print( '\033[31m' + f"Usage: python {sys.argv[0]} <input_image> <output_type>" + '\033[39m')
    print("<input_image> - Your input image. [.png, .jpg, .jpeg, .webp, .tiff etc]")
    print("                Check https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html for Image file format support.\n")
    print("<output_type> - Use '-' or 'stdout' to print the output in command line.")
    print("                Use 'txt' to get output in text file. You will get ascii_text.txt")
    print("                Use 'img' to get output in image file. You will get ascii_image.jpg")

def save_ascii_image(image_path, output_path, font_path=None, font_size = 30, color = (255,255,255)):
    width=200
    ascii_chars=" .,-~:;=+^*>!\#$&%@"
    image = Image.open(image_path)
    height = int(width * image.height // image.width *0.7)
    # height = int(width * image.height // image.width)
    image = image.resize((width,height), Image.NEAREST)
    text = ""
    for y in range(height):
        for x in range(width):
            if image.getpixel((x,y)) == 0:
                r = g = b = 0
            elif image.getpixel((x,y)) == 1:
                r = g = b = 256
            else:
                r, g, b = image.getpixel((x,y))
            gray = 0.299 * r + 0.587 * g + 0.114 * b
            index = int(gray / 256 * len(ascii_chars))
            text += ascii_chars[index]
        text += "\n"

    lines = text.split("\n")
    first_line = lines[0]
    width = int(len(first_line) * font_size*0.605)
    height = len(lines) * font_size
    # create a blank image
    img = Image.new('RGB',(width,height),(0,0,0))
    draw = ImageDraw.Draw(img)
    # load fonts
    font = ImageFont.truetype("fonts/CourierPrime-Regular.ttf", font_size)

    draw.text((10,10), text, fill=color, font=font)
    img.save(output_path)

def create_ascii_art(image_path, width=100,ascii_chars=" .,-~:;=+^*>!\#$&%@"):
    image = Image.open(image_path)
    # height = int(width * image.height // image.width *0.59)
    height = int(width * image.height // image.width *0.9)
    image = image.resize((width,height), Image.NEAREST)
    ascii_image = ""
    for y in range(height):
        for x in range(width):
            if image.getpixel((x,y)) == 0:
                r = g = b = 0
            elif image.getpixel((x,y)) == 1:
                r = g = b = 256
            else:
                r, g, b = image.getpixel((x,y))
            gray = 0.299 * r + 0.587 * g + 0.114 * b
            index = int(gray / 256 * len(ascii_chars))
            # print(ascii_chars[index], end="")
            # print(ascii_chars[index], end="")
            ascii_image += ascii_chars[index]
            ascii_image += ascii_chars[index]
        # print()
        ascii_image += "\n"
    # print(ascii_image)
    print("ASCII art dimentions - ",height,'x',width)
    return ascii_image

def save_ascii_art(input_image, output_type):

    ascii_image = create_ascii_art(input_image)

    if output_type == "txt":
        with open("ascii_text", "w") as f:
            f.write(ascii_image)
        print("ASCII Art saved to text file!")
    elif output_type == "-" or output_type == "stdout":
        print(ascii_image)
        print("lmao")
    elif output_type == 'img':
        save_ascii_image(sys.argv[1],"ascii_image.jpg")
        print("ASCII Art saved to ascii_image.jpg!")
    else:
        print_err()

if __name__ == "__main__":
    print(ascii_art_generator)
    if len(sys.argv) < 3:
        print_err()
        sys.exit(1)
    
    input_image = sys.argv[1]
    output_type = sys.argv[2]
    
    save_ascii_art(input_image, output_type)

    # save_ascii_image(input_image,"ascii_image.jpg")