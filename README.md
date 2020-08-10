# Single Hand Gesture Classifer


Bharatanatyam also previously called Sadir Attam is a major form of Indian classical dance that is indigenous to Tamil Nadu. Bharata Natyam is the oldest classical dance tradition in India.This repo guides you to train a model for classifying 28 Mudras in this dance form using Machine Learning

## Highlights
  - Classifies 28 types of mudras
  - Script for making your own dataset
  - Training Model

# Steps for dataset

  - Determine the boubnding box of the rectangle for capturing hand gesture [Make sure it is atleast 224 by 224 minimum]
    ```sg
    $ python box_window_calc.py
     ```
  - Make atleast 50 captures per class of gesture using the script dataset.py
    ```sg
    $ python dataset.py -n "Gesture_name"
  
  - Set preprocessing accoring to to lighting using the script preprocess.py
    ```sg
    $ python preprocess.py 

     ```
