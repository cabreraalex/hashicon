#!/usr/bin/env python3
from PIL import Image, ImageDraw
import hashlib

def icon(name):
    """Returns icon created from the passed string."""

    if len(name) == 1:
        name = name*4
    elif len(name) == 2:
        name = name*2
    elif len(name) == 3:
        name = name + name[0]

    white = "#ffffff"
    border = 50
    size = 385
    inner = 50
    inner2 = 2*inner

    color = "#" + hex(int(hashlib.md5(name.encode()).hexdigest(), 16) % 0xffffff)[2:]

    length = len(name)/4
    chars = (name[0],name[round(1*length)],name[round(2*length)],name[round(3*length)])

    image = Image.new('RGB', (920, 920), color)
    draw = ImageDraw.Draw(image)

    draw.ellipse((border, border, size+border, size+border), fill=white)
    if ord(chars[0])%3 == 0:
        draw.ellipse((border+inner, border+inner, size+border-inner, size+border-inner), fill=color)
    if ord(chars[0])%3 == 1:
        draw.ellipse((border+inner, border+inner, size+border-inner, size+border-inner), fill=color)
        draw.ellipse((border+inner2, border+inner2, size+border-inner2, size+border-inner2), fill=white)

    draw.ellipse((2*border+size, border, 2*(border+size), size+border), fill=white)
    if ord(chars[1])%3 == 0:
        draw.ellipse((2*border+size+inner, border+inner, 2*(border+size)-inner, size+border-inner), fill=color)
    if ord(chars[1])%3 == 1 :
        draw.ellipse((2*border+size+inner, border+inner, 2*(border+size)-inner, size+border-inner), fill=color)
        draw.ellipse((2*border+size+inner2, border+inner2, 2*(border+size)-inner2, size+border-inner2), fill=white)

    draw.ellipse((border, 2*border+size, size+border, 2*(border+size)), fill=white)
    if ord(chars[2])%3 == 0:
        draw.ellipse((border+inner, 2*border+size+inner, size+border-inner, 2*(border+size)-inner), fill=color)
    if ord(chars[2])%3 == 1:
        draw.ellipse((border+inner, 2*border+size+inner, size+border-inner, 2*(border+size)-inner), fill=color)
        draw.ellipse((border+inner2, 2*border+size+inner2, size+border-inner2, 2*(border+size)-inner2), fill=white)

    draw.ellipse((2*border+size, 2*border+size, 2*(border+size), 2*(border+size)), fill=white)
    if ord(chars[3])%3 == 0:
        draw.ellipse((2*border+size+inner, 2*border+size+inner, 2*(border+size)-inner, 2*(border+size)-inner), fill=color)
    if ord(chars[3])%3 == 1:
        draw.ellipse((2*border+size+inner, 2*border+size+inner, 2*(border+size)-inner, 2*(border+size)-inner), fill=color)
        draw.ellipse((2*border+size+inner2, 2*border+size+inner2, 2*(border+size)-inner2, 2*(border+size)-inner2), fill=color)

    image = image.resize((230,230), resample=Image.LANCZOS)
    return image


def main():
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Create minimalistic icons from a string')
    parser.add_argument('string', default="", nargs='*', help="string to make icon from, image saved by default as png")
    parser.add_argument('-s', '--show', action='store_true', help="show the image with xv instead of saving it")
    parser.add_argument('-e', '--extension', default="no", choices=["png", "jpg", "jpeg", "gif"], nargs="?", help="save icon as different file format, default is PNG")
    args = parser.parse_args()

    if args.string == "":
        string = input("Input a string > ")
        image = icon(string)
    else:
        string = " ".join(args.string)
        image = icon(string)

    if args.extension in ("jpeg", "jpg"):
        image.save(string + ".jpg")

    elif args.extension == "gif":
        image.save(string + ".gif")

    elif args.show:
        image.show()

    else:
        image.save(string + ".png")

if __name__ == "__main__":
    main()
