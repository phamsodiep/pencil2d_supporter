#!/usr/local/bin/python3
import sys
from PIL import Image


def setTransparen(img):
    (width, height) = img.size
    #img = img.convert("RGBA")
    for y in range(0, height):
        for x in range(0, width):
            rgb = img.getpixel((x, y))
            if (rgb[0] == 255) and (rgb[1] == 255) and (rgb[2] == 255):
                rgb = (rgb[0], rgb[1], rgb[2], 0)
                img.putpixel((x, y), rgb)
    return img

startParam = 0.5
countParam = 1
stepParam = 0.1

# Check if there is enough input parameters            
if len(sys.argv) < 2:
    cmd = "{0} <start index> [start alpha] [image count] [increase step alpha]"
    print(cmd.format(sys.argv[0]))
    print("Where:")
    print("\t<start index>: start index for output filename")
    startAlpha = "".join([
        "\t[start alpha]: ",
        "alpha start value parameter (range: 0..1, default: {0})"
    ])
    print(startAlpha.format(startParam))
    print("\t[image count]: fade frame count (default: {0})".format(countParam))
    step = "".join([
        "\t[increase step alpha]: ",
        "increase alpha value of each frame (default: {0})"
    ])
    print(step.format(stepParam))
    sys.exit()

startIdx = int(sys.argv[1])

# PARAMS PROCESSING
if len(sys.argv) >= 3:
    startParam = float(sys.argv[2])
if len(sys.argv) >= 4:
    countParam = int(sys.argv[3])
if len(sys.argv) >= 5:
    stepParam = float(sys.argv[4])

print(startIdx)
print(startParam)
print(countParam)
print(stepParam)

# @TODO: param range checking (validating)

imgA = None
imgB = None
try:
    imgA = Image.open("a.png")
except:
    imgA = None
try:
    imgB = Image.open("b.png")
except:
    imgB = None


if imgA == None:
    print("file 'a.png' is not found")
    sys.exit()

if imgB == None:
    imgB = Image.new('RGBA', imgA.size, (255, 255, 255, 255))


alpha = startParam
idx = startIdx
for idx in range(startIdx, countParam + startIdx):
    fileName = "a.{:03d}".format(idx) + ".png"
    img = Image.blend(imgA, imgB, alpha)
    alpha += stepParam
    idx += 1
    #img.show()
    img = setTransparen(img)
    img.save(fileName)