from rembg import remove
from PIL import Image
import sys

def remove_background(image_path, output_path):
    original_image = Image.open(image_path)
    no_background = remove(original_image)
    no_background.save(output_path)
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 rembg.py <image_path> <output_path>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    remove_background(input_path, output_path)