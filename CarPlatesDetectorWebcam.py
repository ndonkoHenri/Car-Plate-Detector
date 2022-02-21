import cv2 as cv
import numpy as np

widthImg, heightImg = 640, 280
contour_color = (0, 255, 0)
cap = cv.VideoCapture(0)
cap.set(3, widthImg)
cap.set(4, heightImg)
# Local path to the haarcascade_russian_plate_number file (raise an issue if you can't download)
cascadeFilePath = "HaarCascadeFiles/haarcascade_russian_plate_number.xml"


def empty(x):
    pass


cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 500, 200)
cv.createTrackbar("Brightness", "Trackbars", 72, 255, empty)
cv.createTrackbar("Scale", "Trackbars", 3, 100, empty)
cv.createTrackbar("Min Neig", "Trackbars", 2, 20, empty)  # Minimum Neighbors
cv.createTrackbar("Min Area", "Trackbars", 10, 6000, empty)  # Minimum Area

cascade = cv.CascadeClassifier(cascadeFilePath)  # Loading the classifiers

print(
    "Info: \n-Try moving the Trackbars to have better results; \n-Press Q to stop the Program! !")
while True:
    success, img = cap.read()
    brightness = cv.getTrackbarPos("Brightness", "Trackbars")
    cap.set(10, brightness)
    scale = cv.getTrackbarPos("Scale", "Trackbars")  # Get the ScaleTrackbar Position
    min_neighbors = cv.getTrackbarPos("Min Neig", "Trackbars")  # Get the MinNeighborTrackbar Position
    min_area = cv.getTrackbarPos("Min Area", "Trackbars")  # Get the MinAreaTrackbar Position

    # copy = img.copy()  # Necessary when cropping the Original image
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Convert to grayScale
    scaleVal = 1 + (scale / 1000)  # Max value = 1 + (1000/1000)
    carPlates = cascade.detectMultiScale(imgGray, scale, min_neighbors)

    croppedPlate = img
    for (x, y, w, h) in carPlates:
        area = w * h  # The area of the detected plate
        if area > min_area:  # Compare if greater than our Trackbar's Min Area
            cv.rectangle(img, (x, y), (x + w, y + h), contour_color, 2)  # Draw rectangle on the COPY
            cv.putText(img, "Plate", (x, y - 5), cv.FONT_HERSHEY_COMPLEX, 1, contour_color,
                       2)  # Puts Text on the COPY
            croppedPlate = img[y:y + h, x:x + w]  # OriginalImage being cropped to show the Plate only
            cv.imshow("Plate Only", croppedPlate)

    cv.imshow("Car Plate Detector by ndonkoHenri", img)  # Displays the stacked images
    if cv.waitKey(1) == 113:  # Q=113
        break