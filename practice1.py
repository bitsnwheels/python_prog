import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def convolve_2d(image, kernel):
    # Get dimensions of the image and the kernel
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calculate padding size
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2

    # Pad the image with zeros on all sides
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant')

    # Prepare the output array
    output = np.zeros((image_height, image_width))

    # Perform convolution operation
    for i in range(image_height):
        for j in range(image_width):
            # Extract the region of interest
            region = padded_image[i:i + kernel_height, j:j + kernel_width]
            # Apply the kernel (element-wise multiplication and summing up)
            output[i, j] = np.sum(region * kernel)
    
    # Clip values to be in the range [0, 255] and return as uint8
    output = np.clip(output, 0, 255).astype(np.uint8)
    return output

# Define the edge detection filter
kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])

# Load an image as grayscale
image_path = "slide1.jpg"  # Replace with the path to your image
image = Image.open(image_path).convert("L")  # Convert to grayscale
image_array = np.array(image)

# Apply the 2D convolution function
edges = convolve_2d(image_array, kernel)

# Display the original and convolved (edges) image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_array, cmap="gray")

plt.subplot(1, 2, 2)
plt.title("Edges Detected")
plt.imshow(edges, cmap="gray")
plt.show()

