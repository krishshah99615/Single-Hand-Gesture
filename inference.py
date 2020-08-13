####################### LIBRARRIES ##########################
import cv2
import numpy
import os
import argparse
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
####################### INITIALIZAING CAPTURE ##########################

labels = {'Shikhara': 0, 'Simhamukha': 1, 'Trishula': 2}
labels = dict({(u, v) for (v, u) in labels.items()})


# Starting capturing
cap = cv2.VideoCapture(0)

# Setting height and width of webcam
HEIGHT, WIDTH = 360, 640
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

####################### Getting arguments from command promt ##########################

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
                help="model")
args = vars(ap.parse_args())
m_name = args["model"]
model = load_model(m_name)
print("Model Loaded")


####################### Starting capturing ##########################
print("Starting Capturing .......")
while(1):

    # counter to get count of no of images saved

    ret, frame = cap.read()

    # avoid mirror image
    frame = cv2.flip(frame, 1)

    # bounding box from previous script
    bbox = [346, 123, 544, 312]

    # Make a rectabgle for visual help
    cv2.rectangle(frame, (bbox[0], bbox[1]),
                  (bbox[2], bbox[3]), (255, 0, 0), 2)
    # [x1, y1, x2, y2]

    # Cropping rectangle
    rect = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]

    rect = cv2.resize(rect, (224, 224))
    rect = np.reshape(rect, (1, 224, 224, 3))
    rect = rect/255

    i = np.argmax(model.predict(rect)[0])
    p = labels[i]
    print(p)
    cv2.imshow("frame", frame)
    # cv2.imshow("bbox", rect)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

# [561, 83, 384, 287]
