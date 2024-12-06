import cv2
import numpy as np
from PIL import Image

def detect_contours(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Detect edges using Canny edge detection
    edges = cv2.Canny(blurred_image, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

