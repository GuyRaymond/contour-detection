import cv2
import os
from contour_detection import detect_contours

def process_image(INPUT_IMAGE, OUTPUT_IMAGE):
    # Load the image
    image = cv2.imread(INPUT_IMAGE)
    if image is None:
        raise FileNotFoundError(f"Input image not found at {input_path}")

    # Detect contours
    contours = detect_contours(image)

    # Draw the contours on the original image
    contour_image = image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

    # Save the processed image
    cv2.imwrite(OUTPUT_IMAGE, contour_image)

if __name__ == "__main__":
    INPUT_IMAGE = "images/input.jpg"
    OUTPUT_IMAGE = "images/output.jpg"
    process_image(INPUT_IMAGE, OUTPUT_IMAGE)
    print(f"Processed image saved at {OUTPUT_IMAGE}")
