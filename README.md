# Single Hand Gesture Classifer


![alt text](https://github.com/krishshah99615/Single-Hand-Gesture/blob/master/Readme%20image/ss.jpeg)

Bharatanatyam also previously called Sadir Attam is a major form of Indian classical dance that is indigenous to Tamil Nadu. Bharata Natyam is the oldest classical dance tradition in India.This repo guides you to train a model for classifying 28 Mudras in this dance form using Machine Learning

## Highlights
  - Classifies 28 types of mudras [Currently only 3]
  - Script for Tesing on Webcam
  - Preprocess dataset for lighting conditions
  - Training a pretrained Model [VGG16]
 
  
### Current models performance while training
  - No of images in each category approx  : 50 Images
  - Validation accuracy :0.93478
  - Train accuracy :1.0000 [Over fit due to small dataset]
  - F1 ,Recall ,Precision :
  
  ![alt text](https://github.com/krishshah99615/Single-Hand-Gesture/blob/master/Readme%20image/cr.JPG)
  
  - Confusion matrix :
  
  ![alt text](https://github.com/krishshah99615/Single-Hand-Gesture/blob/master/Readme%20image/cm.JPG)
  
  - Training graphs for accuracy and loss:
  
  ![alt text](https://github.com/krishshah99615/Single-Hand-Gesture/blob/master/Readme%20image/accuracy.JPG)
  ![alt text](https://github.com/krishshah99615/Single-Hand-Gesture/blob/master/Readme%20image/loss.JPG)
  
  
# Steps for Requirements

  - Make sure u have pip , install follwing libraries using this command
    ```sh
    $ pip install -r requirements.txt
    
# Steps for dataset

  - Determine the boubnding box of the rectangle for capturing hand gesture [Make sure it is atleast 224 by 224 minimum]
    ```sh
    $ python box_window_calc.py
     ```
  - Make atleast 50 captures per class of gesture using the script dataset.py
    ```sh
    $ python dataset.py -n "Gesture_name"
  
  - Set preprocessing accoring to to lighting using the script preprocess.py [*OPTIONAL*]
    ```sh
    $ python preprocess.py 

     ```
# Steps for Training

  - Go to the follwing link
    ```sh
    $ jupyter notebook Training/Training.ipynb
     ```

# Steps for Testing on Webcam

  - for checking if model is working run the following script where -m referes to models path
    ```sh
    $ python inference.py -m "model.h5"
     ```
