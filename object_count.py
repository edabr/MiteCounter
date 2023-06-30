import cv2

# Load the image
image = cv2.imread("images/6.png")              #TODO set the thresholds??? TO CONSIDER

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a binary image
_, threshold = cv2.threshold(gray, 56, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Print the number of objects detected
print("Number of objects:", len(contours))

cv2.imshow("Edges", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Measure the number of pixels for each contour
for i, contour in enumerate(contours):
    contour_area = cv2.contourArea(contour)
    print(f"Object {i+1}: {contour_area} pixels")

