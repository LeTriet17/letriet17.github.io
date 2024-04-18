from PIL import Image
import os

def resize_images_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # Check if file is an image
            filepath = os.path.join(directory, filename)
            try:
                img = Image.open(filepath)
                width, height = img.size
                img_resized = img.resize((width//4, height//4))
                img_resized.save(filepath)
                print(f"Resized {filename} successfully.")
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

# Usage example:
directory_path = "love"
resize_images_in_directory(directory_path)
