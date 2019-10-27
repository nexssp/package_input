# Nexss PROGRAMMER 2.0.0 - Python3
# Default template for JSON Data

import platform
import json
import sys
import os

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


# STDIN
NexssStdin = sys.stdin.read()

parsedJson = json.loads(NexssStdin)
# Modify Data
# parsedJson["PythonOutput"] = "Hello from Python! " + \
#     str(platform.python_version())

# parsedJson["test"] = "test"


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(
        Image.open(filename)
    )  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

if not "file" in parsedJson:
    parsedJson["error"] = "You need to pass image file to parse."
    exit(1)


if not ":"+os.path.sep in parsedJson["file"]:
    resultText = ocr_core(parsedJson["cwd"] + "/" + parsedJson["file"])
else:
    resultText = ocr_core(parsedJson["file"])
    
parsedJson["text"] = resultText
NexssStdout = json.JSONEncoder().encode(parsedJson)
# STDOUT
sys.stdout.write(NexssStdout)
