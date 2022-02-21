import cv2 as cv
import numpy as np
from datetime import datetime

widthImg, heightImg = 640, 280
contour_color = (0, 255, 0)

# Local path to the haarcascade_russian_plate_number file (raise an issue if you can't download)
cascadeFilePath = "HaarCascadeFiles/haarcascade_russian_plate_number.xml"


def empty(x):
    """Placeholder: Nothing happens when the TrackbarPos is changed"""
    pass


# Creation of trackbars and a window
cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 500, 200)
cv.createTrackbar("Scale", "Trackbars", 99, 1000, empty)
cv.createTrackbar("Min Neig", "Trackbars", 3, 20, empty)  # Minimum Neighbors
cv.createTrackbar("Min Area", "Trackbars", 450, 11000, empty)  # Minimum Area

cascade = cv.CascadeClassifier(cascadeFilePath)  # Loading the classifiers

# Contains the local path to one or many images where the CarPlates are to be detected
all_images = [
    "test_images/plate1.jfif",
    "test_images/plate2.jfif",
    "test_images/plate3.jfif",
    "test_images/plate5.jfif",
    "test_images/plate6.jfif",
]

read_images = []  # Initialisation of variable
for image in all_images:
    reading = cv.imread(image)  # The individual image is READ
    read_images.append(reading)  # And stored in a list initialised above


def plateDetector(img, scale, area_min, neighbors_min):
    """Returns the Plate(if found) and the Original Image(with contours on Plate)"""

    copy = img.copy()  # Necessary when cropping the Original image
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert to grayScale
    scaleVal = 1 + (scale / 1000)  # Max value = 1 + (1000/1000)
    carPlates = cascade.detectMultiScale(imgGray, scaleVal, neighbors_min)
    croppedPlate = img
    for (x, y, w, h) in carPlates:
        area = w * h  # The area of the detected plate
        if area > area_min:  # Compare if greater than our Trackbar's Min Area
            cv.rectangle(copy, (x, y), (x + w, y + h), contour_color, 2)  # Draw rectangle on the COPY
            cv.putText(copy, "Plate", (x, y - 5), cv.FONT_HERSHEY_COMPLEX, 1, contour_color, 2)  # Puts Text on the COPY
            croppedPlate = img[y:y + h, x:x + w]  # OriginalImage being cropped to show the Plate only

    return croppedPlate, copy  # returns the final(plate-only) and the original(fix but with contours) images


def stackImages(new_image_scale, imgArray):
    """Easy Stacking function by Murtaza"""

    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (0, 0), None, new_image_scale, new_image_scale)
                else:
                    imgArray[x][y] = cv.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None,
                                               new_image_scale, new_image_scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv.cvtColor(imgArray[x][y], cv.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv.resize(imgArray[x], (0, 0), None, new_image_scale, new_image_scale)
            else:
                imgArray[x] = cv.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,
                                        new_image_scale, new_image_scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv.cvtColor(imgArray[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


print(
    "Info: \n-Try moving the Trackbars to have better results; \n-If you find the about large, reduce the new_image_scale value.")
while True:
    imageArray1 = []  # contains the originalFixed images (with some contours)
    imageArray2 = []  # Contains the cropped plates(only) or the original images(when plate not found)

    scale_value = cv.getTrackbarPos("Scale", "Trackbars")  # Get the ScaleTrackbar Position
    min_neighbors = cv.getTrackbarPos("Min Neig", "Trackbars")  # Get the MinNeighborTrackbar Position
    min_area = cv.getTrackbarPos("Min Area", "Trackbars")  # Get the MinAreaTrackbar Position
    for i in read_images:
        finalOutput, originalInput = plateDetector(i, scale_value, min_area, min_neighbors)
        imageArray1.append(originalInput)  # Adding to array
        imageArray2.append(finalOutput)  # Adding to array

    # Stacking of the arrays with a new_scale: imageArray1 is stacked vertically on imageArray2
    new_image_scale = 0.9
    stack = stackImages(new_image_scale, (imageArray1, imageArray2))

    cv.imshow("Car Plate Detector by ndonkoHenri", stack)  # Displays the stacked images
    if cv.waitKey(1) == 113:  # Q=113
        break
    """if cv.waitKey(1) & 0xFF == ord('s'):
        newImageArray2 = []
        saving_count+=1
        for idx, s in enumerate(imageArray2):
            # print(s.shape)
            # cv2.imwrite(f"Resources/images/Car Plates/SavedPlates/Plate_{read_images[idx].lstrip('Resources/images/Car Plates/')}_{datetime.now()}_{saving_count}",imageArray2)
            cv.rectangle(imageArray1[idx], (5, 5), (40, 30), (0, 255, 0), cv.FILLED)
            cv.putText(imageArray1[idx], "| §av£d |", (10, 10), cv.FONT_HERSHEY_TRIPLEX, 2, (255, 0, 0), 2)
            cv.imshow("Car Plate Detector ", stack)
            cv.waitKey(500)"""
