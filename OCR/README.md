# Input/OCR Nexss PROGRAMMER 2.0

Convert Image to Text.

## Install

```sh
# First we need to capture screen region and save it as 1.png
# (this also will work without parameters as the parameter 'file' is the same.)
nexss Screen/Capture --file=1.png # We capture the screenshot of mouse selection.

nexss Input/OCR --file=1.png # COnvert to text
```

## Credits

Languages/Technologies used for this Nexss PROGRAMMER package:

- NodeJS
- Python
- <https://github.com/madmaze/pytesseract>
- <https://github.com/python-pillow/Pillow>

## Development

```sh
nexss py install pytesseract Pillow
```
