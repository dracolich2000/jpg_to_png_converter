# jpg_to_png_converter

This script converts images from JPG format to PNG format.

## Features

- Converts JPG images to PNG format.
- Skips images that are already in PNG format.
- Handles errors gracefully when opening images.
- Simple command-line interface.


Description:
This Python script converts images from JPG format to PNG format. It takes two command-line arguments:
1. The folder path/name from which you want to convert images (image_folder).
2. The output folder name/path (output_folder) where converted PNG images will be saved.

## Usage

1. Clone the repository or download the `ImageConverter.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `ImageConverter.py` script.
4. Run the script using the following command:
          python ImageConverter.py <image_folder> <output_folder>

Dependencies:
1. Python 3.x
2. Pillow library (PIL fork) for image processing. Install it using: pip install Pillow

Example Usage:
1. Convert images from "input_images" folder to "output_images" folder:
   python ImageConverter.py input_images output_images
