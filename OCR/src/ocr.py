# Nexss PROGRAMMER 2.x - Python3
# OCR image

import platform
import json
import sys
import os
from os import path

try:
    from PIL import Image, ImageEnhance, ImageFilter
except ImportError:
    import Image
import pytesseract

# STDIN
NexssStdin = sys.stdin.read()

parsedJson = json.loads(NexssStdin)
# Modify Data
# parsedJson["test"] = "test"
# config = "-c tessedit_char_whitelist=0123456789X"
config = ""


def ocr(filename):
    img = Image.open(filename)

    img = img.filter(ImageFilter.MedianFilter())

    img = ImageEnhance.Contrast(img)
    img = img.enhance(3)
    img = img.convert('L')

    img = ImageEnhance.Brightness(img).enhance(3.0)
    img = ImageEnhance.Contrast(img).enhance(2.0)

    text = pytesseract.image_to_string(
        img, lang="eng", config=config)
    return text


if not "file" in parsedJson:
    parsedJson["error"] = "You need to pass image file to parse."
else:
    if not ":" + os.path.sep in parsedJson["file"]:
        p = parsedJson["cwd"] + "/" + parsedJson["file"]
    else:
        p = parsedJson["file"]

    if not path.exists(p):
        sys.stdout.write("File not found", p)

    resultText = ocr(p)

    parsedJson["text"] = resultText

NexssStdout = json.JSONEncoder().encode(parsedJson)
# STDOUT
sys.stdout.write(NexssStdout)

if not "file" in parsedJson:
    exit(1)
