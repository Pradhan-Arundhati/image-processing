import cv2
import numpy as np

# Read an image
image = cv2.imread('"C:\Users\arundhati\OneDrive\Desktop\Screenshot_20200405-163533.png"')

# Grayscale filter
def grayscale_filter(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur filter
def blur_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)

# Edge detection filter
def edge_detection_filter(image):
    return cv2.Canny(image, 100, 200)

# Sharpen filter
def sharpen_filter(image):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

# Apply the filters
grayscale_image = grayscale_filter(image)
blurred_image = blur_filter(image)
edges_image = edge_detection_filter(image)
sharpened_image = sharpen_filter(image)

# Display the original and filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', grayscale_image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Edges Image', edges_image)
cv2.imshow('Sharpened Image', sharpened_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
