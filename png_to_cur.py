import os
import subprocess
from PIL import Image

def png_to_cur(png_file_path, cur_file_path):
    if not os.path.exists(png_file_path):
        print(f"File not found: {png_file_path}")
        return
    
    # Convert the image to RGBA format using Pillow
    with Image.open(png_file_path) as img:
        img = img.convert("RGBA")
        temp_png_path = png_file_path.replace('.png', '_temp.png')
        img.save(temp_png_path, "PNG")
    
    # Use ImageMagick to convert the PNG to CUR
    command = f"magick convert {temp_png_path} {cur_file_path}"
    subprocess.run(command, shell=True)
    os.remove(temp_png_path)
    print(f"Converted {png_file_path} to {cur_file_path}")

def batch_convert_png_to_cur(png_files_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for png_file in os.listdir(png_files_directory):
        if png_file.endswith('.png'):
            png_file_path = os.path.join(png_files_directory, png_file)
            cur_file_path = os.path.join(output_directory, f"{os.path.splitext(png_file)[0]}.cur")
            png_to_cur(png_file_path, cur_file_path)

# Example usage
png_files_directory = r'W:\Vault--02\Projects\Projects--Code\Python\Conv\png_to_cur\Input'
output_directory = r'W:\Vault--02\Projects\Projects--Code\Python\Conv\png_to_cur\Output'
batch_convert_png_to_cur(png_files_directory, output_directory)