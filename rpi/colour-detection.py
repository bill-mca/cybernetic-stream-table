import cv2
import numpy as np

## Import images

img = cv2.imread("training_images/0520172924.jpg", cv2.IMREAD_COLOR)
width = 300
height = 200

# potentially use this if you need better rescaling
# https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
resized_down = cv2.resize(img, (width, height), interpolation= cv2.INTER_LINEAR)

input_image_copy = img.copy()

# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
#cv2.imshow("image", img)

cv2.imwrite("cv2-test.png", img)

## Analyse

# Convert the img in
# BGR(RGB color space) to
# HSV(hue-saturation-value)
# color space
hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Set range for red color and
# define mask
red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)
red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

# Set range for green color and
# define mask
green_lower = np.array([30, 52, 72], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)
green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

# Set range for blue color and
# define mask
blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)
blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

# Set range for yellow color and
# define mask
yellow_lower = np.array([20, 180, 180], np.uint8)
yellow_upper = np.array([30, 255, 255], np.uint8)
yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

# cv2.imshow('blag', img_erosion)

# Set range for yellow color and
# define mask
bright_mask = cv2.inRange(hsvFrame, np.array([0, 0, 200], np.uint8), np.array([255, 255, 255], np.uint8))

black_mask = cv2.inRange(hsvFrame, np.array([0, 0, 0], np.uint8), np.array([255, 255, 50], np.uint8))

sat_mask = cv2.inRange(hsvFrame, np.array([0, 200, 0], np.uint8), np.array([255, 255, 255], np.uint8))

cv2.imwrite("cv2-red-mask-test.png", red_mask)
cv2.imwrite("cv2-green-mask-test.png", green_mask)
cv2.imwrite("cv2-blue-mask-test.png", blue_mask)
cv2.imwrite("cv2-yellow-mask-test.png", yellow_mask)
cv2.imwrite("cv2-brightness-mask-test.png", bright_mask)
cv2.imwrite("cv2-saturation-mask-test.png", sat_mask)
cv2.imwrite("cv2-black-mask-test.png", black_mask)

# Taking a matrix of size 5 as the kernel
# DOWNSCALE
kernel = np.ones((5, 5), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
eroded_mask = cv2.erode(yellow_mask, kernel, iterations=1)

cv2.imwrite("cv2-eroded-mask-test.png", eroded_mask)

## Count

# from https://stackoverflow.com/questions/71491995/how-to-count-the-color-detected-objects-using-opencv/71492126#71492126

# Find the contours on the binary image:
contours, hierarchy = cv2.findContours(eroded_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Store bounding rectangles and object id here:
objectData = []

# ObjectCounter:
objectCounter = 1

# Look for the outer bounding boxes (no children):
for _, c in enumerate(contours):
    # Get the contour's bounding rectangle:
    boundRect = cv2.boundingRect(c)

    # Store in list:
    objectData.append((objectCounter, boundRect))

    # Get the dimensions of the bounding rect:
    rectX = boundRect[0]
    rectY = boundRect[1]
    rectWidth = boundRect[2]
    rectHeight = boundRect[3]

    # Draw bounding rect:
    color = (0, 0, 255)
    cv2.rectangle(input_image_copy, (int(rectX), int(rectY)),
                  (int(rectX + rectWidth), int(rectY + rectHeight)), color, 2)

    # Draw object counter:
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontThickness = 2
    color = (0, 255, 0)
    cv2.putText(input_image_copy, str(objectCounter), (int(rectX), int(rectY)),
                font, fontScale, color, fontThickness)

    #cv2.imshow("Rectangles", input_image_copy)
    #cv2.waitKey(0)
    cv2.imwrite("cv2-object-{}.png".format(objectCounter), input_image_copy)

    # Increment object counter
    objectCounter += 1

cv2.imwrite("cv2-counted-yellow-stuff.png", input_image_copy)

print(objectCounter)

## Clean up

cv2.destroyAllWindows()