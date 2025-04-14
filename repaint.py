from PIL import Image
import os

# Directory containing the images
input_dir = "data/Ricks256"
output_dir = "data/Ricks256_edited"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Rectangle dimensions (adjust as needed)
rect_width = 89
rect_height = 50

# Process each image in the directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png')):
        # Open the image
        img_path = os.path.join(input_dir, filename)
        img = Image.open(img_path)
        img = img.convert("RGBA")  # Ensure image is in RGBA mode

        # Get image dimensions
        width, height = img.size

        # Determine the background color (top-left pixel)
        background_color = img.getpixel((0, 0))

        # Create a drawing context
        pixels = img.load()

        # Define the rectangle's position (bottom-right corner)
        start_x = width - rect_width
        start_y = height - rect_height

        # Repaint the rectangle
        for x in range(start_x, width):
            for y in range(start_y, height):
                pixels[x, y] = background_color

        # Save the modified image
        output_path = os.path.join(output_dir, filename)
        img.save(output_path)



print("All images have been processed and saved to:", output_dir)