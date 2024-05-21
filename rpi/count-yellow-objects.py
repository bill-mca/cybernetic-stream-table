import cv2
import numpy as np
import sys

def main(fname):
    img = cv2.imread(fname, cv2.IMREAD_COLOR)
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
    #cv2.imwrite("cv2-eroded-mask-test.png", eroded_mask)

    ## Count

    # from https://stackoverflow.com/questions/71491995/how-to-count-the-color-detected-objects-using-opencv/71492126#71492126

    # Find the contours on the binary image:
    contours, hierarchy = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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
        cv2.rectangle(img_copy, (int(rectX), int(rectY)),
                    (int(rectX + rectWidth), int(rectY + rectHeight)), color, 2)

        # Draw object counter:
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 1
        fontThickness = 2
        color = (0, 255, 0)
        cv2.putText(img_copy, str(objectCounter), (int(rectX), int(rectY)),
                    font, fontScale, color, fontThickness)

        cv2.imwrite("cv2-object-{}.png".format(objectCounter), img_copy)

        # Increment object counter
        objectCounter += 1

    lfname = fname.split('/')
    lfname[-1] = "cv2-counted-" + lfname[-1]
    cv2.imwrite('/'.join(lfname), img_copy)
    print(objectCounter)

if __name__ == '__main__':
    ## Import image
    fname = sys.argv[-1]
    main(fname)