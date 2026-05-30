import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def calculate_porosity(image_path):
    # Load the SEM image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Unable to read the image. Please check the file path.")

    # Thresholding
    _, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Total pixels
    total_pixels = binary.size

    # Updated: pores are black pixels (0)
    pore_pixels = total_pixels - cv2.countNonZero(binary)

    # Porosity
    porosity = pore_pixels / total_pixels * 100

    return porosity, binary

def change_binary_color(binary_image, pore_color=(0, 255, 0), background_color=(255, 0, 0)):
    colored_image = np.zeros((*binary_image.shape, 3), dtype=np.uint8)

    # Keep the same mapping as the old code (unchanged)
    colored_image[binary_image == 255] = pore_color
    colored_image[binary_image == 0] = background_color

    return colored_image

def save_figure(image_path, colored_image, porosity):
    folder, filename = os.path.split(image_path)
    name, _ = os.path.splitext(filename)
    output_path = os.path.join(folder, f"{name}_calculated.png")

    height = colored_image.shape[0]

    plt.figure(figsize=(5, 3))
    plt.imshow(cv2.cvtColor(colored_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Colored Binary Image")

    # Keep the text style unchanged
    plt.text(10, height - 10, f"Porosity: {porosity:.2f}%",
             color='white', fontsize=12,
             bbox=dict(facecolor='black', alpha=0.6))

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    return output_path

# ===== MAIN =====
image_path = r"Your SEM file path here"  # Update this with your actual SEM image path

porosity, binary_image = calculate_porosity(image_path)
colored_binary_image = change_binary_color(binary_image)

output_file = save_figure(image_path, colored_binary_image, porosity)

print(f"Porosity: {porosity:.2f}%")
print(f"Saved to: {output_file}")

# Display (optional)
plt.imshow(cv2.cvtColor(colored_binary_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
