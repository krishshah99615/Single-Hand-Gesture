####################### LIBRARRIES ##########################
import cv2
import numpy
import os
import argparse

####################### INITIALIZAING CAPTURE ##########################
# Name of base directory
BASE_DIR = "Dataset"

# Starting capturing
cap = cv2.VideoCapture(0)

# Setting height and width of webcam
HEIGHT, WIDTH = 360, 640
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

####################### Getting arguments from command promt ##########################

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
                help="Name of the Gesture")
args = vars(ap.parse_args())
g_name = args["name"]

# Creating drectory of gesturres name if does not exist
g_dir = os.path.join(BASE_DIR, g_name)
os.makedirs(g_dir, exist_ok=True)
print("Made folder name "+str(g_name))

counter = 0
####################### Starting capturing ##########################
print("Starting Capturing .......")
while(1):

    # counter to get count of no of images saved

    ret, frame = cap.read()

    # avoid mirror image
    frame = cv2.flip(frame, 1)

    # bounding box from previous script
    bbox = [561,  83, 384, 287]

    # Make a rectabgle for visual help
    cv2.rectangle(frame, (bbox[0], bbox[1]),
                  (bbox[2], bbox[3]), (255, 0, 0), 2)
    #[x1, y1, x2, y2]

    # Cropping rectangle
    rect = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]

    # if user presses "s" saves image in that folder
    if cv2.waitKey(1) & 0xFF == ord('s'):

        # storing dynaic name of the file
        f_name = f"{g_name}-{counter}.jpg"
        # writing the image
        cv2.imwrite(os.path.join(g_dir, f_name), rect)

        print("Saving "+str(f_name))

        # printing on screen the counter

        # updating count
        counter = counter+1
    cv2.putText(frame, f"Counter for {g_name} : {counter}",
                (100, 38), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0, 2))
    cv2.imshow("frame", frame)
    #cv2.imshow("bbox", rect)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

#[561, 83, 384, 287]
