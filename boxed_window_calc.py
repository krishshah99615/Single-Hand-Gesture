####################### LIBRARRIES ##########################
import cv2
import numpy
import os

####################### INITIALIZAING CAPTURE ##########################
# Starting capturing
cap = cv2.VideoCapture(0)
# Setting height and width of webcam
HEIGHT, WIDTH = 360, 640
cv2.namedWindow('image')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)


####################### Setting trackbar ##########################

def nothing():
    pass


cv2.createTrackbar('x1', 'image', 0, WIDTH, nothing)
cv2.createTrackbar('y1', 'image', 0, HEIGHT, nothing)
cv2.createTrackbar('x2', 'image', 0, WIDTH, nothing)
cv2.createTrackbar('y2', 'image', 0, HEIGHT, nothing)


while(1):

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Get the values from track bar for bbox

    x1 = cv2.getTrackbarPos('x1', 'image')
    y1 = cv2.getTrackbarPos('y1', 'image')
    x2 = cv2.getTrackbarPos('x2', 'image')
    y2 = cv2.getTrackbarPos('y2', 'image')

    # showing rectangle for visual aid
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

    # printing the bbox coorrdinates
    print([x1, y1, x2, y2])

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

#[38, 33, 263, 258]
