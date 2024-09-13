import os
from PIL import Image

def cur_to_png(cur_file_path, png_file_path):
    # Checks if there is a file
    if not os.path.exists(cur_file_path):
        print(f"File not found: {cur_file_path}")
        return
    
    # Open the .cur file using Pillow
    with Image.open(cur_file_path) as img:
        # Convert the image to RGBA format
        img = img.convert("RGBA")
        
        # Save the image as a .png file
        img.save(png_file_path, "PNG")
        print(f"Converted {cur_file_path} to {png_file_path}")

def batch_convert_cur_to_png(cur_files_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for cur_file in os.listdir(cur_files_directory):
        if cur_file.endswith('.cur'):
            cur_file_path = os.path.join(cur_files_directory, cur_file)
            png_file_path = os.path.join(output_directory, f"{os.path.splitext(cur_file)[0]}.png")
            cur_to_png(cur_file_path, png_file_path)

# Example usage
cur_files_directory = 'C:\Windows\Cursors\Vimix Cursors'
output_directory = 'W:\Vault--02\Projects\Projects--Code\Python\Conv\output'
batch_convert_cur_to_png(cur_files_directory, output_directory)
