####################### LIBRARRIES ##########################
import cv2
import numpy as np
import os
import glob

# Load Locations of images
list_of_images = glob.glob('Dataset/pataka/*.jpg')
print(len(list_of_images))

############### CONSTANTS #########################
# Upper and lower bounds in HSV Space
lower = np.array([0, 25, 90], dtype=np.uint8)
upper = np.array([20, 255, 255], dtype=np.uint8)
# DIlation kernel and iteration
dilate_kernel = np.ones((1, 1), np.uint8)
it = 2
# Gaussian Blur kernel and threshold
gaussian_kernel = (3, 3)
x_thresh = 100
###################################################

#################### Preprocess ###############################


def preprocess(name):
    img = cv2.imread(name)

    converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(converted, lower, upper)
    mask_d = cv2.dilate(mask, dilate_kernel, iterations=it)
    mask_b = cv2.GaussianBlur(mask_d, gaussian_kernel, x_thresh)

    return mask_b


while(1):

    ## Example image 1  ###
    img = preprocess(list_of_images[1])
    cv2.imshow("s", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break


cv2.destroyAllWindows()
