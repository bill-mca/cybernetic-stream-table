import cv2
import numpy as np
import sys
from picamera2 import Picamera2


def count_yellow_objects_on_cam():
    objectCounter = 0

    # Take a still that we will analyse
    img = picam2.capture_array()
    img_copy = img.copy()

    ## Analyse

    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    yellow_lower = np.array([20, 180, 180], np.uint8)
    yellow_upper = np.array([30, 255, 255], np.uint8)
    yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper)

    # DOWNSCALE
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)
    eroded_mask = cv2.erode(yellow_mask, kernel, iterations=1)
    dilated_mask = cv2.dilate(yellow_mask, kernel, iterations=8)
    #cv2.imwrite("cv2-eroded-mask-test.png", eroded_mask)

    ## Count

    # from https://stackoverflow.com/questions/71491995/how-to-count-the-color-detected-objects-using-opencv/71492126#71492126

    # Find the contours on the binary image:
    contours, hierarchy = cv2.findContours(dilated_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Store bounding rectangles and object id here:
    objectData = []

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
        cv2.rectangle(img_copy, (int(rectX), int(rectY)),
                    (int(rectX + rectWidth), int(rectY + rectHeight)), color, 2)

        # Draw object counter:
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontThickness = 2
        color = (0, 255, 0)
        cv2.putText(img_copy, str(objectCounter), (int(rectX), int(rectY)),
                    font, fontScale, color, fontThickness)

        #cv2.imwrite("cv2-object-{}.png".format(objectCounter), img_copy)

        # Increment object counter
        objectCounter += 1
    print(objectCounter)
    return(img_copy)

if __name__ == '__main__':
    ## Import image
    fname = sys.argv[-1]

    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    picam2.start()

    cv2.waitKey(2000)

    while True:
        cv2.imshow("The Cybernetic Stream Y'all", count_yellow_objects_on_cam())
        cv2.waitKey(50)


