from rembg import remove
from PIL import Image
import os

def remove_bg(input_path, output_path):
    """Remove background from one image"""
    try:
        img = Image.open(input_path)
        result = remove(img)
        result.save(output_path)
        print("✓ Saved:", output_path)
    except Exception as e:
        print("Error:", e)

def process_folder(input_folder, output_folder):
    """Remove background from all images in a folder"""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, f"no_bg_{file}.png")
            remove_bg(input_path, output_path)

# Main
if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"

    if not os.path.exists(input_folder):
        os.makedirs(input_folder)
        print("Put your images inside 'input_images' folder and run again.")
    else:
        process_folder(input_folder, output_folder)
        print("Done!")