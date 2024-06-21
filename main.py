import cv2

# Load the image
image = cv2.imread("pika.png")

# Define the points for the star
points = [
    (256, 50), (317, 150), (427, 150), 
    (342, 218), (372, 318), (256, 260), 
    (140, 318), (170, 218), (85, 150), 
    (195, 150)
]

# Draw each line of the star
color = (0, 255, 0)  # Green color in BGR
thickness = 3  # Thickness of the lines

# Draw lines between each pair of consecutive points and the last to the first point
image = cv2.line(image, points[0], points[1], color, thickness)
image = cv2.line(image, points[1], points[2], color, thickness)
image = cv2.line(image, points[2], points[3], color, thickness)
image = cv2.line(image, points[3], points[4], color, thickness)
image = cv2.line(image, points[4], points[5], color, thickness)
image = cv2.line(image, points[5], points[6], color, thickness)
image = cv2.line(image, points[6], points[7], color, thickness)
image = cv2.line(image, points[7], points[8], color, thickness)
image = cv2.line(image, points[8], points[9], color, thickness)
image = cv2.line(image, points[9], points[0], color, thickness)

# Display the image with the star
cv2.imshow("Star on Pika", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
