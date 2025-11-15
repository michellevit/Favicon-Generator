import os
from PIL import Image

def find_png_file():
    png_files = [file for file in os.listdir('.') if file.endswith('.png')]
    
    if len(png_files) > 1:
        raise ValueError("Error: Multiple PNG files found in the directory.")
    elif len(png_files) == 0:
        raise ValueError("Error: No PNG file found in the directory.")
    else:
        return png_files[0]

def convert_png_to_ico():
    png_file_path = find_png_file()
    ico_file_path = os.path.splitext(png_file_path)[0] + '.ico'
    
    img = Image.open(png_file_path).convert("RGBA")  
    img.save(ico_file_path, format='ICO')

    width, height = img.size
    print(f"A new favicon has been created of size {width} x {height}.")

try:
    convert_png_to_ico()
except ValueError as e:
    print(e)